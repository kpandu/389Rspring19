# Crypto II Writeup

Name: Krishan Panduwawala
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Krishan Panduwawala

## Assignment Writeup

### Part 1 (70 Pts)
I first called "gpg --import key.asc" on the command line to import the private key so gpg can use it to decrypt. Then I 
called "gpg -d message.txt.gpg" to decrypt the message where I found the email "CMSC389R <fake@email.com>" followed by the flag 
"CMSC389R-{m3ss@g3_!n_A_b0ttl3}." Then I followed the directions in the file and created a file containing "My name is Krishan Panduwawala."
Then I encrypted it using "gpg --clearsign signature.txt" which created a file called signature.txt.asc . 
### Part 2 (30 Pts)
I notice in the ecb picture, that you can still see the outline of the original image, but the colors are scrambled. Each color is associated with a 
color scrambling pattern which distingishes the objects in the image. For example the red oval's colors in the ecb photo are different that the pattern of the white area surrounding it. This shows the outline of the objects. In the cbc image, the entire image is scrambled and nothing can be distinguished in the image. It is impossible to find any similarities to the original image, as it looks like a rainbow mess. This is a clear indication that the ECB mode is less secure than the CBC mode. 

In CBC mode you take each message block and encrypt it using aes in our case. This produces cipher text which can be XOR'd with the next message block and rerun through the aes algorithm. This produces another cipher where we can keep repeating the process for the rest of the blocks which creates the chain. For the first block, an IV is used to encrypt the first message block with XOR before it is put through aes and goes down the chain. Since each block uses the cipher from the previous block, the result is indistinguishable from the original message/image. ECB does not have an IV or a chain. It takes blocks of a message and runs it through a block ciper encryption. Since the encryption scheme is the same for each block, patterns arise such as the colors in the images having a specific pattern. There is not enough variability in ECB which is why it is less secure than CBC. ECB is not bad it just depends on the use case, for example not images.
