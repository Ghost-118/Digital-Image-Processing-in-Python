# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 01:33:03 2024

@author: jose ochoa
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Variable de configuración/control (reservada para iteraciones o identificadores)
n = 1

# --- 1. LECTURA Y PREPROCESAMIENTO DE LA IMAGEN ---
# Carga la imagen en escala de grises (el argumento 0 indica monocromático/grayscale)
img = cv2.imread('img2_E14.jpg', 0)

# Guarda una copia de la imagen de entrada cargada para respaldo/verificación
cv2.imwrite('Entrada_img2_E14.jpg', img) 

# Obtiene las dimensiones de la imagen (resolución en píxeles)
alto, ancho = img.shape 

# Calcula la cantidad total de píxeles en la imagen
pixeles = alto * ancho 

# --- 2. CÁLCULO DE FRECUENCIAS Y DENSIDAD ---
# Obtiene los niveles de gris presentes (values) y la cantidad de veces que se repiten (counts)
values, counts = np.unique(img, return_counts=True)

# Crea el eje X representando los 256 niveles de intensidad (de 0 a 255)
x = np.arange(256)

# Inicializa un arreglo de ceros para almacenar la frecuencia de cada nivel de gris
f_densidad = np.zeros(256)

# Asigna el conteo obtenido a sus respectivos niveles de intensidad dentro del arreglo
f_densidad[values] = counts 

# --- 3. NORMALIZACIÓN DE DATOS ---
# Normaliza el eje X al rango [0, 1] y la función de densidad dividiendo entre el total de píxeles
x, f_densidad = x / 255, f_densidad / pixeles 

# --- 4. GRAFICADO Y EXPORTACIÓN ---
# Aplica el estilo estético predeterminado de Seaborn para la gráfica
sns.set_theme()

# Define el tamaño de la figura (resolución proporcional 16:9)
plt.figure(figsize=(16, 9))

# Genera un gráfico de tipo Stem (diagrama de agujas/bastones) para representar la densidad
plt.stem(x, f_densidad)

# Ajusta los márgenes automáticamente para aprovechar todo el espacio del lienzo
plt.tight_layout()

# Exporta y guarda el gráfico resultante como archivo de imagen
plt.savefig('f_densidad_entrada_img2_E14.jpg')

#Ejercicio de clase 17
