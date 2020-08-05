# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:10:10 2020

@author: Александр
"""


"""Напишите функцию на языке “Python”.

реализующую нахождение длины вектора 
произвольной размерности.
"""

def len_vect(x):
    """ x is a list!"""
    return abs((sum([elem ** 2 for elem in x])) ** 0.5) 
