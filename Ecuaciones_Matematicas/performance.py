import time
import py_Matematica
import cy_Matematica
import random

a=random.randint(-50000,50000)
b=random.randint(-50000,50000)
c=random.randint(-50000,50000)
d=random.randint(-50000,50000)
e=random.randint(-50000,50000)


init_time=time.time()
planPy=py_Matematica.Ecuaciones()
planPy.a = a
planPy.b = b
planPy.c = c
planPy.d = d
planPy.e = e

planCy=cy_Matematica.Ecuaciones()
planCy.a = a
planCy.b = b
planCy.c = c
planCy.d = d
planCy.e = e

time_spam = 400
n_steps=2000000

formato_datos = "{:.5f},{:5f}\n"
for i in range(30):
	iniciopy = time.time()
	py_Matematica.step_time(planPy, time_spam, n_steps)
	finalpy=time.time() - iniciopy
	
	iniciocy = time.time()
	cy_Matematica.step_time(planCy, time_spam, n_steps)
	finalcy=time.time() - iniciocy
		
	with open("Ecuaciones.csv","a") as archivo:
		archivo.write(formato_datos.format(finalpy,finalcy))
	
	
	
