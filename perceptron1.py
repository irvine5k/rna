#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:46:19 2019

@author: irvine
"""

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        s += e[i] * p[i]
    return s

s = soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

r = stepFunction(s)

