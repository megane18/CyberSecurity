# CyberSecurity


# Cybersecurity Journey Progress Tracker

## Overview

This README is to educate people about different encoding schemes and their functionalities. It also tracks my progress as I transition smoothly into the field of cybersecurity.

---

## What Are These Encoding Schemes?

### Base64 Encoding

Base64 is an encoding scheme, but what does that actually mean?  
It transforms data (often binary, such as images or files) into a text format using only characters that are safe and easy to use online.

### Why Is It Called Base64?

Base64 gets its name because it uses **64** different characters to represent data.

Here are the 64 characters used in Base64 encoding:
A–Z, a–z, 0–9, +, /


A sample Base64-encoded output looks like this:


---

### Hexadecimal (HEX) Encoding

When we encrypt something, the resulting ciphertext often includes bytes that are not printable ASCII characters. If we want to share this encrypted data, it's common to encode it into something more user-friendly and portable across different systems.

Hexadecimal encoding is one such method. It represents ASCII strings by first converting each letter to an ordinal number according to the ASCII table. Then, these decimal numbers are converted into base-16 numbers, also known as hexadecimal. The numbers can be combined into one long hex string.

Example of a flag encoded as a hex string:
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d


To decode this back into bytes in Python, use the `bytes.fromhex()` function. You can also use the `.hex()` instance method to convert byte strings into their hex representation.

---

## Binary Representation

Understanding binary is crucial in cybersecurity and encoding schemes. Here's an example of a binary representation of the number **195**:
128 64 32 16 8 4 2 1
0 1 1 0 0 0 0 1

This can be converted to hexadecimal or Base64 for easier storage and sharing.

---

## Progress Tracker

- **Topic 1:** Base64 Encoding  
- **Topic 2:** Hexadecimal Encoding  
- **Goal:** Smooth transition into cybersecurity
