# encoding 'utf-8'
import copy
from copy import deepcopy

origin_map = {'1':1,'num':[1,2,3]}
map1 = origin_map
map2 = origin_map.copy()

#map2['num'] = origin_map['num'].copy()#可以针对子元素执行copy方法
#map2 = deepcopy(origin_map)#使用deepcopy方法得到的map2 是全部深拷贝的
#map2 = copy.deepcopy(origin_map) #使用deepcopy方法得到的map2 是全部深拷贝的
print('----')
print(origin_map)
print(map1)
print(map2)
origin_map['1'] = 2
origin_map['num'].remove(1)
print('----')
print(origin_map)
print(map1)
print(str(map2))

'''
考察dict的浅拷贝，深拷贝
A：map1 = origin_map 这是浅拷贝，指向的还是同一个
B: map2 =  origin_map.copy 也是浅拷贝，与A不同的是：深拷贝父对象（一级），子对象（二级）是浅拷贝
例如：
origin_map = {'1':1,'num':[1,2,3]}
map1 = origin_map
map2 = map.copy

origin_map['1'] = 2
origin_map['num'].remove(1)#移除list的第一位

map1 变为：
{'1':2,'num':[2,3]}
map2 变为：
{'1':1,'num':[2,3]}

与java 的 clone 和 直接赋值 还是有些相似的
'''
