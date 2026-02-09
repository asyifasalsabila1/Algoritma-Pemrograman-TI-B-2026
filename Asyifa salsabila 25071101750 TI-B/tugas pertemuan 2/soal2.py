def bilangan_prima(n):
     # List kosong untuk menyimpan bilangan prima
    prima = []
    for i in range(2, n + 1):
        is_prima = True
         # Mengecek apakah i punya pembagi selain 1 dan dirinya sendiri
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prima = False
                break
             # Jika setelah pengecekan i tetap prima
        if is_prima:
            prima.append(i)
    return prima

# Pemanggilan fungsi
hasil_prima = bilangan_prima(50)
print("Bilangan prima 1–50:", hasil_prima)
