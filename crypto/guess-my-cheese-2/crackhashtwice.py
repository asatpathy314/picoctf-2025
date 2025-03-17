import hashlib

def solve_cheese_challenge():
    # Read the list of possible cheeses
    with open("cheese_list.txt", "r") as f:
        cheese_list = [line.strip() for line in f]
    
    # The target hash we need to match
    target_hash = "6feb1e3c19273547edf66785cacaca99a5c7a4512baa79ceffbc776ef2ad0963"
    
    # Try each cheese
    for cheese in cheese_list:
        # First hash of the cheese
        first_hash = hashlib.sha256(cheese.encode()).digest()
        
        # Try inserting the salt at each position
        for position in range(len(first_hash) + 1):  # +1 to include position after the last byte
            for salt_value in range(256):  # All possible byte values (0-255)
                # Convert salt to bytes
                salt_byte = bytes([salt_value])
                
                # Insert salt at the current position
                salted_hash = first_hash[:position] + salt_byte + first_hash[position:]
                
                # Second hash
                final_hash = hashlib.sha256(salted_hash).hexdigest()
                
                # Check if hash matches target
                if final_hash == target_hash:
                    return cheese, position, salt_value, final_hash
        
        # Print progress to show the code is working
        print(f"Checked cheese: {cheese}")
    
    return None, None, None, None

# Run the solver
cheese, position, salt_value, hash_result = solve_cheese_challenge()

if cheese:
    print(f"Found the cheese: {cheese}")
    print(f"Salt value (decimal): {salt_value}")
    print(f"Salt value (hex): {salt_value:02x}")
    print(f"Salt position: {position}")
    print(f"Hash matches: {hash_result == target_hash}")
    
    # Show the exact process that produced the matching hash
    first_hash = hashlib.sha256(cheese.encode()).digest()
    salted_hash = first_hash[:position] + bytes([salt_value]) + first_hash[position:]
    verification_hash = hashlib.sha256(salted_hash).hexdigest()
    print(f"\nVerification:")
    print(f"First hash of '{cheese}': {first_hash.hex()}")
    print(f"After inserting byte {salt_value:02x} at position {position}: {salted_hash.hex()}")
    print(f"Final hash: {verification_hash}")
    print(f"Matches target: {verification_hash == target_hash}")
else:
    print("No matching cheese found.")
import hashlib

def solve_cheese_challenge():
    # Read the list of possible cheeses
    with open("cheese_list.txt", "r") as f:
        cheese_list = [line.strip() for line in f]
    
    # The target hash we need to match
    target_hash = "6feb1e3c19273547edf66785cacaca99a5c7a4512baa79ceffbc776ef2ad0963"
    
    # Try each cheese
    for cheese in cheese_list:
        # First hash of the cheese
        first_hash = hashlib.sha256(cheese.encode()).digest()
        
        # Try inserting the salt at each position
        for position in range(len(first_hash) + 1):  # +1 to include position after the last byte
            for salt_value in range(256):  # All possible byte values (0-255)
                # Convert salt to bytes
                salt_byte = bytes([salt_value])
                
                # Insert salt at the current position
                salted_hash = first_hash[:position] + salt_byte + first_hash[position:]
                
                # Second hash
                final_hash = hashlib.sha256(salted_hash).hexdigest()
                
                # Check if hash matches target
                if final_hash == target_hash:
                    return cheese, position, salt_value, final_hash
        
        # Print progress to show the code is working
        print(f"Checked cheese: {cheese}")
    
    return None, None, None, None

# Run the solver
cheese, position, salt_value, hash_result = solve_cheese_challenge()

if cheese:
    print(f"Found the cheese: {cheese}")
    print(f"Salt value (decimal): {salt_value}")
    print(f"Salt value (hex): {salt_value:02x}")
    print(f"Salt position: {position}")
    print(f"Hash matches: {hash_result == target_hash}")
    
    # Show the exact process that produced the matching hash
    first_hash = hashlib.sha256(cheese.encode()).digest()
    salted_hash = first_hash[:position] + bytes([salt_value]) + first_hash[position:]
    verification_hash = hashlib.sha256(salted_hash).hexdigest()
    print(f"\nVerification:")
    print(f"First hash of '{cheese}': {first_hash.hex()}")
    print(f"After inserting byte {salt_value:02x} at position {position}: {salted_hash.hex()}")
    print(f"Final hash: {verification_hash}")
    print(f"Matches target: {verification_hash == target_hash}")
else:
    print("No matching cheese found.")
