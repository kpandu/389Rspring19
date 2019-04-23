#!/usr/bin/env python3

import hashlib
import string
  

def crack():
    hashes = open("hashes.txt", "r")
    passwords = open("passwords.txt", "r").readlines()
    characters = string.ascii_lowercase
    map = {}
    for c in characters:
        for p in passwords:
            strip = p.strip()
            h = hashlib.sha256((c + strip).encode()).hexdigest()
            map[h] = c + strip
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52
    for h in hashes:
        if (map[h.strip()] != None):
            print(map[h.strip()] + ":" + h)
    
if __name__ == "__main__":
    crack()
