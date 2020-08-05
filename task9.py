# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 07:58:28 2020

@author: Александр
"""


"""Напишите функцию на языке “Python”,

без использования стандартных библиотек,
нахождения определителя матрицы любой размерности.
"""


def make_any_matr(n_rows, n_cols, fnc):
    return [[fnc(el1, el2)  for el1 in range(n_rows)]  for el2 in range(n_cols)]



def fnc(el1, el2):
    return 1 if el1 == el2 else 0



print(make_any_matr(10, 10, fnc))
