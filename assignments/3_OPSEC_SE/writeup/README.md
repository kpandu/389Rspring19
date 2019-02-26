# Writeup 3 - Operational Security and Social Engineering

Name: Krishan Panduwawala
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Krishan Panduwawala

## Assignment Writeup

### Part 1 (40 pts)
For the pretext I would claim to be a new cybersecurity specialist that is working on building up cybersecurity measures at 1337Bank. The slides mention that background noise improves the persuasiveness so I would include noise of people talking in an office to seem like I am at work. I would explain how the system is weak and that the best way to solve the vulnerabilities is through multi-factor authentication. I then would ask for her to be a test subject for the system before it is deployed to the actual website. I would then ask her to create an account on my fake site that mimics 1337Bank.money, but with the added security of security questions when making an account. These questions are then used when you forget your password. I would use the questions “What's her mother's maiden name?, What city was she born in?, What was the name of her first pet?” which are pretty common security questions. Then I would ask if everything went smoothly on her browser and ask what browser she uses mainly. Lastly, I would say that she needs to put in her bank account’s pin for 1337Bank everytime she logs in. So in my mimic site I would tell her to input her pin and see if it works. After all this I would say thanks for your time and I would ask for recommendations to remove suspicions. My mimic website would have stored all of her information for me to exploit later.

Since I am not that experienced in cybersecurity I can avoid many questions by saying that I am in a non-disclosure agreement with my company. I can avoid all the questions of how I found the vulnerabilities. From the slides, we learned that diving too deep into something you do not know will raise suspicion. I will be able to answer general cybersecurity questions as I plan to communicate through the phone or through email. I would be able to look information up while communicating without raising suscpicion. 



### Part 2 (60 pts)

The first vulnerability I found was the she had a weak password. I was able to find the password from trying common passwords on her website with a script. Not to mention she used the same username as her Twitter account to log into to her website’s shell. The website ConnectSafely mentions that passwords should be approximately 20 characters with symbols. I can confirm this because most of the passwords that was tried on the script were not very long and many did not have symbols. The more characters there are which means more combinations. This means it will take exponentially longer for a script to crack a password. The same website recommends using a password manager such as RoboForm or Lastpass. These store complex passwords for your accounts and are extremely difficult to crack. All you need is one password to access the password database and browsers like Google Chrome have one built in.

The second vulnerability was that she did not have any active security systems blocking intrusions. Intrusion detection systems (IDS) and intrusion prevention systems (IPS) monitor and block potential attacks. Juniper Networks mentions that “attacks are so sophisticated that they can thwart the best security systems, especially those that still operate under the assumption that networks can be secured by encryption or firewalls.” Firewalls are not enough to protect against hackers. Elizabeth and the web server could have implemented IDS and IPS to stop these sophisticated attacks and simple attacks such as the one I did. 

The third vulnerability was that port 1337 was open and the service behind it was accessible to anyone. To access the website shell anyone can access port 1337 and try passwords. First, the port was 1337 which is in the name of the website. To make this more secure the website admins could change the port number to make the hacker have more difficulty in figuring out the port. Second, only her and the admins need to access the system shell rather than anyone else. TechRadar claims that “closing ports you don’t need is...secure.” Elizabeth and the system admins can close the port until they need it which can lead to the security TechRadar claims. By turning off the port when the shell is not used increases the likelihood that the port is not found through nmap and other port scanning tools. She can also place a firewall behind the port which will control traffic and prevent non-admins (hackers) from gaining access to the service behind the port.  


https://www.juniper.net/us/en/products-services/what-is/ids-ips/

https://www.techradar.com/news/networking/how-to-secure-your-tcp-ip-ports-633089

https://www.connectsafely.org/tips-to-create-and-manage-strong-passwords/





