#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:17:39 2022

@author: clinux01
"""

import random

cant_jugadores = 1
cant_turnos = 1

def tirar_dado():
    resultado = random.randint(1,6)
    return resultado

def tirar_varias_veces(nturnos):
    numero_turno = 0
    lis = []
    for numero_turno in range (0,nturnos,1):
        numero_turno = numero_turno + 1 
        lis.append(tirar_dado())
    return lis
##empieza en 0, pero como numero_turno suma antes que el append, se completan sólo 8 turnos.


def a_ver_si_gano (lis):
    i = 0
    worl = False
    while i < len(lis):
        if lis[i] != 6:
            i = i + 1
        else:
            worl = True
    return worl
"""
def jugar_varios(k):
    count_w= []
    for i in range (0,k,1):
       w_or_l = a_ver_si_gano(tirar_varias_veces(cant_turnos))
       if w_or_l == True:
           count_w.append(1)
       else:
           count_w.append(0)
    return count_w
"""
def jugar_varios(k):
    count_w= 0
    for i in range (0,k,1):
       w_or_l = a_ver_si_gano(tirar_varias_veces(cant_turnos))
       if w_or_l == True:
           count_w = count_w + 1
    return count_w
      
def winrate (k,w):
    wrate = w/k*100
    return wrate
    
print(winrate(cant_jugadores, jugar_varios(cant_jugadores)))