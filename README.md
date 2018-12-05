# rock_py
## Created by Taylor Mallory for CS372
## This project is a **very** simple dictionary attack, using Python 3 with the ftplib and time modules, as part of a networking assignment. It is intended for educational purposes only.

### About
rock_py is a simple FTP server dictionary attack program. It asks users for (and assumes they know) ip address, username, and port number of the target server. The program uses ftplib to connect to the given ip address, with port number, and then iterates over rockyou.txt, attempting to login with the given username and current line from the text file. An unsuccessful login is handled by passing the exception and continuing down the list of possible passwords.

### installation
0. Install Python 3
1. Download or clone repo
2. Download rockyou.txt [which can be found here] (https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
3. Move rockyou to repo containing rock_py

### check dependencies
0. From terminal, run `python3 -c "import ftplib"`
1. run `echo $?`
..* if output != 0, install ftplib by running `pip3 install ftplib`
2. From terminal, run `python3 -c "import time"`
3. run `echo $?`
..* if output != 0, install time by running `pip3 install time`

### to run rock_py
0. Move to directory containing rock_py
1. From terminal, type `python3 ./dict_attack.py` and follow prompts




#### TODO
-handle server disconnect
-multithread
