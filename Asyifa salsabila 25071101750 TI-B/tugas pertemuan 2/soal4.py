def pangkat_rekursif(a, b):
    # a = bilangan pokok
    # b = pangkat
    if b == 0:   # Jika pangkat 0, hasil selalu 1
        return 1
    return a * pangkat_rekursif(a, b - 1)

# Contoh pemanggilan
print("Hasil pangkat:", pangkat_rekursif(2, 5))
