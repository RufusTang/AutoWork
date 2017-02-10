# -*- coding:utf-8 -*-

import openpyxl


wb = openpyxl.load_workbook("test.xlsx")

sheetname = u"分摊比例"

print sheetname
sheet =wb.get_sheet_by_name(unicode(sheetname,'GBK').encode('UTF-8'))

data = {}

#Todo: Fill in data

for row in range(2,sheet.get_highest_row()+1):
    style = sheet['a'+str(row)].value
    code = sheet['b'+str(row)].value
    name = sheet.cell(row=row,column=3).value
    print style
    print name
    print code

#Todo: open a text file and write the contents of data