#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 20:06:42 2022

@author: clinux01
"""
import numpy as np


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

def vecinos_de(tablero, coord):
    f = coord[0]
    c = coord[1]
    lista_vecinos = []
    for i in range(-1, 2, 2): #chequea -1 y 1. El stop tiene que ser 2 porque el ultimo paso no lo incluye
        if not es_borde(tablero, (f, c+i)):
            lista_vecinos.append((f, c+i))
        if not es_borde(tablero, (f+i, c)):
            lista_vecinos.append((f+i, c))            
    return lista_vecinos

def desbordar_posicion(tablero, coord):
    lista_vecinos = vecinos_de(tablero, coord)
    if tablero[coord] > 3:
        for i in range (0, len(vecinos_de(tablero, coord)), 1):
            tablero[lista_vecinos[i]] = tablero[lista_vecinos[i]] + 1
        tablero[coord] = 0
    return tablero

def desbordar_valle(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range (1, cantidad_filas, 1):
        for j in range (1, cantidad_columnas, 1):
            desbordar_posicion(tablero, (tablero[i, j]))
    return tablero

        
t1 = crear_tablero(7)
tirar_copo(t1, (2, 3))
tirar_copo(t1, (2, 3))
tirar_copo(t1, (2, 3))
tirar_copo(t1, (2, 3))
tirar_copo(t1, (4, 7))
tirar_copo(t1, (4, 7))
tirar_copo(t1, (4, 7))
tirar_copo(t1, (4, 7))
desbordar_valle(t1)
print(t1)
