# Parcial3-Computacion_Paralela
Ejercicios de prueba cambiando de python a Cython

En el siguiente archivo reposan cinco ejemplos con los cuales mostraremos la efectividad de cython frente a python,
corriendo dos codigos de igual caracteristicas y comparando el tiempo de ejecucion de ambos.

Ejercicio 1: En este se toma como base las ecuaciones necesarias para encontrar la linea de minimos cuadrados (usando en estadistica) con estas ecuaciones se toman diversos datos tales como la "x" y la "y" en el plano, una r (una medida) y "Sx" junto a "Sy" que es la posicion en la diagonal dentro plano.

Ejercicio 2: Para probar definitivamente la mejora de rendimiento de cython, se toman todas las ecuaciones matematicas basicas (suma, resta, division raices y exponentes) realizando las operaciones con datos aparte (a,b,c,d,e) y con los resultados que se dan de las sumas, restas, multiplicaciones, etc.

Para ejecutar los programas en la terminal de ubuntu, se debe entrar desde la terminal hasta la carpeta donde reposan todos los codigos (tres .py, un .pyx y un Makefile) ejecutar parcialmente todos los archivos usando un "make all" para despues hacer la prubea y generar el .csv invocando al "perfomance" ingresando "phyton3 perfomance.py"
