function [] = Inversa()

#Meter parametros por pantalla
x = input("Introduzca x");
y = input("Introduzca y");
l1 = input("Introduzca l1");
l2 = input("Introduzca l2");

#Calculo de las titas

printf('La segunda tita es : %4.3f \n');
a = (x^2+y^2-l1^2+l2^2);
b= (2*l1*l2);
q2  = acos(a/b)

epsilon = atan(y/x);

c = l2*sin(q2);
d = l2*cos(q2);
e = c/d;
alpha = atan(e);

printf('La primera tita es : %4.3f \n');
q1 = epsilon - alpha


#Ver si está bien mediante la cinematica directa
 
 CD2(q1,q2)
 #Esta mal la cinematica directa
