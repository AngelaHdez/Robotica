function D_H = D_H(tita ,al,a ,d)
D_H = [cos(tita) -cos(al)*sin(tita) sin(al)*cos(tita)  a*cos(tita);
       sin(tita) cos(al)*cos(tita) -sin(al)*cos(tita) a*sin(tita);
       0 sin(al) cos(al) d;
       0 0 0 1];
