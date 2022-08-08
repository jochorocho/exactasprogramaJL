#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 20:06:42 2022

@author: clinux01
"""

import numpy as np
import matplotlib.pyplot as plt



def crear_tablero(n):
    m = n+2
    t = np.repeat(0,(m)*(m)).reshape(m,m)
    for i in range (0, m, 1):
        t[0, i] = -1
        t[m-1, i] = -1
        t[i, 0] = -1
        t[i, m-1] = -1
    return t

def es_borde(tablero, coord):
    borde = False
    if tablero[coord] == -1:
        borde = True
    return borde

    
def tirar_copo(tablero, coord):
    tablero[coord] = tablero[coord] + 1

t1 = crear_tablero(7)

#tirar_copo(t1,(1,7))

def vecinos_de(tablero, coord):
    f = coord[0]
    c = coord[1]
    lista_vecinos = []
    for i in range(-1, 2, 2): #chequea -1 y 1. Tiene que ser 2 porque el ultimo paso no lo incluye
        if not es_borde(tablero, (f, c+i)):
            lista_vecinos.append((f, c+i))
        if not es_borde(tablero, (f+i, c)):
            lista_vecinos.append((f+i, c))            
    return lista_vecinos



print(vecinos_de(t1,(4,7)))