#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-02 23:04:41
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-03 20:41:00
# 关键字参数

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, city=kw['city'], job=kw['job'])
# or
kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, **kw)