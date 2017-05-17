# encoding 'utf-8'
import os
import urllib

import requests
from bs4 import BeautifulSoup

names1 = ['a', 'b', 'c', 'd']
names2 = names1
names3 = names1[:]
names2[0] = 'hh'
print(names1)
names3[1] = 'ww'
print(names1)
sum = 0

for ls in (names1, names2, names3):
    if ls[0] == 'hh':
        sum += 1
    if ls[1] == 'ww':
        sum += 10
    print(sum)

'''考察的应该是深拷贝 浅拷贝'''