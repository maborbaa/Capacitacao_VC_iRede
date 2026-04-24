import matplotlib
matplotlib.use('Qt5Agg') # Mantemos o nosso motor gráfico blindado

import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn import datasets

print("Carregando a imagem da flor...")

# 1. Carrega a imagem nativa da biblioteca (A mesma usada na aula)
# A imagem já vem no formato RGB
img_rgb = datasets.load_sample_image("flower.jpg")

# 2. Converte de RGB para HSV usando OpenCV
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

# 3. Separa os três canais do HSV
h, s, v = cv2.split(hsv)

# 4. Ajuste do Matiz (Hue)
# O OpenCV guarda o Matiz de 0 a 179 para caber em 8 bits. 
# O professor fez essa reescala matemática para 0-255 apenas para a tela exibir o cinza corretamente.
h_vis = np.uint8(h.astype(np.float32) * (255.0 / 179.0))

# 5. Plota os 4 quadros lado a lado
plt.figure(figsize=(15, 5))

# Imagem 1: Original
plt.subplot(1, 4, 1)
plt.imshow(img_rgb)
plt.title("Imagem Original (RGB)")
plt.axis("off")

# Imagem 2: Matiz (O "tipo" da cor)
plt.subplot(1, 4, 2)
plt.imshow(h_vis, cmap="gray")
plt.title("Canal H (Matiz)")
plt.axis("off")

# Imagem 3: Saturação (A pureza da cor - O)
plt.subplot(1, 4, 3)
plt.imshow(s, cmap="gray")
plt.title("Canal S (Saturação)")
plt.axis("off")

# Imagem 4: Valor (O brilho/iluminação)
plt.subplot(1, 4, 4)
plt.imshow(v, cmap="gray")
plt.title("Canal V (Valor)")
plt.axis("off")

print("Gerando painel comparativo...")
plt.show()