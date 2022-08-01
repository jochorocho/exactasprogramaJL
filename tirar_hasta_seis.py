#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:14:40 2022

@author: clinux01
"""

import random

def tirar_dado():
    resultado = random.randint(1,6)
    return resultado
	
def tirar_hasta_seis():
	lis = [0]
	i = 0
	while lis[i] != 6:
		lis.append(tirar_dado())
		i = i + 1
	return lis
"""
def tirar_hasta_seis():
    valores = []
    dado = random.randint(1,6)
    if dado ==6
        return valores
    else
   

def tirar_hasta_seis():
    valores =  []
    c = True
    while c == True:
        dado = random.randint(1,6)
        if dado == 6:
            c = False
        valores.append(dado)
    return valores
        
"""

def cuanto_suman(lis):
	i = 0
	suma = 0
	while i < len(lis) and suma <= 20:
		suma = suma + lis[i]
		i = i+1
	return suma
"""
def cuanto_suman(lista_dados):
    suma = 0
    for i in range (o, len(lista_dados),1):
        suma = suma + lista_dados[i]
    return suma
"""


def win_orlose (sum):
	win = False
	if sum == 20:
		win = True
	return win
		
		
def jugar_varios(k):
	wcount = 0
	for i in range (0, k, 1):
		if win_orlose(cuanto_suman(tirar_hasta_seis())) == True:
			wcount = wcount + 1	
	return wcount
	
	
cant_jugadores = 50000
print(str(jugar_varios(cant_jugadores)/cant_jugadores*100) + "%")