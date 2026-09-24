# 🖼️ Procesamiento Digital de Imágenes: Cálculo de Función de Densidad de Probabilidad (PDF)

Este proyecto realiza el análisis de niveles de intensidad de grises y el cálculo de la **Función de Densidad de Probabilidad (PDF)** sobre una imagen utilizando **Python**, **OpenCV**, **NumPy**, **Matplotlib** y **Seaborn**.

---

## 🚀 Características

- 📷 **Carga y Conversión:** Lee la imagen de entrada en escala de grises (`cv2.imread(..., 0)`) y la guarda como copia de trabajo[cite: 21, 22].
- 📐 **Análisis de Dimensiones:** Obtiene el alto, ancho y calcula el total de píxeles ($alto \times ancho$) de la imagen[cite: 21, 22].
- 📊 **Conteo de Intensidades:** Determina la frecuencia de cada nivel de gris (0 a 255) empleando `np.unique`[cite: 21, 22].
- 📈 **Cálculo de la Función de Densidad (PDF):** Normaliza el histograma dividiendo la frecuencia entre el total de píxeles[cite: 22].
- 🎨 **Visualización y Exportación:** Genera un gráfico tipo *stem plot* estilizado con Seaborn y exporta el resultado como imagen gráfica (`f_densidad_entrada_img2_E14.jpg`)[cite: 22, 24].

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **OpenCV (`opencv-python`)**[cite: 22]
- **NumPy**[cite: 22]
- **Matplotlib**[cite: 22]
- **Seaborn**[cite: 22]

---

## 📁 Estructura del Repositorio

```text
Digital-Image-Processing-in-Python/
├── QuickSort algorithm.py              # Script principal con la lógica de procesamiento
├── img2_E14.jpg                        # Imagen original de entrada (color)
├── Entrada_img2_E14.jpg                # Imagen procesada en escala de grises
└── f_densidad_entrada_img2_E14.jpg     # Gráfico generado de la función de densidad
