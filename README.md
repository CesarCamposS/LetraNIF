# LetraNIF
Este programa lo he creado para mi uso personal en el trabajo.

A veces necesito conocer la letra del NIF o NIE, pero en la documentación o no viene, o no se lee bien. 
Para ahorrarme entrar en alguna página web que me haga el cálculo, he hecho este script en python para hacer el cálculo de forma local en mi equipo. 

El programa detecta si es un NIF o un NIE comprobando el primer caracter. Si es un número, se trata de un NIF, si es X, Y o Z, es un NIE.

El archivo .exe, ejecutable en windows lo he hecho con pyinstaller.exe con los parámetros --onefile y --noconsole. 
