
from math import sqrt

class Ecuaciones(object):
	def _init_(self):
		self.a=0.0
		self.b=0.0
			
		self.c=0.0
			
		self.d=0.0
		self.e=0.0


def single_step(f):

		suma=f.a+f.b+f.c+f.d+f.e
		resta= suma - (f.b+f.c+f.e)
		multiplicacion=suma*resta+(f.a+f.b)-(f.d+f.e)
		division=(multiplicacion/suma)+(resta/suma)*(resta/multiplicacion)
		raizes=suma**(1/2)+multiplicacion**(1/4)
		exponente=(f.a**10+division**(1/3))

def step_time(f,time_span,n_steps):
	dt=time_span/n_steps
	for j in range(n_steps):
		single_step(f)
