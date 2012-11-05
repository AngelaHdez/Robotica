# Cinemática de un brazo robot 
# Angulos en grados

function [] = CD2(q1,q2)

#Constantes
# Longitudes del robot 
l1 = 1; 
l2 = 1;

#Definición longitud de D
d1 = 0;
d2 = 0;
  
#Definción tita
o1 = q1;
o2 = q2;

#Definir longitud a
a1 = 0;
a2 = 0;

#Definir alpha
al1 = 0;
al2 = 0;

#Transformadas homogeneas entre los tres sistemas de referencia
A01 = D_H(o1, al1, a1, d1); 
A12 = D_H(o2, al2, a2, d2);

#Homogenea completa
T = A01*A12;

# Coordenadas de los origenes de los sistemas de refencia
P00 = [0 0 0 1]';
P01 = A01*[0 0 0 1]';
P02 = A01*A12*[0 0 0 1]';

x = [P00(1) P01(1) P02(1)];
printf('X es : %4.3f \n', x);
y = [P00(2) P01(2) P02(2)];
printf('Y es : %4.3f \n', y);

