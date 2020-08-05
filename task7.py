# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 06:31:02 2020

@author: Александр
"""


"""Напишите программу на языке “Python”

нахождения количества N значных чисел делящихся на m.
Ограничение на время ее выполнения для 4-х значных чисел
не более 4 сек.
"""

from datetime import datetime



def amount_N_counter(N, K, m):
    lst = []
    for int_ in range(K + 1):
        if not int_ % m and  int_ // 10 ** \
            (N - 1) and not int_ // 10 ** N:
            lst.append(int_)
    return len(lst)
           
 
start_time = datetime.now()    
print(amount_N_counter(5, 100000, 5))
print(datetime.now() - start_time)