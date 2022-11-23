

#Fichero para la creacion del objeto compartido

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("cy_grafica.pyx"))

setup(ext_modules = exts)
