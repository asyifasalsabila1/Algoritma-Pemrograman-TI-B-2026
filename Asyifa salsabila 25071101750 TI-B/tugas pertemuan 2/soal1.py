def rata_rata(nilai):
    # Mengecek apakah list kosong
    if len(nilai) == 0:
        return "Data kosong"
    return sum(nilai) / len(nilai) # Fungsi sum() digunakan untuk menjumlahkan seluruh elemen list
                                # Fungsi len() digunakan untuk menghitung jumlah data dalam list

# Pemanggilan fungsi
data_nilai = [80, 75, 90, 60, 85]  # Membuat list nilai mahasiswa
hasil = rata_rata(data_nilai)

print("Rata-rata nilai:", hasil)
