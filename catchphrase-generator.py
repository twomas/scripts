#!/usr/bin/python3

import sys
import json
from random import randrange

msgglobal = ' ' # global

def requester(url,debug):
	data_dict = None
	try:
		# python -m pip install requests
		import requests
		
		response = requests.get(url, timeout=(1, 2))
		if debug:
			print(url)
			print(response) 
	except:
		pass
	
	try:
		#print(json.loads(response.text))
		data_dict = json.loads(response.text)
		#print(data_dict)
	except:
		pass
		
	return data_dict

def notification(title,msg):
	try:
		# python -m pip install plyer
		from plyer import notification

		notification.notify(
			title = title,
			message = msg,
			app_icon = None,  # e.g. 'C:\\icon_32x32.ico'
			timeout = 5,  # seconds
		)
	except:
		pass

def show(str):
	global msgglobal
	print(' ')
	print(str)
	print(' ')
	msgglobal = str

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
			show(sentence)
		except:
			if debug:
				print('quotes error!')
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
			show(sentence)
		except:
			if debug:
				print('words error!')
			pass

# https://github.com/twomas/scripts/blob/master/phrases.json
def phrases(str_url,debug):
	if debug:
		print('phrases')
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
			more = data_dict[index]['more']
			sentence = text + '\n' + more
			show(sentence)
		except:
			if debug:
				print('phrases error!')
			pass
			
def main():

	global msgglobal
	debug = False
	title = None
	
	try:
		import argparse
		
		parser = argparse.ArgumentParser()
		parser.add_argument("-d", "--debug", help="debug info", action="store_true")
		parser.add_argument("-t", "--test", help="run tests", action="store_true")
		parser.add_argument("-n", "--notify", help="show notification", type=str)
		args = parser.parse_args()
		if args.notify:
			title = args.notify
		if args.debug:
			debug = True
		if args.test:
			print('test mode!!!')
			if debug:
				print(' ')
			# test some errors
			if debug:
				print('test some errors')
				print(' ')
			quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.jsonnnn',debug)
			words('https://randomwordgenerator.com/json/questions.json','questionnnn',debug)
			words('https://randomwordgeneratorrrr.com/json/questions.json','question',debug)
			# should be ok
			if debug:
				print(' ')
				print('should be ok')
				print(' ')
			requester('https://lionseksjo.wordpress.com/kontakt/',debug)
			quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.json',debug)
			words('https://randomwordgenerator.com/json/facts.json','fact',debug)
			words('https://randomwordgenerator.com/json/act-of-kindness.json','act_of_kindness',debug)
			words('https://randomwordgenerator.com/json/sentences.json','sentence',debug)
			words('https://randomwordgenerator.com/json/questions.json','question',debug)
			words('https://randomwordgenerator.com/json/fake-words.json','word',debug)
			words('https://randomwordgenerator.com/json/make-money.json','idea',debug)
			words('https://randomwordgenerator.com/json/phrases.json',None,debug)
			phrases('https://raw.githubusercontent.com/twomas/scripts/master/phrases.json',debug)
	except:
		if debug:
			print('test error!')
		debug = False
	
	random = randrange(6+2) # An effort to hit quotes more often
	if debug:
		print('random number: ' + str(random))
	
	if random == 0:
		words('https://randomwordgenerator.com/json/phrases.json',None,debug)
	elif random == 1:
		words('https://randomwordgenerator.com/json/facts.json','fact',debug)
	elif random == 2:
		words('https://randomwordgenerator.com/json/act-of-kindness.json','act_of_kindness',debug)
	elif random == 3:
		words('https://randomwordgenerator.com/json/fake-words.json','word',debug)
	elif random == 4:
		words('https://randomwordgenerator.com/json/questions.json','question',debug)
	elif random == 5:
		phrases('https://raw.githubusercontent.com/twomas/scripts/master/phrases.json',debug)
	else:
		quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.json',debug)
		
	if title:
		if debug:
			try:
				print('title:')
				print(title)
			except:
				pass
		notification(title,msgglobal)

if __name__ == "__main__":
	main()
