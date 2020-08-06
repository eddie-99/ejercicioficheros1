"""
    EJERCICIO 1:

Escribir una función que pida un número entero entre 1 y 10 y 
guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.

"""

from io import open
import pathlib
import shutil

def numero_entero():
    numero = int(input("Introduzca un numero: "))

    if numero < 1 and numero > 10:
        numero = int(input("Introduce un numero del 1 al 10: "))
    
    n = numero

    ruta = str(pathlib.Path().absolute()) + f"/tabla-{n}.txt"
    archivo = open(ruta, "w") # "w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
    archivo.write(f"**************** Tabla del {n} *****************\n")
    for elemento in range(1,11):
        resultado = n*elemento
        archivo.write(f"{n} X {elemento} = {resultado} \n")
    archivo.close()

    return(n)

numero_entero()
