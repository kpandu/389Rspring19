#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():

    passwords = open("passwords.txt", "r").readlines()
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337
    map = {}
    for c in characters:
        for p in passwords:
            strip = p.strip()
            h = hashlib.sha256((c + strip).encode()).hexdigest()
            map[h] = c + strip

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    data = data.decode('utf-8')   
    print(data)
    for x in range(3):
        h = data.split('\n')[2].strip()
        if (map[h] != None):
            s.send((map[h.strip()] + '\n').encode())
            time.sleep(2)
        data = s.recv(1024)
        data = data.decode('utf-8')   
        print(data)

    
if __name__ == "__main__":
    server_crack()
