import hashlib
import itertools

def solve_cheese_challenge():
    # Read the list of possible cheeses
    with open("cheese_list.txt", "r") as f:
        cheese_list = [line.strip() for line in f]
    
    # The target hash we need to match
    target_hash = "6b75f4e10d0eb94012adc4880313d0b23cef33a86a58058c1ed55e94b9825693"
    
    # Try each cheese with each possible byte value at each position
    for cheese in cheese_list:
        for position in range(len(cheese) + 1):  # +1 to include position after the last character
            for byte_value in range(256):  # All possible byte values (0-255)
                # Insert the byte at the current position
                byte_to_insert = bytes([byte_value])
                modified_cheese = cheese[:position].encode() + byte_to_insert + cheese[position:].encode()
                
                # Calculate SHA-256 hash
                hash_obj = hashlib.sha256(modified_cheese)
                hash_value = hash_obj.hexdigest()
                
                # Check if hash matches target
                if hash_value == target_hash:
                    return cheese, position, byte_value, modified_cheese
        
        # Print progress to show the code is working
        print(f"Checked cheese: {cheese}")
    
    return None, None, None, None

# Run the solver
cheese, position, byte_value, modified_cheese = solve_cheese_challenge()

if cheese:
    print(f"Found the cheese: {cheese}")
    print(f"Byte inserted: {byte_value} (hex: {byte_value:02x})")
    print(f"Position: {position}")
    print(f"Full string that was hashed: {modified_cheese}")
    print(f"Full string (hex): {modified_cheese.hex()}")
else:
    print("No matching cheese found.")
