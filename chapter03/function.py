#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-02 21:31:54
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-02 23:33:11
def my_abs(x):
	if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
x = int(raw_input())
print type(x)
print x
print my_abs(x)