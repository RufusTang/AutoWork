# coding=utf-8
'''
Created on 2016-8-16
@author: Jennifer
Project:使用chrome浏览器，安装chromewebdriver.exe
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://eip.chinatowercom.cn')
driver.find_element_by_id('username').send_keys(r'tanghan')
driver.find_element_by_id('password').send_keys(r'y880228')
driver.find_element_by_css_selector("html body div div div form div button.submit").click()

driver.get('http://mail.10086.cn')
driver.find_element_by_id('txtUser').send_keys(r'15825279415')
driver.find_element_by_id('txtPass').send_keys(r'y880228')
driver.find_element_by_css_selector("html body section div div div form fieldset ul li dl  dd div button#loginBtn").click()
