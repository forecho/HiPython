#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-02 23:12:32
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-03 20:39:11
# 参数组合

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

print func(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}

print func(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}

print func(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}

print func(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

args = (1, 2, 3, 4)
kw = {'x': 99}
print func(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}