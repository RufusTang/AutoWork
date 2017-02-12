# -*- coding:utf-8 -*-

import json,urllib2,sys

#compute location from command line arguments
"""
if len(sys.argv)<2:
    print "Usage: quickweather.py location"
    sys.exit()

location = ' '.join(sys.argv[1:])
"""


#Todo: download the JSON data from openweathemap.org's API
url = r'http://example.webscraping.com/ajax/search.json?page=1&page_size=10&search_term=a'
res = urllib2.urlopen(url)

hjson = json.loads(res.read())

for (key, value) in hjson.items():
    print key
    print value

print hjson['records'][1]['pretty_link']


#Todo:load JSON data into a Python variables

