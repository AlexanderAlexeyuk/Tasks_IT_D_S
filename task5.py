# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 07:40:59 2020

@author: Александр
"""


"""Напишите функцию на языке “Python”

нахождения определителя матрицы размерностью 4Х4.
"""


def make_matr(n_rows, n_cols):
    return [[el1  for el1 in range(n_rows)]  for el2 in range(n_cols)]


print(make_matr(4, 4))
