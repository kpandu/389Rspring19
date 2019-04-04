# Writeup 6 - Forensics

Name: Krishan Panduwawala
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Krishan Panduwawala

## Assignment Writeup

### Part 1 (45 Pts)
1. 142.93.136.81
2. 
    i) They are using command injection. This is shown  as the server’s response is “PORT 159,203,113,181,222,226” which meant the hackers were trying multiple ports. Then the server says “PORT command successful” which meant that the hackers were trying command injection on multiple ports until the command succeeded.

    ii) vsFTPd 3.03 which was at the top of the logs between the hackers and the server. They used this to transfer files.
3. Their ip is 159.203.113.181 which I found from the source to destination ip addresses since I knew the ip of the website. I found the file that the hackers stole and the destination IP from the server was the hackers’ IP. By putting the ip in Censys.io, I know that the hackers’ are connecting from Clifton, New Jersey

4. They are using port 20. Found when clicking on the packets when the greetz.fpff and find_me.jpeg were transferred between the server and the hackers.

5. 
    a) A photo called find_me.jpeg. The type of the file is jpeg. I downloaded the raw version of the file using WireShark. Then I was able to change the file type to jpg which let me see the photo. 

    b) The photo was taken at the beach which I found from the photo. I saw a large hand sculpture coming from the sand. I then searched up beaches with hand sculpture coming out of the sand. This brought me to beach called “La Mano (the hand)” which matched the hand statue exactly. The state of the sculpture is in Uruguay and the city is Punta del Este.

    c) It was taken on the Sunday, December 23, 2018 at 05:16:24 PM. I found this through exiftool on the photo.

    d) The back camera of an iPhone 8. This was also found using exiftool on the photo.

    e) 4.5 meters below sea level (exiftool).

6. They left a file called greetz.fpff . I found this through WireShark by filtering for the attackers’ IP and looking at the packets. There were multiple packets with “STOR greetz.fpff” with the destination ip as the website. This was a clear indication that greetz.fpff was being stored. I used the same process to find which file the attackers stole from the website.

7. A countermeasure to prevent this attack from happening is to add a firewall that will control what leaves and enters the file system. A firewalls job is to block unauthorized access from and to a private network. This would prevent hackers from putting files in the network and prevent the hackers accessing secured parts of the network.


### Part 2 (55 Pts)

1. The file was generated in 2019-03-27 at time 04:15:05

2. The author of the file was fl1nch who we know from previous assignments. 

3. 
    a) The first section is SECTION_ASCII and it contains “Hey you, keep looking :)”
    b) The second section is SECTION_COORD and it contains the coordinates “52.336035 4.880673”
    c) The third section is SECTION_PNG and it contains an image of testudo.
    d) The fourth section is SECTION_ASCII that contains the flag                                          “ }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC” which in reverse is “CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}. “
    e) The fifth section is SECTION_ASCII and it contains “Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=”
4. 
    a) CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
    I found this through parsing greetz.fpff and it was in the 4th section.

    b) CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak}
    I found this through parsing a png file in greetz.fpff . Upon opening the file I find a picture of testudo with the flag next to him.







