import math    # Mengimpor module math untuk fungsi akar kuadrat

def jarak(x1, y1, x2, y2):     # Menghitung selisih koordinat x
   # Menghitung jarak menggunakan rumus kartesius
    # sqrt = akar kuadrat
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   # Menghitung selisih koordinat y

# Contoh pemanggilan
hasil_jarak = jarak(1, 2, 4, 6)
print("Jarak =", hasil_jarak)
