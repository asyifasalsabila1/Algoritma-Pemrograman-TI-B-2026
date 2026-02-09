def jumlah_digit(n):
    # Jika n sudah 0, proses rekursi berhenti
    if n == 0:
        return 0
    # n % 10 mengambil digit terakhir
    # n // 10 menghilangkan digit terakhir
    # Fungsi memanggil dirinya sendiri sampai n menjadi 0
    return (n % 10) + jumlah_digit(n // 10)

# Contoh pemanggilan
print("Jumlah digit:", jumlah_digit(1234))
