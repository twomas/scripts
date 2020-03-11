#!/usr/bin/python3

import json

def show(str):
	print(' ')
	print(str)
	print(' ')

def main():
	with open('phrases.json') as f:
	  array = json.load(f)

	for object in array:
		text = object['text']
		more = object['more']
		sentence = text + '\n' + more
		show(sentence)

if __name__ == "__main__":
	main()
