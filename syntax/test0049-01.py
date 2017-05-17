# encoding 'utf-8'
import os
import urllib

import requests
from bs4 import BeautifulSoup


def print_header(str):
    print('+++%s+++' % str)

print_header.category = 1
print_header.text = 'some info'
print_header('%d%s' % (print_header.category, print_header.text))
print_header('%d%s' % (print_header.category, print_header.text))

'''
涉及到几个知识点
1.字符串的格式化
格式化操作符
字符串模板
内建函数format

2.函数的定义，传参

3.函数的局部变量？
方法名.变量 = 值
method.Variable = value ？
自省，反射
'''