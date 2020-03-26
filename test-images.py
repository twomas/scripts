#!/usr/bin/python3

import json

def show(str):
	print(' ')
	print(str)
	print(' ')

def main():
	with open('images.json') as f:
	  data_dict = json.load(f)

	for object in data_dict:
		url = object['url']
		name = object['name']
		sentence = url + '\n' + name
		show(sentence)

if __name__ == "__main__":
	main()
