#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-03 21:00:48
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-03 21:08:03
# 生成器 generator

# 只要把一个列表生成式的[]改成()，就创建了一个 generator
g = (x * x for x in range(10))
print g

# 如果要一个一个打印出来，可以通过generator的next()方法：
# print g.next()
# print g.next()
# print g.next()
# print g.next()

# 正确的方法是使用for循环
for n in g:
	print n