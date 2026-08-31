# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 01:33:03 2024

@author: jose ochoa
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

n = 1

img = cv2.imread('img2_E14.jpg', 0)
cv2.imwrite('Entrada_img2_E14.jpg', img) 
alto, ancho = img.shape 
pixeles = alto*ancho 

values, counts = np.unique(img, return_counts=True)

x = np.arange(256)
f_densidad = np.zeros(256)
f_densidad[values]=counts 

x, f_densidad = x/255, f_densidad/pixeles 

sns.set_theme()
plt.figure(figsize=(16, 9))
plt.stem(x, f_densidad)
plt.tight_layout()
plt.savefig('f_densidad_entrada_img2_E14.jpg') 

#Ejercicio de clase 17