#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:54:23 2022

@author: clinux01
"""
import matplotlib.pyplot as plt

def dar_pasito (x, y, v_x, v_y, dt):
    
    x_2 = x + v_x * dt
    y_2 = y + v_y * dt
    return (x_2, y_2)

def dar_pasos (x, y, v_x, v_y, dt, n_pasos):
    trayectoria_x = [x]
    trayectoria_y = [y]
    for i in range (0, n_pasos, 1):
        pos = dar_pasito(x, y, v_x, v_y, dt)
        x = pos[0]
        y = pos[1]
        trayectoria_x.append(x)
        trayectoria_y.append(y)
    return 
        

def rebotar_der(x, v_x, x_max):
    if x > x_max:
        dist = x_max-x
        x = x - 2 * dist
    return x


        
# dar_pasos(x, y, v_x, v_y, dt, n_pasos)

x = 0.25 # posicion inicial X
y = -3.5 # posicion inicial Y
v_x = 15 # velocidad inicial en x
v_y = 22 # velocidad inicial en y
dt = 0.1 #tamaño del paso temporal
n_pasos = 4
x_max = 5
trayectoria_x = [x]
trayectoria_y = [y]


nombre_archivo='trayectoria'
archivo=open(nombre_archivo + ".txt","w")
print(1, file=archivo) # escribimos la cant. de particulas (1)
print(' ',file=archivo) # escribimos una linea vacia
print(1,x, y, file=archivo) # escribimos las coordenadas de la posicion inicial
3
for i in range(n_pasos):
    x,y = dar_pasito(x, y, v_x, v_y, dt)
    rebotar_der(x, v_x, x_max)
    print(1,x, y, file=archivo) # escribimos las coordenadas de la posicion nueva
    trayectoria_x.append(x) # guardamos la coordenada siguiente en x
    trayectoria_y.append(y) # guardamos la coordenada siguiente en y
    

#ahora vamos a graficar la caja
L=5 # caja [-L, L]x[-L,L]
plt.plot(trayectoria_x,trayectoria_y,'o')
plt.vlines(x=[-L,L],ymin=[-L,-L],ymax=[L,L], color="y") #bordes de la caja
plt.hlines(y=[-L,L],xmin=[-L,-L],xmax=[L,L], color="y") #bordes de la caja
B=2*L #Valor para armar el bode del grafico
plt.axis([-B,B,-B,B]) # definimos bordes del grafico
plt.grid() # ponemos una grilla


    
archivo.close()