def gcd(a, b):
    """Fungsi untuk mencari Faktor Persekutuan Terbesar (FPB/GCD)"""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """
    Fungsi untuk mencari Invers Modulo menggunakan Extended Euclidean Algorithm.
    Ini digunakan untuk mencari Kunci Privat (d).
    """
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    
    while y3 != 0:
        q = x3 // y3
        y1, y2, y3, x1, x2, x3 = (x1 - q * y1), (x2 - q * y2), (x3 - q * y3), y1, y2, y3
        
    if x3 == 1:
        return x2 % phi
    return None

def generate_keypair(p, q):
    """Fungsi untuk membangkitkan Kunci Publik dan Kunci Privat"""
    print("\n--- [1] TAHAP KEY GENERATION ---")
    
    # 1. Hitung n = p * q
    n = p * q
    print(f"[*] Menghitung n (Modulus) = p * q = {p} * {q} = {n}")
    
    # 2. Hitung phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)
    print(f"[*] Menghitung Phi(n) (Totient Euler) = ({p}-1) * ({q}-1) = {phi}")
    
    # 3. Pilih e (Kunci Publik)
    # Syarat: 1 < e < phi dan gcd(e, phi) == 1
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    print(f"[*] Menemukan e (Kunci Publik) yang relatif prima dengan {phi} = {e}")
    
    # 4. Hitung d (Kunci Privat)
    # Syarat: (d * e) % phi == 1
    d = mod_inverse(e, phi)
    print(f"[*] Menghitung d (Kunci Privat) = Invers Modulo dari {e} mod {phi} = {d}")
    
    print(f"\n[+] Kunci Publik (e, n) : ({e}, {n})")
    print(f"[+] Kunci Privat (d, n) : ({d}, {n})")
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Fungsi Enkripsi mengubah teks menjadi angka rahasia (Ciphertext)"""
    print("\n--- [2] TAHAP ENKRIPSI ---")
    e, n = public_key
    
    # Rumus Enkripsi RSA: C = M^e mod n
    # Mengubah huruf menjadi nilai ASCII (M), lalu dienkripsi (C)
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    
    print(f"[*] Plaintext: '{plaintext}'")
    print(f"[*] Proses: Mengubah karakter ke ASCII -> M^{e} mod {n}")
    print(f"[+] Hasil Ciphertext (Array Angka): {ciphertext}")
    
    return ciphertext

def decrypt(private_key, ciphertext):
    """Fungsi Dekripsi mengembalikan angka rahasia menjadi teks asli"""
    print("\n--- [3] TAHAP DEKRIPSI ---")
    d, n = private_key
    
    # Rumus Dekripsi RSA: M = C^d mod n
    # Mengubah angka sandi (C) kembali ke nilai ASCII (M), lalu jadi huruf
    decrypted_chars = [chr((char ** d) % n) for char in ciphertext]
    plaintext = ''.join(decrypted_chars)
    
    print(f"[*] Ciphertext: {ciphertext}")
    print(f"[*] Proses: C^{d} mod {n} -> Mengembalikan ke karakter")
    print(f"[+] Hasil Dekripsi: '{plaintext}'")
    
    return plaintext

# MAIN EXECUTION (Demonstrasi Program)
if __name__ == '__main__':
    print("=== DEMONSTRASI ALGORITMA RSA DARI NOL ===")
    
    # Menggunakan bilangan prima kecil untuk demonstrasi agar mudah dilacak
    # Untuk keamanan nyata, p dan q haruslah bilangan prima yang sangat besar
    p = 61
    q = 53
    
    print(f"[*] Memulai dengan dua bilangan prima: p={p}, q={q}")
    
    # Proses Pembangkitan Kunci
    public, private = generate_keypair(p, q)
    
    # Pesan yang akan dienkripsi
    pesan_rahasia = "RAHMAT338"
    
    # Proses Enkripsi
    pesan_terenkripsi = encrypt(public, pesan_rahasia)
    
    # Proses Dekripsi
    pesan_terdekripsi = decrypt(private, pesan_terenkripsi)
    
    print("\n=== KESIMPULAN ===")
    if pesan_rahasia == pesan_terdekripsi:
        print("[SUKSES] Pesan berhasil dikembalikan dengan sempurna!")
    else:
        print("[GAGAL] Ada kesalahan dalam proses dekripsi.")