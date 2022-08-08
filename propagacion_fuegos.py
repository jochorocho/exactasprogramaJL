#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import statistics
import numpy as np
import matplotlib.pyplot as plt


def suceso_aleatorio(p):
    resultado = False
    if random.random() < p:
        resultado = True
    return resultado


def generar_bosque_vacio(n):
    bosque = []
    for i in range (0, n, 1):
        bosque.append(0)
    return bosque


def generar_brotes(bosque, p):
    for i in range (0, len(bosque), 1):
        if suceso_aleatorio(p):
            bosque[i] = 1
    return bosque


def count_tipo(bosque, tipo_celda): #cuenta la cantidad de celdas en el tipo de celda deseado
    count = 0    
    for i in range (0, len(bosque)):
        if bosque[i] == tipo_celda:
            count = count + 1
    return count


def generar_rayos(bosque, f):
     for i in range (0, len(bosque), 1):
         if suceso_aleatorio(f):
             bosque[i] = bosque[i] * -1
     return bosque
 
def propagacion(bosque):
    for i in range (0, len(bosque)-1, 1): #tengo que poner el len-1 porque si no se pasa del list range. ADemas no me hace falta chequear el ultimo puesto porque no propaga
        if bosque[i] == -1 and bosque[i+1] == 1:
                bosque[i+1] = -1
                i = i + 1
    for j in range (len(bosque)-1, 0, -1):
        if bosque[j] == -1 and bosque[j-1] == 1:
            bosque[j-1] = -1
            j = j - 1
    return bosque

def limpieza(bosque):
    for i in range (0, len(bosque), 1):
        if bosque[i] == -1:
            bosque[i] = 0
    return bosque
                          
                          
#n = numero de celdas, a = años de repeticion, p = probabilidad de brotes, f = probabilidad de fuego
def dinamica(n, a, p, f):
    count_list = []
    bosque = generar_bosque_vacio(n)
    for t in range (1, a, 1):
        count_tipo(bosque, 1)
        generar_brotes(bosque, p)
        generar_rayos(bosque, f)
        propagacion(bosque)
        limpieza(bosque)
        count_list.append(count_tipo(bosque, 1))
    return statistics.mean(count_list)



def graficar_dinamicas(intervalo_p, n, a, f):
    x_axis = np.arange(0, 1, intervalo_p)
    y_axis = []
    for i in range (len(x_axis)):
        valor_y = dinamica(n, a, x_axis[i], f)
        y_axis.append(valor_y)
    plt.plot(x_axis, y_axis)
    

#intervalo de p, numero de celdas, años de repeticion, probabilidad de fuego
print(graficar_dinamicas(0.02, 100, 500, 0.5))




"""
b_1 = [1, 1, 1, -1, 0, 0, 0, -1, 1, 0]
print(propagacion(b_1))

b_2 = [-1, 1, 1, -1, 1, 1, 0, 0, -1, 1]
print(propagacion(b_2))

b_3 = [-1, 1, 0, 1, 0, -1, 1, 0, 0, 1, -1]
print(propagacion(b_3))


 
bosque_t0 = generar_bosque_vacio(10)
print(bosque_t0)
bosque_t1 = generar_brotes(bosque, 0.6)
print(bosque_t1)
bosque_t2 = generar_rayos(bosque_t1, 0.2)
print(bosque_t2)
bosque_t3 = propagacion(bosque_t2)
print(bosque_t3)
"""
