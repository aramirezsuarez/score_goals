# -*- coding: utf-8 -*-
"""Taller_guia_de_estilo_de_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GMyH2plZMH3vi_d6594iHrkMNWjen6ks

# Taller 13 Guía de estilo para escribir código en Python
En este taller aprenderá los conceptos **básicos** relativos a la guía de estilo para escribir código en Python [(PEP8)](https://peps.python.org/pep-0008/).

La guía de estilo busca mejorar la claridad y la legibilidad del código en Python, pero no afecta su ejecución.

# **Ejercicios**.

## 01.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

nRo1=float(input("Ingrese el primer número: "))


nRo2=float(input("Ingrese el segundo número: "))
s =  nRo1 +     nRo2
print("La suma es:", s)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 02.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero    =    int  (input  (    "Ingrese un número para calcular su factorial: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 03.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos.Agregue comentarios y documentación en los casos que se requieran.
"""

import numpy as np

MATRIZ_1 = np.array([    [2,6,2, 5],              [8, 3, 7, 3],            [5, 8, 1, 2]])
MATRIZ_2 = np.array([    [4,5,6,8],              [2, 3, 22, 3],            [7, 9, 11, 13]])

print (MATRIZ_1     +  MATRIZ_2)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 04.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.

"""

cadena_CARACTERES = input("Ingrese una cadena: ")
vocales = "aeiouAEIOU"
conteo_VOCALES = sum(1 for char in cadena_CARACTERES if char in vocales)
print("Número de vocales:", conteo_VOCALES)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 05.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def ecuacion_bernoulli(presion, densidad, velocidad, gravedad, altura):
    constante = presion + 0.5 * densidad * velocidad**2 + densidad * gravedad * altura
    return constante
presion_fluido = float(input("Ingrese la presión del fluido (P): "))
densidad_fluido = float(input("Ingrese la densidad del fluido (ρ): "))
velocidad_fluido = float(input("Ingrese la velocidad del fluido (v): "))
gravedad = float(input("Ingrese la aceleración debido a la gravedad (g): "))
altura_referencia = float(input("Ingrese la altura sobre el punto de referencia (h): "))
resultado_bernoulli = ecuacion_bernoulli(presion_fluido, densidad_fluido, velocidad_fluido, gravedad, altura_referencia)
print(resultado_bernoulli)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 06.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def ordenar_numeros():
      numeros = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
      numeros_ordenados     =     sorted(numeros)
      print("Lista ordenada:",    numeros_ordenados)
ordenar_numeros()

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 07.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

import matplotlib.pyplot as plt
def plot_histogram(datos, bins=20, edgecolor='black', xlabel='Valores', ylabel='Frecuencia', title='Histograma'):
    plt.hist(datos, bins=bins, edgecolor=edgecolor)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
import numpy as np
datos = np.random.randn(1000)
plot_histogram(datos)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 08.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

b = float(input("Ingrese la base del triángulo: "))
a = float(input("Ingrese la altura del triángulo: "))
t = 0.5 * b * a
print("El área del triángulo es:", t)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 09.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

import matplotlib.pyplot as plt
porcentajes = [25,
                            30,
                                      20,
                                               15,
                                                      10]
categoRIAS = ['A',
              'B',
              'C',
              'D',
              'E']

plt.pie(porcentajes, labels=categoRIAS, autopct='%1.1f%%', startangle=90) # configuracion del grafico
plt.title('Grafico de Pastel') # titulo del grafico
plt.show()

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 10.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

import pandas as pd
D = {'Nombre': ['Alice', 'Bob', 'Charlie'],'Edad': [25, 30, 35],'Ciudad': ['A', 'B', 'C']} #DATOS

df    =    pd.DataFrame(D)
print(df) #mostrar dataframe

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 11.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

import pandas as pd
def filtrar_personas_mayores(datos, edad_limite=30):
    df = pd.DataFrame(datos)
    MAYORESlimite = df[df['Edad'] > edad_limite]
    return MAYORESlimite

datos = {'Nombre': ['Alice', 'Bob', 'Charlie'], 'Edad': [25, 30, 35], 'Ciudad': ['A', 'B', 'C']}
personas_mayores = filtrar_personas_mayores(datos)
print("Personas mayores de 30 años:")
print(personas_mayores)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 12.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def movimiento_rectilineo_uniforme(velocidad, tiempo_total, intervalo_tiempo):
    tiempo = 0
    while tiempo <= tiempo_total:
        D = velocidad * tiempo #desplazamiento
        print(f"Tiempo: {tiempo} segundos - Posición: {D} unidades de distancia")
        tiempo += intervalo_tiempo

v = 5  # velocidad objeto
t = 10  # tiempo total simulacion en segundos
i = 1  #intervalo de tiempo en segundos
movimiento_rectilineo_uniforme(v, t, i)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 13.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def determinar_paridad(numero):
    if numero % 2 == 0: #comprobación
        print("El número es par.")
    else:
        print("El número es impar.")

n = int(input())
determinar_paridad(n)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 14.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def CELSIUS_a_fahrenheit(celsius):
    return celsius     * 9/5    +      32
def fahrenheit_a_CELSIUS(fahrenheit):
    return (fahrenheit -      32)       * 5/9
print(CELSIUS_a_fahrenheit(0))
print(fahrenheit_a_CELSIUS(32))

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 15.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b




def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"





print(suma(5, 3))
print(resta(7, 2))
print(multiplicacion(4, 6))
print(division(8, 2))

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 16.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def verificar_circulo_unico():



    n = int(input())
    for i in range(n):
        cables = input()
        cable_f = cables.count("F")
        cable_m = cables.count("M")
        if cable_f == cable_m:
            print("Es posible hacer un único círculo")



        else:
            print("No es posible")



verificar_circulo_unico()

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 17.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

def cambiafrase(nombre):
    corregido = ""
    for parte in nombre:
        corregido =   corregido   +     parte.capitalize()
    return corregido



n =       int(input())
for i in range(n):
    nombre = input().split('_')
    print(cambiafrase(nombre))

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 18.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

import random
NS = random.randint(1, 100) #NUMERO SERCRETO
i = 0#intentos
while True:
    I_U = int(input("Adivina el número (entre 1 y 100): "))       #INTENTO USUARIOS
    i += 1#intentos
    if I_U == NS:
        print(f"¡Correcto! Has adivinado en {i} intentos.")
        break
    elif I_U < NS:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 19.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

import numpy as np
numeros_ALEATORIOS = np.random.randint(1, 101, 10) # NUMEROS ALEATORIOS ENTRE 1 Y 100
print("Arreglo de números aleatorios:")
print(numeros_ALEATORIOS)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8

"""## 20.
Modifique el siguiente código para que se ajuste a las recomendaciones del PEP 8. Asigne nombres significativos a los elementos. Agregue comentarios y documentación en los casos que se requieran.
"""

import numpy as np
arreglo_original = np.array([ 1,2,3,4,5,6,7,8,9,10]) # arreglo de números del 1 al 10





M2x5 = arreglo_original.reshape(2, 5) # Cambiar la forma del arreglo a una matriz 2x5


s_C = np.sum(M2x5, axis=0)            #  Calcular la suma de cada columna

print("Arreglo Original:")
print(arreglo_original)
print("\nMatriz 2x5:")
print(M2x5)
print("\nSuma de cada columna:")
print(s_C)

# Modifique en esta casilla el código anterior para que se ajuste al PEP8