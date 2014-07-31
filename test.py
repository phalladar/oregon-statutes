# coding=utf-8
import re, pprint, pickle

theString = """

​Oregon Revised Statutes (ORS)
2013 Edition


The Oregon Revised Statutes are codified laws of the State of Oregon. The ORS is published every two years. Each edition of the ORS incorporates all laws, and changes to laws, enacted by the Legislative Assembly through the odd-numbered year regular session referenced in the volume titles for that edition. Purchase the Oregon Revised Statutes.
Oregon Rules of Civil Procedure (2013)

 

SCOPE; CONSTRUCTION; APPLICATION; RULE; CITATION

 

1 A Scope

1 B Construction

1 C Application

1 D “Rule” defined and local rules

1 E Use of declaration under penalty of perjury in lieu of affidavit; “declaration” defined

1 F Electronic filing

1 G Citation

 

FORM OF ACTION

 

2 One form of action

 

COMMENCEMENT

 

3 Commencement of action

 

JURISDICTION

(Personal)

 

4 Personal jurisdiction

4 A Local presence or status

4 B Special jurisdiction statutes
"""

theHeader = "SCOPE; CONSTRUCTION; APPLICATION; RULE; CITATION"
#print theHeader
# findHeader = theString.find(theHeader)
# theString = theString[0:findHeader] + '<h2>' + theString[findHeader:findHeader+len(theHeader)] + '</h2>' + theString[findHeader + len(theHeader):]

theString = theString.replace(theHeader, 'NOOOOOOOOOOOOOOOOOOO')

print theString