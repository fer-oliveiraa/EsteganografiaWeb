from PIL import Image
import os

# Converte uma string em uma sequência binária
def str_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Converte binário em texto
def bin_to_str(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)

# Esconde texto em imagem usando LSB
def hide_text_in_image(image_path, output_path, secret_text):
    img = Image.open(image_path).convert('RGB')

    # Converte para PNG se não for
    if not image_path.lower().endswith('.png'):
        converted_path = os.path.splitext(image_path)[0] + '_converted.png'
        img.save(converted_path, format='PNG')
        img = Image.open(converted_path).convert('RGB')

    pixels = img.load()

    # Prepara a mensagem + delimitador
    binary_text = str_to_bin(secret_text) + '1111111111111110'
    total_bits = len(binary_text)
    max_capacity = img.width * img.height * 3  # 3 bits por pixel

    if total_bits > max_capacity:
        raise ValueError(
            f"Mensagem muito longa para esta imagem! "
            f"Capacidade máxima: {(max_capacity - 16) // 8} caracteres, "
            f"mensagem enviada: {len(secret_text)} caracteres."
        )

    idx = 0
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            if idx < total_bits:
                r = (r & ~1) | int(binary_text[idx])
                idx += 1
            if idx < total_bits:
                g = (g & ~1) | int(binary_text[idx])
                idx += 1
            if idx < total_bits:
                b = (b & ~1) | int(binary_text[idx])
                idx += 1
            pixels[x, y] = (r, g, b)
            if idx >= total_bits:
                break
        if idx >= total_bits:
            break

    img.save(output_path, format='PNG')


# Extrai o texto escondido na imagem
def extract_text_from_image(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()

    binary_text = ''
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_text += str(r & 1)
            binary_text += str(g & 1)
            binary_text += str(b & 1)

    end_marker = '1111111111111110'
    end_index = binary_text.find(end_marker)

    if end_index != -1:
        message_bits = binary_text[:end_index]
        if len(message_bits) % 8 != 0:
            return "Erro: mensagem truncada ou delimitador mal posicionado."
        return bin_to_str(message_bits)
    else:
        return "Delimitador de fim não encontrado."
