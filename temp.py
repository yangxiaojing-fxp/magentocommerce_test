import re
import os

from selenium import webdriver
pattern = re.compile(r'^[0-9a-zA-Z_]+$')
str = 'a。'
print(type(pattern.search(str)))

str1 = '47530954_aaa'
print(pattern.search(str1),type(pattern.search(str1)))


x="《》"

print(re.search(r"^[^`~!@#%^&*()_+=|{}':;""<>'/?,]*$",x))

print(os.getcwd())
f=open(r"/setests/keyMouse/20201028.py",mode='r')

f.close()

