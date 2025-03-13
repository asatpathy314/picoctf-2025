import lzma
import struct
import sys

def decompress_lzma_with_truncation(input_file, output_file):
    # Read the compressed data
    with open(input_file, 'rb') as f:
        compressed_data = f.read()
    
    # Define XOR key values from the malware's FUN_1400018b0 function
    key_values = [
        0x14044ae, 0xe67c7320, 0xac2eda02, 0xd443ec8c, 
        0x92dd00b3, 0x12d71086, 0x7b3f64a4
    ]
    
    # Convert key values to bytes for XOR operation
    key_bytes = b''
    for val in key_values:
        key_bytes += val.to_bytes(4, byteorder='little')
    
    # Try to decompress with different truncation lengths
    data_len = len(compressed_data)
    
    # Start from the full length and work backwards
    for i in range(data_len, 0, -1):
        try:
            # Try to decompress the truncated data
            decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, 
                                                filters=[{'id': lzma.FILTER_LZMA1}])
            decompressed_data = decompressor.decompress(compressed_data[:i])
            
            # If we get here, decompression was successful
            print(f"Successfully decompressed {len(decompressed_data)} bytes after truncating to {i} bytes")
            
            # Decrypt the data using XOR with the key
            decrypted_data = bytearray(len(decompressed_data))
            for j in range(len(decompressed_data)):
                decrypted_data[j] = decompressed_data[j] ^ key_bytes[j % len(key_bytes)]
            
            # Write the decrypted data to the output file
            with open(output_file, 'wb') as f:
                f.write(bytes(decrypted_data))
            
            print(f"Successfully decrypted and saved to {output_file}")
            return
            
        except lzma.LZMAError:
            # If this truncation length doesn't work, try a shorter one
            continue
    
    print("Failed to decompress the file with any truncation length")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)
    
    decompress_lzma_with_truncation(sys.argv[1], sys.argv[2])
