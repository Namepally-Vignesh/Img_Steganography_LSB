# 🖼️ Image Steganography using LSB in Python

## Objective:
- This project implements a simple but powerful image steganography tool using the **Least Significant Bit (LSB)** technique in Python. It allows users to hide secret text messages inside PNG images without any visible change to the image, and retrieve them later with accuracy.

## 📌 Project Overview
- 🔐 **Steganography** hides the *existence* of the message, unlike encryption which hides the *content*.
- This tool uses **Python**, `Pillow`, and `NumPy` to manipulate image pixels.
- It works with **lossless PNG images** to ensure hidden data isn't corrupted.
- The system is capable of both **encoding** and **decoding** messages via command-line interaction.

## 📂 Features
- ✅ Encode text messages inside PNG images without altering appearance.
- ✅ Decode and retrieve hidden messages accurately.
- ✅ Works on any uncompressed RGB PNG image.
- ✅ Simple, readable Python code with minimal dependencies.

## ⚙️ Technologies Used
- Python 3.x  
- [Pillow (PIL)](https://pillow.readthedocs.io/) – Image processing  
- [NumPy](https://numpy.org/) – Pixel array manipulation

## 🚀 How to Use
Encode a message       
```bash
python encode.py
```
Input:
- Path to a PNG image (cover.png)
- Secret message
- Output image filename (encoded.png)

Decode a message
```bash
python decode.py
```
Input:
- Path to the encoded PNG image (encoded.png)

## 🌐 References
- https://pillow.readthedocs.io/
- https://numpy.org/
- https://en.wikipedia.org/wiki/Steganography
- https://geeksforgeeks.org/lsb-steganography
