import hashlib
import itertools

def solve_cheese_challenge():
    # Read the list of possible cheeses
    with open("cheese_list.txt", "r") as f:
        cheese_list = [line.strip() for line in f]
    
    # The target hash we need to match
    target_hash = "9a367bdfe8dff8f142b5723ca84e75d03b9fe7a4cd48615fb122a5515bb7fd6d"
    
    # Try each cheese with each possible byte value at each position
    for cheese in cheese_list:
        for letter in range(0, 256):
            modified_cheese = cheese

            # Calculate SHA-256 hash
            hash_obj = hashlib.sha256(bytes(letter) + modified_cheese.encode('ascii'))
            hash_value = hash_obj.hexdigest()
            print(hash_value)
            
            # Check if hash matches target
            if hash_value == target_hash:
                return modified_cheese
        
        # Print progress to show the code is working
        print(f"Checked cheese: {cheese}")
    
    return None

# Run the solver
modified_cheese = solve_cheese_challenge()

if modified_cheese:
    print(f"Found the cheese: {modified_cheese}")
else:
    print("No matching cheese found.")
