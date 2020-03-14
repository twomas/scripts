#!/usr/bin/python3
# From https://github.com/twomas/scripts

import sys
import json
from random import randrange

msgglobal = ' ' # global

def debugPrint(msg,debug):
	if debug:
		print(' ')
		print('    ' + msg)
		print(' ')
	
def requester(url,debug):
	data_dict = None
	try:
		# python -m pip install requests
		import requests
		
		response = requests.get(url, timeout=(1, 2))
		debugPrint(url + ' ' + str(response),debug)

	except:
		pass
	
	try:
		#print(json.loads(response.text))
		data_dict = json.loads(response.text)
		#print(data_dict)
	except:
		pass
		
	return data_dict

def notification(title,msg,timer):
	try:
		# python -m pip install plyer
		from plyer import notification

		notification.notify(
			title = title,
			message = msg,
			app_icon = None,  # e.g. 'C:\\icon_32x32.ico'
			timeout = timer,  # seconds
		)
	except:
		pass

def show(str):
	global msgglobal
	print(' ')
	print(str)
	print(' ')
	msgglobal = str
	
def random(dict,debug):
	size = len(dict)
	debugPrint('size: ' + str(size),debug)
	index = randrange(int(size))
	debugPrint('index: ' + str(index),debug)
	
	return index

# https://github.com/fortrabbit/quotes/blob/master/quotes.json
def quotes(str_url,debug):
	debugPrint('quotes',debug)

	#for url in [str_url,str_url]:
	for url in [str_url]:
		try:
			data_dict = requester(url,debug)
			index = random(data_dict,debug)
			text = data_dict[index]['text']
			author = data_dict[index]['author']
			sentence = text + '\n' + 'Author: ' + author
			show(sentence)
		except:
			debugPrint('quotes error!',debug)
			pass

# https://randomwordgenerator.com/json/
def words(str_url,key,debug):
	debugPrint('words',debug)

	#for url in [str_url,str_url]:
	for url in [str_url]:
		try:
			data_dict = requester(url,debug)
			index = random(data_dict['data'],debug)
			if not key:
				phrase = data_dict['data'][index]['phrase']
				meaning = data_dict['data'][index]['meaning']
				sentence = phrase + '\n' + 'Meaning: ' + meaning
			else:
				sentence = data_dict['data'][index][key]
			show(sentence)
		except:
			debugPrint('words error!',debug)
			pass

# https://github.com/twomas/scripts/blob/master/phrases.json
def phrases(str_url,debug):
	debugPrint('phrases',debug)
	#for url in [str_url,str_url]:
	for url in [str_url]:
		try:
			data_dict = requester(url,debug)
			index = random(data_dict,debug)
			text = data_dict[index]['text']
			more = data_dict[index]['more']
			sentence = text + '\n' + more
			show(sentence)
		except:
			debugPrint('phrases error!',debug)
			pass

def popuploop(title,msg,seconds):
	# python -m pip install pysimplegui
	import PySimpleGUI as sg
	
	sg.theme('DarkBlack')   # Add a touch of color
	# All the stuff inside your window.
	layout = [ [ sg.Text(msg) ] ]

	# Create the Window
	if title:
		window = sg.Window(title, layout, no_titlebar=False, alpha_channel=.5, grab_anywhere=True)
	else:
		window = sg.Window(title, layout, no_titlebar=True, alpha_channel=.5, grab_anywhere=True)
	
	event, values = window.Read(timeout=seconds * 1000) 
	window.close()
			
def main():

	global msgglobal
	debug = False
	notify = None
	popup1 = None
	popup2 = None
	delay = None
	
	try:
		import argparse
		
		parser = argparse.ArgumentParser()
		parser.add_argument("-d", "--debug", help="debug info", action="store_true")
		parser.add_argument("-t", "--test", help="run tests", action="store_true")
		parser.add_argument("-n", "--notify", help="show notification", type=str)
		parser.add_argument("-p", "--popup1", help="show popup1", type=str)
		parser.add_argument("-q", "--popup2", help="show popup2", type=str)
		parser.add_argument("-c", "--delay", help="show popup time", type=str)
		args = parser.parse_args()
		
		if args.notify:
			notify = args.notify
		if args.popup1:
			popup1 = args.popup1
		if args.popup2:
			popup2 = args.popup2
		if args.delay:
			delay = args.delay
		if args.debug:
			debug = True
		if args.test:
			debugPrint('test mode!!!',debug)
			# test some errors
			debugPrint('test some errors',debug)
			quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.jsonnnn',debug)
			words('https://randomwordgenerator.com/json/questions.json','questionnnn',debug)
			words('https://randomwordgeneratorrrr.com/json/questions.json','question',debug)
			# should be ok
			debugPrint('should be ok',debug)
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
			delay = 5
			notify = 'notify'
			popup1 = 'popup1'
			popup2 = 'popup2'
	except:
		debugPrint('test error!',debug)
		debug = False
	
	random = randrange(6+2) # An effort to hit quotes more often
	debugPrint('random number: ' + str(random),debug)
	
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
		
	if notify:
		try:
			timer = '3'
			if delay:
				timer = int(delay)
			notification(notify,msgglobal,timer)
		except:
			pass
		
	if popup1:
		try:
			timer = '30'
			if delay:
				timer = int(delay)
			popuploop(popup1,msgglobal,timer)
		except:
			pass
			
	if popup2:
		try:
			text = popup2 + '\n' + msgglobal
			timer = '30'
			if delay:
				timer = int(delay)
			popuploop(None,text,timer)
		except:
			pass

if __name__ == "__main__":
	main()
