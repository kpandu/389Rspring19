#!/usr/bin/env python2

import sys
import struct
from datetime import datetime
offset = 8
png_count = 0
# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

timestamp,_ = struct.unpack("<LL", data[offset:offset+8])
offset = offset + 4
print("DATE: " + str(datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')))
author = struct.unpack("8s", data[offset:offset+8])
offset = offset + 8
print("Author: " + str(sorted(author)[0].decode('utf-8')))

section_count,_ = struct.unpack("<LL", data[offset:offset+8])
offset = offset + 4
section_count = int(section_count)
print("Section count: %d" % section_count)
if (section_count < 1):
    bork("Invalid section offset with size %d" % int(section_count))
# # We've parsed the magic and version out for you, but you're responsible for
# # the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
for i in range(section_count):
    section_type,_ = struct.unpack("<LL", data[offset:offset+8])
    offset = offset + 4
    section_type = int(section_type)

    slen,_ = struct.unpack("<LL", data[offset:offset+8])
    offset = offset + 4
    
    if (section_type == 1):
        print("SECTION_ASCII ")
        format = str(slen)+ "s"
        ascii = struct.unpack(format, data[offset:offset+slen])
        offset += slen  
        print(ascii[0].decode('utf-8'))
    elif (section_type == 2): 
        print("SECTION_UTF8 ")
        for j in range(slen):
            utf8 = struct.unpack("<LL", data[offset:offset+8])
            offset += slen 
            print(utf8.decode('utf-8'))
    elif (section_type == 3):
        print("SECTION_WORDS ")
        for j in range(slen/4):
            arr = struct.unpack("s", data[offset:offset+4])
            offset += 4
            print(arr[0].decode('utf-8')) 
    elif (section_type == 4): 
        print("SECTION_DWORDS ")
        for j in range(slen/8):
            arr = struct.unpack("s", data[offset:offset+8])
            offset += 8
            print(arr[0].decode('utf-8')) 
    elif (section_type == 5): 
        print("SECTION_DOUBLES")
        for j in range(slen/8):
            arr = struct.unpack("s", data[offset:offset+8])
            offset += 8
            print(arr[0].decode('utf-8')) 
    elif (section_type == 6):
        print("SECTION_COORD ")
        if (slen != 16):
            bork()
        coord = struct.unpack("dd", data[offset:offset+16])
        offset += 16
        print(coord[0], coord[1])    
        
    elif (section_type == 7): 
        print("SECTION_REFERENCE ")
        if (slen != 4):
            bork()
        indx = struct.unpack("s", data[offset:offset+4])
        offset += 4
        print(arr[0].decode('utf-8')) 
    elif (section_type == 8): 
        print("SECTION_PNG ")
        print("PNG STORED IN FILE: " + str(png_count) + "pic.png")
        format = str(slen)+ "s"
        file_name = str(png_count) + "pic.png"
        png_count += 1
        f = open(file_name, "wb")
        f.write(bytes([137,80,78,71,13,10,26,10]))
        string = struct.unpack(format, data[offset:offset+slen])
        offset += slen
        string = string[0]
        f.write(string)
        f.close()
    elif (section_type == 9):
        print("SECTION_GIF87 ")
        print("GIF STORED IN FILE: " + str(png_count) + "pic.gif")
        format = str(slen)+ "s"
        file_name = str(png_count) + "pic.gif"
        png_count += 1
        f = open(file_name, "wb")
        f.write("GIF87a".encode('utf-8'))
        string = struct.unpack(format, data[offset:offset+slen])
        offset += slen
        string = string[0]
        f.write(string)
        f.close()  
    elif (section_type == 10): 
        print("SECTION_GIF89 ")
        print("GIF STORED IN FILE: " + str(png_count) + "pic.gif")
        format = str(slen)+ "s"
        file_name = str(png_count) + "pic.gif"
        png_count += 1
        f = open(file_name, "wb")
        f.write("GIF89a".encode('utf-8'))
        string = struct.unpack(format, data[offset:offset+slen])
        offset += slen
        string = string[0]
        f.write(string)
        f.close()  
    print('\n')
    
