# -*- coding:utf-8 -*-

import urllib2,sys,bs4,os

url = "http://xkcd.com"

if not (os.path.isdir(r'.\xkcd')):
    print "Creat dir"
    os.makedirs("xkcd")

while not url.endswith("#"):


#TODO:download the page
    print "Download the page "
    res = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(res.read(),'html.parser')

#TODO:find the url of the comic image
    comicElem = soup.select("#comic img")
    if len(comicElem) == 0:
        print "Could not find image"
    else:
        comicurl = "http:"+comicElem[0].get('src')

    try:
        print "download: " + comicurl
        response = urllib2.urlopen(comicurl)
    except urllib2.URLError, e:
        print e.reason


#TODO:save the image
    imagefile = open(os.path.join("xkcd",os.path.basename(comicurl)),'wb')
    for line in response.readlines():
        imagefile.write(line)
    imagefile.close()

#TODO:get the prev button's url
    preLink = soup.select('a[rel="prev"] ')[0]
    url = "http://xkcd.com" + preLink.get('href')
print "Done"