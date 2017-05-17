# encoding 'utf-8'
import os
import urllib

import requests
from bs4 import BeautifulSoup

confusion = {}
print(confusion)

confusion[(1, 2, 4)] = 8
print(confusion)
confusion[(4, 2, 1)] = 10
print(confusion)
confusion[(1, 2)] = 12
print(confusion)
sum = 0
print((1, 2, 4).__hash__())  # hash:2528502973976161366
print((4, 2, 1).__hash__())  # hash:6312110366011971310
print(hash((4, 2, 1)))  # hash:6312110366011971310
for i in confusion:
    sum = sum + confusion[i]
    print(sum)

print(len(confusion))
print(confusion.__len__())
#print(hash(confusion))
#print(confusion.__hash__())
