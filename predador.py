#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:07:29 2022

@author: clinux01
"""
import numpy as np

def crear_tablero(fil, col):
    f = fil + 2
    c = col + 2
    t = np.repeat(" ", (f)*(c)) . reshape (f, c)
    for i in range  (0, f, 1):
        t[i, 0] = "M"
        t[i, c-1] = "M"
    for i in range ( 0, c, 1):
        t[0, i] = "M"
        t[f-1, i] = "M"
    return t
        
def poner_animales(t, fil, col, ani):
    for i in range (len(animal)):
        t[(fil[i], col[i])] = animal[i]
    return t

def vecinos_de (t, coord):
    desp = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    vecinos = []
    for i in range (len(desp)):
        coord_veci = desp[i] + coord #corrijo el desplazamiento sumandole la coordenada para que de las coordenadas del lugar
    return coord_veci

"""
        if t[coord_veci] != "M":
            vecinos.append(coord_veci)
    return vecinos
"""
def buscar_ady (t, coord, obj): #busca animal objetivo (obj) adyacente a la coordenada (coord) en un tablero (t)
    veci = vecinos_de(t, coord) #tira la lista de vecinos
    lo_encontre = False
    i = 0
    res = []
    while not lo_encontre and i<len(veci): #chequea hasta que termina la lista hasta que lo_encontre sea TRue
        if t[veci[i]] == obj: #chequea la lista de vecinos y se fija si son del tipo de objetivo, para añadirlos a la lista de resultado
            res.append(veci[i])
    return res

def fase_mover (t):
    fila, col = t.shape #tupla en la que 
    for i in range(1, fila-1):
        for j in range(1, col-1):
            if t[i, j] != " ":
                individuo = t[(i,j)]
                adyacentes = buscar_ady(t,(i,j), " ")
            if len(adyacentes) != 0:
                t[(i, j)] = " "
                t[adyacentes[0]] = individuo
    return t

def alimentacion (t): #CHEQUEAR
    fila, col = t.shape #tupla en la que 
    for i in range(1, fila-1):
        for j in range(1, col-1):
            if t[i, j] == "L":
                individuo = t[(i,j)]
                adyacentes = buscar_ady(t,(i,j), "A")
            if len(adyacentes) != 0:
                t[(i, j)] = " "
                t[adyacentes[0]] = individuo
    return t

def fase_reproducir(t):
    fila, col = t.shape #tupla en la que 
    for i in range(1, fila-1):
        for j in range(1, col-1):
            if t[i, j] != " ":
                individuo = t[(i,j)]
                adyacentes = buscar_ady(t,(i,j), individuo)
            if len(adyacentes) != 0:
                ady_vacio = buscar_ady(t, (i,j), " ")
                if len(ady_vacio != 0):
                    t[ady_vacio[0]] = individuo
    return t
# esta formula se puede repetir modificando levemente para hacer la fase alimentacion, solo que se busca un animal y el individuo se mueve a su lugar


t = crear_tablero(3,4)
filas = [1, 2, 2, 3, 1]
columnas = [3, 1, 3, 1, 1]
animal = ["A", "A", "A", "A", "L"]
print(vecinos_de(t, (1,2)))