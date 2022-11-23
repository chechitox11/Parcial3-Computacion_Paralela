#cython: language level=3
cimport cython
"""
Fecha: 2 Nov 2022
Autor: Sergio Cortes
prgrama de cython para el calculo de la orbita

"""

cdef extern from "math.h":
	double sqrt(double x) nogil
	
cdef class Diagonal(object):

		cdef public double Sx,Sy,r,x,y
	
		cdef _init_(self):
			self.Sx=0.0
			self.Sy=0.0
			
			self.r=0.0
			
			self.x=0.0
			self.y=0.0


@cython.cdivision(True)
cdef void single_step(Diagonal f) nogil:
		cdef double b,a
		
		b= f.r + (f.Sy/f.Sx)
		a= f.y-b*f.x
		
		

def step_time(Diagonal f,float time_span,int n_steps):
		cdef int j
		dt=time_span/n_steps

		with nogil:
			for j in range(n_steps):
				single_step(f)
