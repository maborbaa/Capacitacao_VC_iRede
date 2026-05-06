def convert_rgb_to_hsv(r, g, b):
    # Normalização
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax - cmin

    # Cálculo do Hue (Matiz) em graus
    if diff == 0:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    # Cálculo da Saturação em %
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100

    # Cálculo do Valor (Brilho) em %
    v = cmax * 100

    return h, s, v

# O teste da aula
r, g, b = 150, 50, 200
h, s, v = convert_rgb_to_hsv(r, g, b)

print(f"Entrada RGB: ({r}, {g}, {b})")
print(f"Saída HSV: ({h:.1f}°, {s:.1f}%, {v:.1f}%)")