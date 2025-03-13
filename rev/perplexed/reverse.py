flag = b"\xe1\xa7\x1e\xf8\x75\x23\x7b\x61\xb9\x9d\xfc\x5a\x5b\xdf\x69\xd2\xfe\x1b\xed\xf4\xed\x67\xf4"

binary = []
for byte in flag:
    binary.append(bin(int(byte))[2:][::-1])

binary = [chr(int(char, 2)) for char in binary]
print(''.join(binary))