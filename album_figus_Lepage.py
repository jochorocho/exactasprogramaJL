#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:34:26 2022

@author: clinux01
"""
"""
- Album vacio (6)
- Comprar figurita (sorteo entre 6)
- CHequear si ya tengo la figurita
-Comprar hasta que se complete el album

"""
import random
import statistics

def crear_album (n_figus):
    album = []
    i = 0
    while i < n_figus:
        album = album + [0]
        i = i+1
    return album



def hay_alguno(lista, elem):
    i = 0
    hay_alguno = False
    while i < len(lista) and hay_alguno == False:
        i = i + 1
        if lista[i] == elem:
            hay_alguno = True
    return hay_alguno
            


def comprar_una_figu(figus_total):
    return random.randint(0, figus_total)
    

def chequear_album(album):
    i = 0
    hay_cero = False
    while i < len(album) and not hay_cero:#cuando compruebo que está incompleto dejo de chequear. Si ya llegué al final de la lista también.
        if album[i] == 0:
            hay_cero = True
        i = i + 1
    return hay_cero        
        
        
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    count_figus = 0
    while chequear_album(album):
        figu_nueva = comprar_una_figu(figus_total)
        album[figu_nueva-1] = figu_nueva
        count_figus = count_figus + 1
    return count_figus
        

def experimento(figus_total, n_rep):
    resultados = []
    for i in range (0, n_rep, 1):
        resultados.append(cuantas_figus(figus_total))
    return resultados
        
"""def promedio_experimentos(figus_total,n_rep):
    suma = 0
    lista = experimento(figus_total,n_rep)
    for i in range (0, len(lista), 1):
        suma = suma + lista[i]
        i = i+1
    statistics.mean(suma)"""

def promedio_experimentos(figus_total,n_rep):
    promedio = statistics.mean(experimento(figus_total,n_rep))
    return promedio

print(promedio_experimentos(6,200))