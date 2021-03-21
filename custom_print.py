from time import sleep

def slow_print(string):
	for i in range(len(string)):
		print(string[i], end="", flush=True); sleep(0.2)
	print("\n")


