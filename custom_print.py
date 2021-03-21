from time import sleep
from random import choice

import os

os.system('')

colors = {
    'purple':		'\033[95m',
    'blue': 		'\033[94m',
    'cyan': 		'\033[96m',
    'green': 		'\033[92m',
    'yellow': 		'\033[93m',
    'red': 			'\033[91m',
    'end': 			'\033[0m',
    'bold': 		'\033[1m',
    'underline': 	'\033[4m'
}

def _random_sleep():
	"""Generates random sleep time to simulate realistic typing."""
	return choice([0.05, 0.1, 0.15, 0.2])

def cprint(string, sleep_time=None, color=None):
	"""Custom print simulates someone typing.

	Keyword arguments:
	sleep_time -- how long to wait before printing the next letter, defaults to random (default None)
	color --  what color is printed (default None)
	"""
	start_color = colors.get(color, '')
	end_color = colors.get('end') if color else ''
	for i in range(len(string)):
		print(
			f"{start_color}{string[i]}{end_color}", 
			end="", 
			flush=True); sleep(sleep_time or _random_sleep()
		);
	print("\n")


# Examples - uncomment and run this script to see how it works.
# cprint("this is a test string.")
# cprint("this is a test string.", 0.01, 'red')
# cprint("this is a test string.", 0.05, 'blue')
# cprint("this is a test string.", 0.1, 'green')