#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:54:23 2022

@author: clinux01
"""
import matplotlib.pyplot as plt
import random

def dar_pasito (x, y, v_x, v_y, dt): 
    x_2 = x + v_x * dt
    y_2 = y + v_y * dt
    return (x_2, y_2)

def rebotar_der(x, v_x, x_max):
    mod_v = 0
    dist = x - x_max
    if x > x_max:
        x = x - (2*dist)
        v_x = - v_x
        mod_v = abs(v_x)
    return x, v_x, mod_v

def rebotar_izq(x, v_x, x_min):
    mod_v = 0
    dist = x_min - x
    if x < x_min:
        x = x + (2*dist)
        v_x = - v_x
        mod_v = abs(v_x)
    return x, v_x, mod_v

def rebotar_arr(y, v_y, y_max):
    mod_v = 0
    dist = y - y_max
    if y > y_max:
        y = y - (2*dist)
        v_y = - v_y
        mod_v = abs(v_y)
    return y, v_y, mod_v

def rebotar_aba(y, v_y, y_min):
    mod_v = 0
    dist = y - y_min
    if y < y_min:
        y = y - (2*dist)
        v_y = - v_y
        mod_v = abs(v_y)
    return y, v_y, mod_v

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

def cond_ini(L,v_max,n_part):
    xx=[]
    yy=[]
    vv_x=[]
    vv_y=[]
    for j in range (n_part):
        xx.append(random.random()*2-1*L)
        yy.append(random.random()*2-1*L)
        vv_x.append(random.random()*2-1*v_max)
        vv_y.append(random.random()*2-1*v_max)
    return xx,yy,vv_x,vv_y

def acumular_vel (vel_acum, mod_v):
    vel_acum = vel_acum + mod_v
    return vel_acum

def calcular_presion(n_pasos, vel_acum):
    presion = vel_acum/(n_pasos*dt*4*L)
    return presion


L=5 #a modo de ejemplo.
V_max=2 #a modo de ejemplo.
n_part =10 #a modo de ejemplo
dt=0.1
n_pasos=100000
vel_acum = 0
archivo=open("trayectorias.txt", "w")
print(n_part, file=archivo) # la primera linea es el numero de particulas
print( " ", file=archivo) # una linea vacia
lista_presion =[]

x_min = -L
x_max = L
y_min = -L
y_max = L

x,y,v_x,v_y=cond_ini(L,V_max,n_part) # la funcion que hicieron

for i in range(1, n_pasos):
    for j in range(n_part):
        x[j],y[j] = dar_pasito(x[j],y[j],v_x[j],v_y[j], dt)# aca hay que actualizar la posicion de la j-esima particula
        x[j],v_x[j], mod_v = rebotar_der(x[j],v_x[j], x_max) #corrijo x y v_x, por si me escape
        vel_acum = acumular_vel(vel_acum, mod_v)
        x[j],v_x[j], mod_v = rebotar_izq(x[j],v_x[j], x_min) #corrijo x y v_x, por si me escape
        vel_acum = acumular_vel(vel_acum, mod_v)
        y[j], v_y[j], mod_v = rebotar_arr(y[j],v_y[j], y_max)
        vel_acum = acumular_vel(vel_acum, mod_v)
        y[j], v_y[j], mod_v = rebotar_aba(y[j],v_y[j], y_min)
        vel_acum = acumular_vel(vel_acum, mod_v)
        print(j, x[j], y[j], file=archivo) # # escribimos en el archivo
    lista_presion.append(calcular_presion(i, vel_acum))   

plt.plot(lista_presion)

"""
plt.plot(trayectoria_x,trayectoria_y,'o')
plt.vlines(x=[-L,L],ymin=[-L,-L],ymax=[L,L], color="y") #bordes de la caja
plt.hlines(y=[-L,L],xmin=[-L,-L],xmax=[L,L], color="y") #bordes de la caja
B=2*L #Valor para armar el borde del grafico
plt.axis([-B,B,-B,B]) # definimos bordes del grafico
plt.grid() # ponemos una grilla ponemos una grilla
"""
archivo.close()