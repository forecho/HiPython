#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-02 22:02:04
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-02 23:03:29
# 默认参数

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x = int(raw_input())
y = int(raw_input())

x, y = move(100, 100, 60, math.pi / 6)
print x, y
r = move(100, 100, 60, math.pi / 6)
print r