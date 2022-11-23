#cython: language level=3
cimport cython
"""
Fecha: 2 Nov 2022
Autor: Sergio Cortes
prgrama de cython para el calculo de la orbita

"""

cdef extern from "math.h":
	double sqrt(double x) nogil
	
cdef class Ecuaciones(object):

		cdef public double a,b,c,d,e
	
		cdef _init_(self):
			self.a=0.0
			self.b=0.0
			
			self.c=0.0
			
			self.d=0.0
			self.e=0.0


@cython.cdivision(True)
cdef void single_step(Ecuaciones f) nogil:
		cdef double suma,resta,division,raizes,exponente
		
		suma=f.a+f.b+f.c+f.d+f.e
		resta= suma - (f.b+f.c+f.e)
		multiplicacion=suma*resta+(f.a+f.b)-(f.d+f.e)
		division=(multiplicacion/suma)+(resta/suma)*(resta/multiplicacion)
		raizes=suma**(1/2)+multiplicacion**(1/4)
		exponente=(f.a**10+division**(1/3))
		
		

def step_time(Ecuaciones f,float time_span,int n_steps):
		cdef int j
		dt=time_span/n_steps

		with nogil:
			for j in range(n_steps):
				single_step(f)
