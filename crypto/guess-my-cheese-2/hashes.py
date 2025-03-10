import hashlib
import itertools
import string

def generate_hashes():
    hash = "21181a64c582cf753a444cd62722189d5115b12fb1c0cd4c692f2bd6193fd00e"
    for i in range(0, 65535):
        print(f"{hash}:{i}")

if __name__ == "__main__":
    generate_hashes()