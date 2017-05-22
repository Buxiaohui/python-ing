# encoding 'utf-8'
import copy
from copy import deepcopy

origin_map = {'1':1,'2':2,'3':3}
new_map = {'1':20,"4":4}
print(origin_map)
print(new_map)
origin_map.update(new_map)

print('--update--')
print(origin_map)
print(new_map)


'''

'''
