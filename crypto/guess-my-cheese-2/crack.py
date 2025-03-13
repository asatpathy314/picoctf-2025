import rsa
import json
from binascii import hexlify

def prepend(a, b):
    return a + b

def postpend(a, b):
    return b + a

def prepostpend(a, b):
    return b[0] + a + b[1]

def create_rainbow_table(cheese_file):
    with open(cheese_file, "r") as f:
        cheeses = [line.strip() for line in f.readlines()]

    salting_engine = [
        lambda x, y: prepend(x, y),
        lambda x, y: postpend(x, y),
        lambda x, y: prepostpend(x, y),
    ]

    preparation_engine = [
        lambda x: x.upper(),
        lambda x: x.lower()
    ]

    rainbow_table = dict()
    # Iterate through all possible 2-nibble hex values (00-FF)
    for salt in [f"{i:02x}" for i in range(256)]:
        print(salt)
        for cheese in cheeses:
            for salter in salting_engine:
                for preparer in preparation_engine:
                    # Concatenate cheese with the hex salt
                    salted_cheese = salter(cheese, preparer(salt))
                    # Create SHA256 hash
                    h = rsa.compute_hash(salted_cheese.encode('ascii'), method_name="SHA-256")
                    digest = hexlify(h).decode('ascii')
                    # Store the original cheese (without salt) as the value
                    rainbow_table[digest] = (cheese, preparer(salt))
            
    with open("rainbow_table.json", "w") as f:
        json.dump(rainbow_table, f)

if __name__ == "__main__":
    create_rainbow_table("cheese_list.txt")
    with open("rainbow_table.json", "r") as f:
        table = json.load(f)

    while True:
        query = input("Input a hash to look it up in the table: ")
        print(bytes(query, encoding='ascii'))
        if query in table:
            print(f"Cheese is {table[query]}.")
        else:
            print("Cheese not found.")