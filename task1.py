# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:04:15 2020

@author: Александр
"""

"""Напишите функцию на языке “Python”.

получающую на вход численные значения некоторой случайной
величины и вероятности их появления, а возвращающую –
ее математическое ожидание и дисперсию.
"""


def rand_value_info(x, p):
    return x * p, x ** 2 * p - (x * p) ** 2
