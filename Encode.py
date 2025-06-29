from PIL import Image
import numpy as np

DELIMITER = '1111111111111110'  # Unique bit pattern to signal end of message

def text_to_bits(text):
    return ''.join([format(ord(c), '08b') for c in text])

def encode(image_path, message, output_path):
    image = Image.open(image_path).convert('RGB')
    pixels = np.array(image)
    flat = pixels.flatten()

    binary = text_to_bits(message) + DELIMITER
    if len(binary) > len(flat):
        raise ValueError("Message too long for this image!")

    for i in range(len(binary)):
        flat[i] = (flat[i] & 0xFE) | int(binary[i])

    encoded = flat.reshape(pixels.shape)
    Image.fromarray(encoded.astype(np.uint8)).save(output_path)
    print(f" Message encoded successfully into '{output_path}'.")

if __name__ == '__main__':
    print(" Image Steganography Encoder")
    image_path = input("Enter input PNG image (e.g. cover.png): ").strip()
    message = input("Enter message to hide: ").strip()
    output_path = input("Enter output filename (e.g. encoded.png): ").strip()

    encode(image_path, message, output_path)
