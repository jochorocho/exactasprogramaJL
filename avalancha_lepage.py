#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 20:06:42 2022

@author: clinux01
"""
import numpy as np
import imageio
import os
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
    for i in range (1, cantidad_filas-1, 1):
        for j in range (1, cantidad_columnas-1, 1):
            desbordar_posicion(tablero, (i, j))
    return tablero

def hay_que_desbordar(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    hay_que = False
    for i in range (1, cantidad_filas-1, 1):
        for j in range (1, cantidad_columnas-1, 1):
            if tablero[(i,j)] >= 4:
                hay_que = True
                return hay_que
            
def estabilizar(tablero):
    while hay_que_desbordar(tablero) == True:
        desbordar_valle(tablero)
            
def paso(tablero):
    tirar_copo(tablero, (4,4))
    estabilizar(tablero)
    
def guardar_foto(t, paso):
    dir_name = "output"
    if not os.path.exists(dir_name): # me fijo si no existe el directorio
        os.mkdir(dir_name) #si no existe lo creo
       
    ax = plt.gca()
    file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
    plt.imshow(t, vmin=-1, vmax=3)
    ax.set_title("Copos tirados: {}".format(paso+1)) #titulo
    plt.savefig(file_name)

def hacer_video(cant_fotos):
    dir_name = "output"
    lista_fotos=[]
    for i in range (cant_fotos):
        file_name = os.path.join(dir_name, "out{:05}.png".format(i))
        lista_fotos.append(imageio.imread(file_name))


    video_name = os.path.join(dir_name, "avalancha.mp4")
    #genero el video con 10 Copos por segundo. Explorar otros valores:
    imageio.mimsave(video_name, lista_fotos, fps=10)
    print('Estamos trabajando en el directorio', os.getcwd())
    print('y se guardo el video:', video_name)

def probar(n, pasos):
    t = crear_tablero(n)
    for i in range(pasos):
        paso(t)
        guardar_foto(t, i)
    hacer_video(pasos)
    return t
        
probar(7, 200)
