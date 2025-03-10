import hashlib
import json

def create_rainbow_table(cheese_file):
    with open(cheese_file, "r") as f:
        cheeses = [line.strip() for line in f.readlines()]

    rainbow_table = dict()
    # Iterate through all possible 2-nibble hex values (00-FF)
    for salt in [f"{i:02x}" for i in range(256)]:
        for cheese in cheeses:
            # Concatenate cheese with the hex salt
            salted_cheese = cheese + salt
            # Create SHA256 hash
            h = hashlib.sha256()
            h.update(bytes(salted_cheese, encoding="utf-8"))
            digest = h.hexdigest()
            # Store the original cheese (without salt) as the value
            rainbow_table[digest] = cheese
            
    with open("rainbow_table.json", "w") as f:
        json.dump(rainbow_table, f)

if __name__ == "__main__":
    create_rainbow_table("cheese_list.txt")
    with open("rainbow_table.json", "r") as f:
        table = json.load(f)

    while True:
        query = input("Input a hash to look it up in the table: ")
        if query in table:
            print(f"Cheese is {table[query]}.")
        else:
            print("Cheese not found.")