# Not used
# Author : Satish Palaniappan
__author__ = "Satish Palaniappan"

import os, sys, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)


from twokenize import *
import re


Code  = r"\\[a-zA-Z0-9]+"

List = [
    Url_RE,
    Timelike,
    Code
]

# stoplist = [")","(",".","'",",",";",":","?","/","!","@","$","*","+","-","_","=","&","%","`","~","\"","{","}"]
stopwords = [s.strip() for s in open(cmd_folder + "/stopwords","r").readlines()]
# print(stopwords)

### Not Implemented
def prep (text):
	line = text
	line = re.sub(r"[@#]", '', line)
	for r in List:
		line = re.sub(r," ", line)
	for w in stopwords:
		line = line.replace(" " + w.strip() + " "," ")
	return line

def process(text):
	# text = prep(text.strip().lower())
	text = text.strip().lower()
	text = u" ".join(tokenize(text))
	return text.encode("utf-8")
