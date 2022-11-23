
from math import sqrt

class Diagonal(object):
	def _init_(self):
		self.Sx=0.0
		self.Sy=0.0
		self.r=0.0
		self.x=0.0
		self.y=0.0


def single_step(f):

		b= f.r + (f.Sy/f.Sx)
		a= f.y-b*f.x

def step_time(f,time_span,n_steps):
	dt=time_span/n_steps
	for j in range(n_steps):
		single_step(f)
