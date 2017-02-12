# -*- coding:utf-8 -*-

import PyPDF2

pdfFile = open('xf.pdf')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pageobj = pdfReader.getPage(5)
print pageobj.extractText()
