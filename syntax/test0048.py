# encoding 'utf-8'
import os
import urllib

import requests
from bs4 import BeautifulSoup
confusion = {}
print(confusion)

confusion[1] = 1
print(confusion[1])
print(confusion)
#print(confusion['1']) #KeyError: '1'
confusion['1'] = 2
print(confusion['1'])
print(confusion)
confusion[1.0] = 4
print(confusion[1.0])
print(confusion)

sum = 0
print(confusion)
for  k in confusion:
    sum += confusion[k]
    print(sum)

'''
    小括号：元组
    中括号：list
    大括号：字典
'''

'''
如果keyA和keyB是哈希等价键，那么它们将被视为完全相同的两个键，于是d[keyA]和d[keyB]会指向同一个字典元素。

例如，1和1.0就满足上述两个条件，因此是哈希等价键
'''

'''
{}
1
{1: 1}
2
{1: 1, '1': 2}
4
{1: 4, '1': 2}
{1: 4, '1': 2}
4
6
'''