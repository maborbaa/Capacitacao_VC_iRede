import matplotlib
matplotlib.use('Qt5Agg') # Força o uso do PyQt5 no lugar do Tkinter quebrado

import numpy as np
import cv2
import matplotlib.pyplot as plt

print("Dependências importadas com sucesso!")
print(f"Versão do OpenCV: {cv2.__version__}")

# 1. Cria uma imagem artificial 100x100 pixels (Matriz NumPy)
# Três canais (RGB), preenchidos com zeros (preto)
imagem_rgb = np.zeros((100, 100, 3), dtype=np.uint8)

# Pinta um quadrado vermelho no centro
imagem_rgb[25:75, 25:75] = [255, 0, 0] # R=255, G=0, B=0

# 2. Converte de RGB para HSV usando OpenCV
imagem_hsv = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2HSV)

# 3. Plota os resultados com Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem_rgb)
plt.title("Imagem Original (RGB)")
plt.axis("off")

plt.subplot(1, 2, 2)
# Exibindo apenas o canal Hue (Matiz)
plt.imshow(imagem_hsv[:, :, 0], cmap='gray')
plt.title("Canal H (Matiz) do HSV")
plt.axis("off")

print("Gerando visualização... Feche a janela da imagem para encerrar o script.")
plt.show()