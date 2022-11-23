import time
import py_grafica
import cy_grafica
import random

a=random.randint(-50000,50000)
b=random.randint(-50000,50000)
c=random.randint(-50000,50000)
d=random.randint(-50000,50000)
e=random.randint(-50000,50000)


init_time=time.time()
planPy=py_grafica.Diagonal()
planPy.Sx = a
planPy.Sy = b
planPy.r = c
planPy.x = d
planPy.y = e

planCy=cy_grafica.Diagonal()
planCy.Sx = a
planCy.Sy = b
planCy.r = c
planCy.x = d
planCy.y = e

time_spam = 400
n_steps=2000000

formato_datos = "{:.5f},{:5f}\n"
for i in range(30):
	iniciopy = time.time()
	py_grafica.step_time(planPy, time_spam, n_steps)
	finalpy=time.time() - iniciopy
	
	iniciocy = time.time()
	cy_grafica.step_time(planCy, time_spam, n_steps)
	finalcy=time.time() - iniciocy
		
	with open("Grafica.csv","a") as archivo:
		archivo.write(formato_datos.format(finalpy,finalcy))
	
	
	
