import re

filename = raw_input("file: ")
#filename = "ender_tmp.txt"
file = open(filename,"r")
filestr = ""
fileall = ""
for line in file:
	fileall += line
	filestr += line.replace("\n", " ")

#everything, punctuation and all
count = 0
quote = 0
temp = ""
everything = []
ender = ".","?","!" #incase delimiters changes
for count in range(0, len(fileall)):
	char = fileall[count]
	#quote starting
	if char == "\"":
		temp += char
		if quote == 0:
			quote = 1
		else: 
			#quote ending, nothing following
			if fileall[count + 1] == "\n":
				temp += " "
				everything.append(temp)
				temp = ""
				count += 1
				quote = 0
			else: 
				quote = 0
	else: 
		#in quote, continue no matter what
		if quote == 1:
			if char != "\n":
				temp += char
			else: 
				temp += " "
		#out of quote, sentence ended
		elif char in ender:
			temp += char + " "
			everything.append(temp)
			temp = ""
		else: 
			if char != "\n":
				temp += char
			else:
				temp += " "


#just sentences and commas
delimiters = ".","?","!", "\""
regexPattern = '|'.join(map(re.escape, delimiters))
#creates list delimited by delimiters 
content = re.split(regexPattern,filestr)
just_sentences = []
for x in content:
	if len(x) > 2:
		just_sentences.append(x)
	#attempt to concat quotes properly
	'''
	if len(x) > 0:
		num = x.count("\"")
		if num == 1:
			if start == 0: 
				start = 1
				temp = ""
				temp += x
			else:
				start = 0
				temp += x
				final.append(temp)
				temp = ""
		elif num == 2:
			final.append(x)
		elif start == 1:
			temp += x
		else:
			final.append(x)
	'''

#tried to add quoted areas
'''
		if len(x) == 1 and x == "\"":
			print content[count-1] + content[count]
			content[count-1:count] = [''.join(content[count-1:count])]
		count += 1
'''


