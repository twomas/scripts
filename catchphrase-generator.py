#!/usr/bin/python3

import requests
import json
from random import randrange

# https://randomwordgenerator.com/json/

def anything(str_url,key):
	for url in [str_url]:
		try:
			response = requests.get(url)
			#print(json.loads(response.text))
			data_dict = json.loads(response.text)
			#print(data_dict)
			size = len(data_dict['data'])
			#print(size)
			index = randrange(int(size))
			#print(index)
			question = data_dict['data'][index][key]
			print(' ')
			print(question)
			print(' ')
		except:
			print(' ')

def phrase(str_url):
	for url in [str_url]:
		try:
			response = requests.get(url)
			#print(json.loads(response.text))
			data_dict = json.loads(response.text)
			#print(data_dict)
			size = len(data_dict['data'])
			#print(size)
			index = randrange(int(size))
			#print(index)
			phrase = data_dict['data'][index]['phrase']
			meaning = data_dict['data'][index]['meaning']
			print(' ')
			print(phrase)
			print('Meaning: ' + meaning)
			print(' ')
		except:
			print(' ')
			
def main():
	random = randrange(4)
	#print(str(random))
	
	if random == 1:
		anything('https://randomwordgenerator.com/json/questions.json','question')
	elif random == 2:
		anything('https://randomwordgenerator.com/json/facts.json','fact')
	elif random == 3:
		anything('https://randomwordgenerator.com/json/act-of-kindness.json','act_of_kindness')
	elif random == 4:
		anything('https://randomwordgenerator.com/json/act-of-kindness.json','inspirational-quote')
	else:
		phrase('https://randomwordgenerator.com/json/phrases.json')

main()
