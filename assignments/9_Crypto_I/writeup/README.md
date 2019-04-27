# Crypto I Writeup

Name: Krishan Panduwawala
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Krishan Panduwawala

## Assignment Writeup

### Part 1 (70 Pts)

### Part 2 (30 Pts)

Since I know that there is a single arbitrary lower-case letter before each password, I took every single combination of a lower-case letter and a password in the passwords.txt file (double for-loop). I make sure to remove any new line characters from the input. Then I encoded each result and called hashlib.sha256() which converts each result into a hash. I then store each hash into a hashmap where the key is hexdigest() of the hash.Now I can move to the hashes in hashes.txt and iterate through each hash and find a matching hash in the hash table I made. Then I can pull the password from the value field of the hash table and print it with the hash. 

For Part 2 I first connected to the ip using sockets on the port 1337. Then I use the split method to get access to the hash from the other data received, which is at index 2. With this hash I checked if it existed in a map which was generated in the same exact way as part 1. If it exists then return the value associated with the hash in the hash table. I would take the value which is the password and decode it and send it back through the socket. To prevent the script from hanging trying to receive data before the response from the server, I used time.sleep(2) to add a 2 second delay that would prevent the hanging. Finally I would receive the response which would again contain a hash to decode and send the corresponding password. Since the process is the same I put it all in a for-loop that would iterate 3 times. After the third time I received that flag: CMSC389R-{h@sh1ng_@nd_sl@sh1ng} . 

