#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-03 20:00:40
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-03 20:17:52
# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 笨方法
print [L[0], L[1], L[2]]

# 循环
r = []
n = 3
for i in range(n):
	r.append(L[i])
print r

# 切片 从索引0开始取，直到索引3（即第3个）
print L[0:3]
print L[:3]

# 以上结果都是：['Michael', 'Sarah', 'Tracy']


# 倒数第1个元素 结果是：Jack
print L[-1]

# 倒数2个元素 结果是：['Bob', 'Jack']
print L[-2:]


L = range(100)
# 前10个数，每两个取一个
print L[:10:2]

# 所有数，每5个取一个
print L[::5]

# 切片操作tuple
print (0, 1, 2, 3, 4, 5)[:3]

# 操作字符串'xxx'或Unicode字符串u'xxx'
print 'ABCDEFG'[::2]
