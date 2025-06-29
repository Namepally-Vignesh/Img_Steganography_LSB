from PIL import Image
import numpy as np

DELIMITER = '1111111111111110'

def bits_to_text(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join([chr(int(c, 2)) for c in chars])

def decode(image_path):
    image = Image.open(image_path).convert('RGB')
    pixels = np.array(image)
    flat = pixels.flatten()

    bits = ''.join([str(p & 1) for p in flat])
    end = bits.find(DELIMITER)

    if end == -1:
        print("No hidden message found.")
        return

    message_bits = bits[:end]
    message = bits_to_text(message_bits)
    print("\n Hidden Message Extracted:")
    print(message)

if __name__ == '__main__':
    print(" Image Steganography Decoder")
    image_path = input("Enter encoded PNG image (e.g. encoded.png): ").strip()
    decode(image_path)
