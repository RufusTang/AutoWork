# -*- coding:utf-8 -*-

import urllib2,sys,webbrowser,bs4

import re

linkregel = re.compile(r"href=\"http:.*?\"",re.VERBOSE|re.DOTALL|re.IGNORECASE)

print "Baiding..."

res = urllib2.urlopen(r'http://www.baidu.com/s?wd=%s'%("luck"))

#TODO: Retrieve top search result links
soup = bs4.BeautifulSoup(res.read(),'html.parser')


#TODO: Open a browse tab for each result

links = soup.find_all(["div","a"],"result")


for link in links:
    print link
    print linkregel.findall(str(link))[0][6:-1]
