# encoding 'utf-8'


origin_map = {'1': 1, '2': 2}
map1 = origin_map.copy()
print('----')
print(origin_map)
print(map1)
map1['1'] = 2
print('----')
print(origin_map)
print(map1)

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
{'1':2,'num':[1,2,3]}
map2 变为：
{'1':2,'num':[2,3]}

与java 的 clone 和 直接赋值 还是有些相似的
'''
