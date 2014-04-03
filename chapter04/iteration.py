#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-03 20:21:15
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-03 20:33:32
# 迭代

d = {'a': 1, 'b': 2, 'c': 3}

# 默认情况下，dict迭代的是key。
for key in d:
	print key


# 迭代value
for value in d.itervalues():
	print value

# 同时迭代key和value
for k, v in d.iteritems():
	print k, v

# 判断一个对象是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable) # str可迭代
print isinstance([1,2,3], Iterable) # list可迭代
print isinstance(123, Iterable) # 整数不可迭代

# 把一个list变成索引-元素
for i, value in enumerate(['A', 'B', 'C']):
	print i, value

# 同时引用了两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y