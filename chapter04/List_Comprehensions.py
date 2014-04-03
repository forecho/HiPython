#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-03 20:43:15
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-03 20:58:25
# 列表生成式

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1,11):
	L.append(x * x)
print L
# 用列表生成式实现
print [x * x for x in range(1, 11)]
# 结果都是：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 写列表生成式时，把要生成的元素【x * x】放到前面，后面跟【for】循环，就可以把list创建出来
print [x * x for x in range(1, 11) if x % 2 == 0]
# 结果是：[4, 16, 36, 64, 100]


# 使用两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']
# 结果是：['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录


# 列表生成式使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]


# list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]