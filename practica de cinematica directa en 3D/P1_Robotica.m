# Cinemática de un brazo robot 
# Angulos en grados

function [] = P1_Robotica()

q1 = input("Introduzca el primer angulo");
l2 = input ("Introduzca la longitud 2");
q3 = input("Introduzca el tercer angulo");
q4 = input("Introduzca el cuarto angulo");

# Convertir angulos a radianes

q1= q1*pi/180;
q3= q3*pi/180;
q4= q4*pi/180;

#Constantes
# Longitudes del robot 
l1 = 1; 
l3 = 1;
l4 = 1;

#Definición longitud de D
d1 = l1;
d2 = l2;
d3 = 0;
d4 = 0;

#Definción tita
o1 = q1;
o2 = 0;
o3 = q3;
o4 = q4;

#Definir longitud a
a1 = 0;
a2 = 0;
a3 = l3;
a4 = l4;

#Definir alpha
al1 = 0;
al2 = pi/2;
al3 = -(pi/2);
al4 = 0;

#Transformadas homogeneas entre los tres sistemas de referencia
A01 = D_H(o1, al1, a1, d1); 
A12 = D_H(o2, al2, a2, d2);
A23 = D_H(o3, al3, a3, d3);
A34 = D_H(o4, al4, a4, d4);

#Homogenea completa
T = A01*A12*A23*A34;

# Coordenadas de los origenes de los sistemas de refencia
P00 = [0 0 0 1]';
P01 = A01*[0 0 0 1]';
P02 = A01*A12*[0 0 0 1]'
P03 = A01*A12*A23*[0 0 0 1]';
P04 = A01*A12*A23*A34*[0 0 0 1]';

x = [0 P01(1) P02(1) P03(1) P04(1)];
y = [0 P01(2) P02(2) P03(2) P04(2)];
z = [0 P01(3) P02(3) P03(3) P04(3)];


subplot(1,3,1);
plot(x,y,"-o","linewidth",4);
xlabel(' X ')
ylabel(' Y ')

subplot(1,3,2);
plot(x,z,"r-+","linewidth",4);
xlabel(' X ')
ylabel(' Y ')

subplot(1,3,3);
plot(y,z,"k-*","linewidth",4);
ylabel(' Y ')
zlabel(' Z ')
title(' Brazo robotico con 4 grados de libertad ')

#subplot(1,4,4)
#figure(1)
#plot3(x,y,z,"k-*","linewidth",4);







