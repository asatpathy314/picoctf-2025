def reverse_engineer_flag():
    # Encoded flag from the C code
    enc_flag = [
        0xE1, 0xA7, 0x1E, 0xF8, 0x75, 0x23, 0x7B, 0x61, 
        0xB9, 0x9D, 0xFC, 0x5A, 0x5B, 0xDF, 0x69, 0xD2, 
        0xFE, 0x1B, 0xED, 0xF4, 0xED, 0x67, 0xF4
    ]
    
    # Convert to binary representation
    enc_bits = []
    for byte in enc_flag:
        # Convert to 8-bit binary representation
        bits = [(byte >> i) & 1 for i in range(7, -1, -1)]
        enc_bits.extend(bits)
    
    # Reconstruct the flag
    flag_bits = []
    local_20 = 0
    
    for enc_bit in enc_bits:
        if local_20 == 0:
            local_20 = 1
        
        flag_bits.append(enc_bit)
        
        local_20 += 1
        if local_20 == 8:
            local_20 = 0
    
    # Convert bits to bytes
    flag_bytes = []
    for i in range(0, len(flag_bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(flag_bits):
                byte = (byte << 1) | flag_bits[i + j]
        flag_bytes.append(byte)
    
    # Convert bytes to ASCII
    flag = ''.join(chr(b) for b in flag_bytes)
    return flag

print(reverse_engineer_flag())
