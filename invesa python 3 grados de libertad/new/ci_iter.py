# -*- coding: utf-8 -*-
from math import *
import numpy as np
import pylab as pl


def matriz_T(theta,alpha,a,d):
        # calcula la matriz T
        
        f0=[cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), a*cos(theta)]
        f1=[sin(theta),cos(theta)*cos(alpha), -sin(alpha)*cos(theta), a*sin(theta)]
        f2=[0, sin(alpha), cos(alpha), d]
        f3=[0,0,0,1]
        
        T=[f0,f1,f2,f3]
        return T

def multiplica(matriz,vector_entrada):
        # multiplica una matriz 4x4 por un vector 4x1

        vector_salida=[]

        for i in range(4):
                suma=0
                for j in range (4):
                        suma+=matriz[i][j]*vector_entrada[j]
                vector_salida.append(suma)
        
        return vector_salida

def prod_esc(vector_1,vector_2):
        # calcula el producto escalar de dos vectores
        
        l=len(vector_1)
        suma=0
        for i in range(l):
            suma+=vector_1[i]*vector_2[i]
        return suma

def resta_vect(vector_1,vector_2):
        # calcula la resta de dos vectores
        
        l=len(vector_1)
        vector_salida=[]
        for i in range(l):
            vector_salida.append(vector_1[i]-vector_2[i])
        return vector_salida

def unitario_vect(vector):
        # calcula un vector unitario a partir de un vector cualquiera
        
        l=len(vector)
        norma=0
        for i in range(l):
            norma+=vector[i]*vector[i]
        norma=sqrt(norma)
        vector_salida=[]
        for i in range(l):
            vector_salida.append(vector[i]/norma)
        return vector_salida


def angulo_vect(vector):
        # calcula el ángulo de un vector
        x=vector[0]
        y=vector[1]
        if x>0:
            if y>=0:
                l=atan(y/x)
            if y<0:
                l=atan(y/x)
        if x<0:
            if y>0:
                l=pi+atan(y/x)
            if y<0:
                l=atan(y/x)-pi
        if x==0:
            if y>=0:
                l=pi/2
            if y<0:
                l=-pi/2
            if y==0:
                l='error'
        return l


def cin_dir(t1,t2,t3):
        #calcula la cinemática directa para un manipulador planar de dos articulaciones

        # Parámetros de contrucción
        a1=10
        d1=0
        alfa1=0

        a2=5
        d2=0
        alfa2=0
        
        a3=3
        d3=0
        alfa3=0
  
        # Variables 
        # tita1
        # tita2

        # calculo matrices transformación
        T01=matriz_T(t1,alfa1,a1,d1)
        T12=matriz_T(t2,alfa2,a2,d2)
        T23=matriz_T(t3,alfa3,a3,d3)
	      
        # origenes
        o00=[0,0,0,1]
        o11=[0,0,0,1]
        o22=[0,0,0,1]
        o33=[0,0,0,1]
        
        # calculo punto uno del robot
        o10=multiplica(T01,o11)

        # calculo punto dos del robot
        o21=multiplica(T12,o22)
        o20=multiplica(T01,o21)

       #calculo punto tres del robot
        o32=multiplica(T23,o33)
        o31=multiplica(T12,o32)
        o30=multiplica(T01,o31)

        p=[o00,o10,o20,o30]
        return p


#cálculo de la cinemática inversa de forma iterativa por el método CCD

# valores articulares arbitrarios para la cinemática directa inicial
tita1=0;
tita2=0;
tita3=0;
# introducción del punto para la cinemática inversa
x=input('coordenada x  ')
y=input('coordenada y  ')
r=[x,y]

k=1
cuenta=1 
while (k==1):

    # cálculo de la cinemática directa para el primer valor
    p=cin_dir(tita1,tita2,tita3)
    O0=[p[0][0],p[0][1]]
    O1=[p[1][0],p[1][1]]
    O2=[p[2][0],p[2][1]]
    O3=[p[3][0],p[3][1]]
    
    x0=[p[0][0], p[1][0], p[2][0], p[3][0]]
    y0=[p[0][1], p[1][1], p[2][1], p[3][1]]

    # primera corrección
    # determinación del módulo del ángulo
    v1=resta_vect(r,O2)
    v2=resta_vect(O3,O2)
    v1=unitario_vect(v1)
    v2=unitario_vect(v2)
    v=prod_esc(v1,v2)
    t=acos(v)

    # determinación del signo de la corrección
    c1=angulo_vect(v1)
    c2=angulo_vect(v2)
    if c1>c2:
        signo=1
    else:
        signo=-1

    # aplicación de la primera corrección
    tita3=tita3+signo*t
   


    # cálculo de la cinemática directa para el segundo valor
    p=cin_dir(tita1,tita2,tita3)
    O0=[p[0][0],p[0][1]]
    O1=[p[1][0],p[1][1]]
    O2=[p[2][0],p[2][1]]
    O3=[p[3][0],p[3][1]]
    
    x1=[p[0][0], p[1][0], p[2][0], p[3][0]]
    y1=[p[0][1], p[1][1], p[2][1], p[3][1]]

    # segunda corrección
    # determinación del módulo del ángulo
    v1=resta_vect(r,O1)
    v2=resta_vect(O3,O1)
    v1=unitario_vect(v1)
    v2=unitario_vect(v2)
    v=prod_esc(v1,v2)
    t=acos(v)

    # determinación del signo de la corrección
    c1=angulo_vect(v1)
    c2=angulo_vect(v2)
    if c1>c2:
        signo=1
    else:
        signo=-1

    # aplicación de la segunda corrección
    tita2=tita2+signo*t


    # cálculo de la cinemática directa para el segundo valor
    p=cin_dir(tita1,tita2,tita3)
    O0=[p[0][0],p[0][1]]
    O1=[p[1][0],p[1][1]]
    O2=[p[2][0],p[2][1]]
    O3=[p[3][0],p[3][1]]

    x2=[p[0][0], p[1][0], p[2][0], p[3][0]]
    y2=[p[0][1], p[1][1], p[2][1], p[3][1]]
     # tercera corrección
    # determinación del módulo del ángulo
    v1=resta_vect(r,O0)
    v2=resta_vect(O3,O0)
    v1=unitario_vect(v1)
    v2=unitario_vect(v2)
    v=prod_esc(v1,v2)
    t=acos(v)

    # determinación del signo de la corrección
    c1=angulo_vect(v1)
    c2=angulo_vect(v2)
    if c1>c2:
        signo=1
    else:
        signo=-1

    # aplicación de la segunda corrección
    tita1=tita1+signo*t
        # cálculo de la cinemática directa para el segundo valor
    p=cin_dir(tita1,tita2,tita3)
    O0=[p[0][0],p[0][1]]
    O1=[p[1][0],p[1][1]]
    O2=[p[2][0],p[2][1]]
    O3=[p[3][0],p[3][1]]

    
    x3=[p[0][0], p[1][0], p[2][0], p[3][0]]
    y3=[p[0][1], p[1][1], p[2][1], p[3][1]]


    # representación gráfica
    pl.figure(cuenta)
    pl.xlim(-15,15)
    pl.ylim(-15,15)
    pl.plot(x0,y0, 'k-o')
    pl.plot(x1, y1, 'r-o')
    pl.plot(x2, y2, 'g-o')
    pl.plot(x3, y3, 'b-o')
    pl.plot(x, y, '*')
    pl.show()

    
    
    
    k=input('distinto de 1 para salir  ')
    cuenta+=1

# valores articulares tras la última iteración
print tita1
print tita2
print tita3



