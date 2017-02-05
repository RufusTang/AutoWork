# -*- coding:utf-8 -*-

import pyperclip,re

#Distill the str from clipboard
#text = str(pyperclip.paste())
text = r'''111-111-1111
222-222-2222
333-333-3333'''
print text

phoneregex = re.compile(r'''(\d{3}|\(\d{3}\))?
                        (\s|-|\.)
                        (\d{3})
                        (\s|-|\.)
                        (\d{4})''',re.VERBOSE|re.DOTALL|re.IGNORECASE)

matchs = []
for groups in phoneregex.findall(text):
    phonenum = '-'.join([groups[0],groups[2],groups[4]])
    matchs.append(phonenum)

print matchs

if len(matchs) > 0:
    pyperclip.copy('\n'.join(matchs))
    print "copied to clipboard"
    print '\n'.join(matchs)
else:
    print 'not found'