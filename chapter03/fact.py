#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: forecho
# @Date:   2014-04-02 23:20:24
# @Email:  caizhenghai@gmail.com
# @Last modified by:   forecho
# @Last modified time: 2014-04-02 23:28:10
# 递归函数

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)


def fact(n):
    return fact_iter(1, 1, n)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)


