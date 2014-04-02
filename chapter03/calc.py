#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-02 22:57:01
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-02 23:03:51
# 可变参数

# def calc(numbers):
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# nums = [1, 2, 3]
# calc(*nums)