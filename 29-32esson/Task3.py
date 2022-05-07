#!/usr/bin/env python
from sys import argv

def task3_positional_arguments():
	while True:
		print("\nEnter phrases the please.\nIf you want to exit the programm you need to enter something like this")
		for i in argv:
			if argv[0] == i:
				continue
			print(i)
		user_phrases = input()
		for i in argv:
			if argv[0] == i:
				print("Congratulations!")
				continue
			if i == user_phrases:
		    	return 0
		print("\nTry again!")


task3_positional_arguments()
