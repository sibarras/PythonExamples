mode(-1);
/*
Programa realizado por Samuel Ibarra para presentar el resultado de la logica
para el control de trafico vehicular utilizado con el toolbox de scilab. El
archivo utilizado sera adjunto. Para que este programa funcione, se debe colcoar
la localizacion en donde esta guardado el archivo de logica difusa de extension fls.

El archivo de logica difusa puede ser abierto mediante el editor de logica difusa
que puede ser abierto mediante el comando:
>>> sciFLTEditor()
Dentro de este editor se busca el archivo y se podran sobservar los conjuntos difusos,
las entradas y las salidas utilizadas. El archivo sera adjunto junto a este.
*/
fls=loadfls("C:\Users\Samuel\Desktop\controlador_de_trafico.fls");
nx1=30;
nx2=30;
x1=linspace(0,30,nx1)';
x2=linspace(0,30,nx2)';
X=genspace(x1,x2);
Y=evalfls(X,fls);
Y=matrix(Y,nx2,nx1)';
scf();clf();
plot3d(x1,x2,Y);
