#!/usr/bin/python3

import sys
import json
from random import randrange

def requester(url,debug):
	try:
		import requests
		
		response = requests.get(url, timeout=(1, 2))
	except:
		pass
	
	try:
		#print(json.loads(response.text))
		data_dict = json.loads(response.text)
		#print(data_dict)
	except:
		pass
		
	return data_dict

# https://github.com/fortrabbit/quotes/blob/master/quotes.json
def quotes(str_url,debug):
	if debug:
		print('quotes')
	#for url in [str_url,str_url]:
	for url in [str_url]:
		try:
			data_dict = requester(url,debug)
			size = len(data_dict)
			if debug:
				print('size: ' + str(size))
			index = randrange(int(size))
			if debug:
				print('index: ' + str(index))
			text = data_dict[index]['text']
			author = data_dict[index]['author']
			sentence = text + '\n' + 'Author: ' + author
			print(' ')
			print(sentence)
			print(' ')
		except:
			pass

# https://randomwordgenerator.com/json/
def words(str_url,key,debug):
	if debug:
		print('words')
	#for url in [str_url,str_url]:
	for url in [str_url]:
		try:
			data_dict = requester(url,debug)
			size = len(data_dict['data'])
			if debug:
				print('size: ' + str(size))
			index = randrange(int(size))
			if debug:
				print('index: ' + str(index))
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
			pass
			
def main():

	debug = False
	
	try:
		import argparse
		
		parser = argparse.ArgumentParser()
		parser.add_argument("-d", "--debug", help="debug info", action="store_true")
		parser.add_argument("-t", "--test", help="run tests", action="store_true")
		args = parser.parse_args()
		if args.debug:
			debug = True
		if args.test:
			print('test mode!!!')
			if debug:
				print(' ')
			# test some errors
			quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.jsonnnn',debug)
			words('https://randomwordgenerator.com/json/questions.json','questionnnn',debug)
			words('https://randomwordgeneratorrrr.com/json/questions.json','question',debug)
			# should be ok
			quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.json',debug)
			words('https://randomwordgenerator.com/json/facts.json','fact',debug)
			words('https://randomwordgenerator.com/json/act-of-kindness.json','act_of_kindness',debug)
			words('https://randomwordgenerator.com/json/act-of-kindness.json','inspirational-quote',debug)
			words('https://randomwordgenerator.com/json/questions.json','question',debug)
			words('https://randomwordgenerator.com/json/phrases.json', None,debug)
			sys.exit()
	except:
		debug = False
	
	random = randrange(5+2) # An effort to hit quotes more often
	if debug:
		print('random number: ' + str(random))
	
	if random == 0:
		words('https://randomwordgenerator.com/json/phrases.json',None,debug)
	elif random == 1:
		words('https://randomwordgenerator.com/json/facts.json','fact',debug)
	elif random == 2:
		words('https://randomwordgenerator.com/json/act-of-kindness.json','act_of_kindness',debug)
	elif random == 3:
		words('https://randomwordgenerator.com/json/act-of-kindness.json','inspirational-quote',debug)
	elif random == 4:
		words('https://randomwordgenerator.com/json/questions.json','question',debug)
	else:
		quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.json',debug)

if __name__ == "__main__":
	main()
