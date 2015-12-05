#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
    Python cookbook chapter 1.20
    Date: 2015-12-05
'''

from collections import ChainMap
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

c = ChainMap(a,b)
print([c[k] for k in ('x','y','z')])
print(list(c.keys()))
print(list(c.values()))
print(c)
# 如果有重复的键，那么会采用第一个映射中的值
print("c['z']={}".format(c['z']))

# 修改映射的操作总是会作用在第一个映射结构上
c['z'] = 10
c['w'] = 20
print(c)
print(a)
# 因此，以下是错误的，因为第一个映射中没有'y'键
#del c['y']

# 修改第一个映射，同时也会影响到ChainMap
del a['x']
print(c)

# ChainMap与带有作用域的值，比如程序中的变量一起
# 工作时特别有用
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])

# 作为ChainMap的替代方案，我们可能会考虑使用字典的
# update()方法将多个字典合并在一起
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = dict(a)
merged.update(b)
print(merged)
# 合并后，原始字典的修改不会反应到合并的结果中来
a['w'] = 20
print(a)
print(merged)