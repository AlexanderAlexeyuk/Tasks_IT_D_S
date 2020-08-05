# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:33:49 2020

@author: Александр
"""


"""Игральную кость бросили N раз. 

Какова вероятность того, что M раз выпадет число не менее S.
Напишите функцию на языке “Python” решения данной задачи,
для любых N, M и S.
"""



def prob_bone(N, M, S):
    factorial_N = 1
    factorial_M = 1
    factorilal_N_M = 1
    for i in range(2, N + 1):
        factorial_N *= i
    for el in range(2, M + 1):
        factorial_M *= el
    for elems in range(2, (N - M) + 1):
        factorilal_N_M *= elems
    dg = N - M
    return (factorial_N / (factorial_M * factorilal_N_M)) \
            * (( (6 - S) / S) ** M) * ((1 - (6 - S) / S)) ** dg

            

print(prob_bone(10, 2, 5))
            
            
            

            


    
    

    
    