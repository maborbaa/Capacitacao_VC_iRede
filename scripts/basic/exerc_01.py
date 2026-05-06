#Exercício 1: Imagem Digital
#Objetivo: Criar uma imagem do zero usando apenas o NumPy
# Criaremos uma matriz pequena (5x5) onde você vai pintar pixels puramente digitando números 
# e depois usaremos o Matplotlib para visualizar essa matriz como uma imagem em tons de cinza
import numpy as np
import matplotlib.pyplot as plt

matrix_= np.array([
    [0,128,255],
    [60,100,150]
], dtype=np.uint8)

print(matrix_.shape)
print(matrix_.dtype)

back_ = np.zeros((5,5), dtype = np.uint8)
back_[2,2]=255

plt.imshow(back_, cmap='gray')
#plt.imshow(matrix_, cmap='gray')
plt.title("Print")
plt.show()
