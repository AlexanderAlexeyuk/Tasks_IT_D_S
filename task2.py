# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:59:08 2020

@author: Александр
"""


"""Напишите функцию на языке “Python”.

реализующую скалярное произведение двух 
векторов произвольной размерности.
"""


def scal_mult(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))