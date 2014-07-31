# coding=utf-8
import re, pprint, pickle, win32com.client

word = win32com.client.Dispatch('Word.Application')


theString = open('civil-procedure.txt', 'r').read()

theHeadings = re.findall(r'\n([A-Z\s\;\,\.]+)\n', theString)
rulesArray = re.findall(r'\n\s*?(RULE\s\d*(?:\s\(.*\))?)', theString)
rulesSpecial = re.findall(r'(RULES \d+\sand\s\d+\s?\(.*\))', theString)

rulesArray = rulesArray + rulesSpecial

headingsArray = []

for i in theHeadings:
	i = i.split()
	if i != []:
		headingsArray.append(' '.join(i))
		#print ' '.join(i)

x = 0
for j in headingsArray:
	theHeader = headingsArray[x]
	theString = theString.replace(headingsArray[x], '<h2>' + headingsArray[x] + '</h2>', 1)
	x += 1

for rule in rulesArray:
	theString = theString.replace(rule, '<h3>' + rule + '</h3>', 1)

doc = word.Documents.Add(theString)
doc.SaveAs('statutes.doc', FileFormat=10)
doc.Close()

word.Quit()