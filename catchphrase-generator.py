#!/usr/bin/python3
# From https://github.com/twomas/scripts

import sys
import json
import os
import base64
import shutil
from random import randrange
from datetime import datetime
from io import BytesIO

msgglobal = ' ' # global

def requester(url,stream,debug):
	response = None
	try:
		# python -m pip install requests
		import requests
		
		response = requests.get(url,stream=stream,timeout=(1, 2))
		debugPrint(url + ' ' + str(response),debug)
	except:
		pass

	return response

def getJson(url,debug):
	data_dict = None

	try:
		response = requester(url,False,debug)
		#print(json.loads(response.text))
		data_dict = json.loads(response.text)
		#print(data_dict)
	except:
		pass

	return data_dict

def debugPrint(msg,debug):
	if debug:
		print(' ')
		print('    ' + msg)
		print(' ')

def show(str):
	global msgglobal
	print(' ')
	print(str)
	print(' ')
	msgglobal = str

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

def popuploop(title,msg,seconds):
	# python -m pip install pysimplegui
	import PySimpleGUI as sg
	
	sg.theme('DarkBlack')	# Add a touch of color
	# All the stuff inside your window.
	layout = [ [ sg.Text(msg) ] ]

	# Create the Window
	if title:
		window = sg.Window(title, layout, no_titlebar=False, alpha_channel=.5, grab_anywhere=True)
	else:
		window = sg.Window(title, layout, no_titlebar=True, alpha_channel=.5, grab_anywhere=True)
	
	event, values = window.Read(timeout=seconds * 1000) 
	window.close()

def downloadDilbertImage(dirName,debug):
	try:
		dateTimeObj = datetime.now()
		day = dateTimeObj.strftime('%d')
		name = 'dilbert-' + day + '.png'
		path = dirName + name
		# Only download if new day
		if not os.path.exists(path):
			response = requester('https://dilbert.com/',False,debug)
			content = str(response.content)
			res = content.partition('data-image=')[2]
			res = res.split('"')
			url = 'http:' + res[1]
			downloadImage(url,dirName,name,debug)
	except:
		debugPrint('downloadDilbertImage error!',debug)
		pass

def downloadImage(url,dirName,file,debug):
	try:
		response = requester(url,True,debug)
		debugPrint(url + ' ' + file,debug)
		with open(dirName + file, 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response
	except:
		debugPrint('downloadImage error!',debug)
		pass

def downloadImages(dirName,file,debug):
	# Only download from file if directory does not exists
	if not os.path.exists(dirName):
		os.makedirs(dirName)
		
		debugPrint('downloadImages',debug)
		with open(file) as f:
			data_dict = json.load(f)
			
		for i in range(len(data_dict)):
			url = data_dict[i]['url']
			name = data_dict[i]['name']
			downloadImage(url,dirName,name,debug)
			
	downloadDilbertImage(dirName,debug)

def scaleImage(input_image_path,
				width,
				height,
				debug
				):
	from PIL import Image
	
	original_image = Image.open(input_image_path)
	w, h = original_image.size
	debugPrint('Original image size is {wide} wide x {height} '
		  'high'.format(wide=w, height=h),debug)
	if width and height:
		max_size = (width, height)
	elif width:
		max_size = (width, h)
	elif height:
		max_size = (w, height)
	else:
		# No width or height specified
		raise RuntimeError('Width or height required!')
	original_image.thumbnail(max_size, Image.ANTIALIAS)
	byte_io = BytesIO()
	original_image.save(byte_io, 'PNG')
	scaled_image = Image.open(byte_io)
	width, height = scaled_image.size
	debugPrint('Scaled image size is {wide} wide x {height} '
		  'high'.format(wide=width, height=height),debug)
		  
	return base64.b64encode(byte_io.getvalue()),width,height
		  
def getImage(width,height,debug):
	d = os.getcwd() + os.sep + 'images'
	
	pngfiles = []
	for subdir, dirs, files in os.walk(d):
		for file in files:
			filepath = subdir + os.sep + file
			if filepath.endswith('.png'):
				pngfiles.append(filepath)

	idx = randrange(int(len(pngfiles)))
	image = pngfiles[idx]

	debugPrint(image,debug)
	scaledimage = scaleImage(image,width,height,debug)

	return scaledimage

def popupimageloop(title,msg,seconds,alpha,width,debug):
	# python -m pip install pysimplegui
	import PySimpleGUI as sg
	
	height = width * 2
	result = getImage(height,width,debug)
	
	image = result[0]
	height = result[1]
	width = result[2]
	
	sg.theme('DarkBlack')	# Add a touch of color
	# All the stuff inside your window.
	layout = [ 
		[ sg.Text(msg) ],
		[ sg.Graph(
			canvas_size=(height, width),
			graph_bottom_left=(0, 0),
			graph_top_right=(height, height),
			key='graph'
		) ]
	]

	# Create the Window
	if title:
		window = sg.Window(title, layout, no_titlebar=False, alpha_channel=alpha, grab_anywhere=True)
	else:
		window = sg.Window(title, layout, no_titlebar=True, alpha_channel=alpha, grab_anywhere=True)

	window.Finalize()
	graph = window.Element('graph')
	graph.DrawImage(data=image, location=(0, height))

	event, values = window.Read(timeout=seconds * 1000) 
	window.close()

def random(dict,debug):
	size = len(dict)
	debugPrint('size: ' + str(size),debug)
	index = randrange(int(size))
	debugPrint('index: ' + str(index),debug)

	return index

# https://github.com/fortrabbit/quotes/blob/master/quotes.json
def quotes(str_url,debug):
	debugPrint('quotes',debug)

	for url in [str_url]:
		try:
			data_dict = getJson(url,debug)
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

	for url in [str_url]:
		try:
			data_dict = getJson(url,debug)
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

def phrasesFile(file,debug):
	debugPrint('phrasesFile',debug)
	try:
		with open(file) as f:
			data_dict = json.load(f)
		index = random(data_dict,debug)
		text = data_dict[index]['text']
		more = data_dict[index]['more']
		sentence = text + '\n' + more
		show(sentence)
	except:
		debugPrint('phrasesFile error!',debug)
		pass

def addTimeStamp(text):
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime('%H:%M:%S')
	body = text + '\n' + timestampStr
	return body

def main():

	global msgglobal
	debug = False
	notify = None
	popup1 = None
	popup2 = None
	popup3 = None
	popup3big = None
	delay = None
	timer = 5
	file = 'phrases.json'
	fileImages = 'images.json'
	dirNameDownloads = 'images' + os.sep + 'downloads' + os.sep
	
	phrases = 'my-phrases.json' # Check if user wants to override
	if os.path.exists(phrases):
		file = phrases

	
	images = 'my-images.json' # Check if user wants to override
	if os.path.exists(images):
		fileImages = images

	try:
		import argparse

		parser = argparse.ArgumentParser()
		parser.add_argument("-d", "--debug", help="debug info", action="store_true")
		parser.add_argument("-t", "--test", help="run tests", action="store_true")
		parser.add_argument("-n", "--notify", help="show notification", type=str)
		parser.add_argument("-p", "--popup1", help="show popup1", type=str)
		parser.add_argument("-q", "--popup2", help="show popup2", type=str)
		parser.add_argument("-i", "--popup3", help="show popup3", type=str)
		parser.add_argument("-j", "--popup3big", help="show popup3big", type=str)
		parser.add_argument("-c", "--delay", help="show popup time", type=str)
		parser.add_argument("-r", "--remove", help="remove images", action="store_true")
		parser.add_argument("-a", "--download", help="download images", action="store_true")
		args = parser.parse_args()

		if args.notify:
			notify = args.notify
		if args.popup1:
			popup1 = args.popup1
		if args.popup2:
			popup2 = args.popup2
		if args.popup3:
			popup3 = args.popup3
		if args.popup3big:
			popup3big = args.popup3big
		if args.delay:
			delay = args.delay
		if args.debug:
			debug = True
		if args.remove:
			shutil.rmtree(dirNameDownloads, ignore_errors=True)
			return
		if args.download:
			shutil.rmtree(dirNameDownloads, ignore_errors=True)
			downloadImages(dirNameDownloads,fileImages,debug)
			return
		if args.test:
			debugPrint('test mode!!!',debug)
			# test some errors
			debugPrint('test some errors',debug)
			quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.jsonnnn',debug)
			words('https://randomwordgenerator.com/json/questions.json','questionnnn',debug)
			words('https://randomwordgeneratorrrr.com/json/questions.json','question',debug)
			# should be ok
			debugPrint('should be ok',debug)
			getJson('https://lionseksjo.wordpress.com/kontakt/',debug)
			quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.json',debug)
			words('https://randomwordgenerator.com/json/facts.json','fact',debug)
			words('https://randomwordgenerator.com/json/act-of-kindness.json','act_of_kindness',debug)
			words('https://randomwordgenerator.com/json/sentences.json','sentence',debug)
			words('https://randomwordgenerator.com/json/questions.json','question',debug)
			words('https://randomwordgenerator.com/json/fake-words.json','word',debug)
			words('https://randomwordgenerator.com/json/make-money.json','idea',debug)
			words('https://randomwordgenerator.com/json/phrases.json',None,debug)
			phrasesFile(file,debug)
			delay = 5
			notify = 'notify'
			popup1 = 'popup1'
			popup2 = 'popup2'
			popup3 = 'popup3'
			popup3big = 'popup3big'
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
		phrasesFile(file,debug)
	else:
		quotes('https://raw.githubusercontent.com/fortrabbit/quotes/master/quotes.json',debug)

	if delay:
		timer = int(delay)

	if notify:
		try:
			body = msgglobal
			notification(notify,body,timer)
		except:
			pass
		
	if popup3big:
		try:
			downloadImages(dirNameDownloads,fileImages,debug)
			body = addTimeStamp(msgglobal)
			popupimageloop(popup3big,body,timer,0.7,250,debug)
		except:
			popup1 = popup3big

	if popup3:
		try:
			downloadImages(dirNameDownloads,fileImages,debug)
			body = addTimeStamp(msgglobal)
			popupimageloop(popup3,body,timer,0.7,90,debug)
		except:
			popup1 = popup3

	if popup1:
		try:
			body = addTimeStamp(msgglobal)
			popuploop(popup1,body,timer)
		except:
			pass

	if popup2:
		try:
			body = popup2 + '\n' + msgglobal
			body = addTimeStamp(body)
			popuploop(None,body,timer)
		except:
			pass

if __name__ == "__main__":
	main()
