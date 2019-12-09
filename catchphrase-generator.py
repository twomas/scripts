#!/usr/bin/python3

import requests
import json
from random import randrange

# https://randomwordgenerator.com/json/

def words(str_url,key):
	for url in [str_url]:
		try:
			response = requests.get(url, timeout=(1, 2))
			#print(json.loads(response.text))
			data_dict = json.loads(response.text)
			#print(data_dict)
			size = len(data_dict['data'])
			#print(size)
			index = randrange(int(size))
			#print(index)
			if not key:
				phrase = data_dict['data'][index]['phrase']
				meaning = data_dict['data'][index]['meaning']
				sentence = phrase + '\n' + 'Meaning: ' + meaning
			else:
				sentence = data_dict['data'][index][key]
			print(' ')
			print(sentence)
			print(' ')
		except:
			print(' ')
			
def main():
	random = randrange(4)
	#print(str(random))
	
	if random == 1:
		words('https://randomwordgenerator.com/json/questions.json','question')
	elif random == 2:
		words('https://randomwordgenerator.com/json/facts.json','fact')
	elif random == 3:
		words('https://randomwordgenerator.com/json/act-of-kindness.json','act_of_kindness')
	elif random == 4:
		words('https://randomwordgenerator.com/json/act-of-kindness.json','inspirational-quote')
	else:
		words('https://randomwordgenerator.com/json/phrases.json', None)

if __name__ == "__main__":
	main()
