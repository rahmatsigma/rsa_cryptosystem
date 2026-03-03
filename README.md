# RSA Cryptosystem 🔐

This repository contains a pure Python implementation of the **RSA (Rivest-Shamir-Adleman)** asymmetric encryption algorithm. Built entirely from scratch without the use of any external cryptography libraries (like `import rsa` or `cryptography`), demonstrating the fundamental mathematics behind public-key cryptography.

This project is submitted as an assignment for the Cryptography Course.

## 📝 Features
This implementation covers the three main concepts of the RSA algorithm:
1. **Key Generation**: Mathematical computation to generate a Public Key $(e, n)$ and a Private Key $(d, n)$ using prime numbers, Euler's Totient function, and Modular Multiplicative Inverse.
2. **Encryption**: Converting plaintext into numeric ciphertext using the Public Key.
3. **Decryption**: Reversing the ciphertext back into readable plaintext using the Private Key.

## 🛠️ Prerequisites
- Python 3.x installed on your local machine.
- No external dependencies or libraries are required.

## 🚀 How to Run the Demo
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/rahmatsigma/rsa_cryptosystem.git]
   
2. Navigate to the project directory:
   ```bash
   [cd rsa-cryptosystem]

3. Run the Python script to see the step-by-step RSA demonstration:
   ```bash
   [python rsa_cryptosystem.py]

(Note: The program will print out every mathematical step, including Modulus calculation, Totient Euler, and the Keypair generation process).


Disclaimer: This implementation uses small prime numbers for educational and demonstration purposes to make the mathematical steps traceable. It is not intended for securing real-world data.
