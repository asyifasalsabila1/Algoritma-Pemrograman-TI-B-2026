#soal 4 (perulangan )
# Program menampilkan bilangan 1 sampai 10 dan menghitung jumlahnya

# Inisialisasi variabel jumlah
jumlah = 0

# Menampilkan judul program
print("===================================")
print("Program Menampilkan Bilangan 1-10")
print("Dan Menghitung Jumlahnya")
print("===================================\n")

# Menggunakan perulangan for untuk menampilkan bilangan 1 sampai 10
for i in range(1, 11):  # range(1, 11) menghasilkan angka 1 sampai 10
    print("Bilangan saat ini:", i)  # Menampilkan bilangan saat ini
    jumlah += i                    # Menambahkan bilangan ke variabel jumlah
    print("Jumlah sementara:", jumlah, "\n")  # Menampilkan jumlah sementara

# Menampilkan total jumlah akhir
print("===================================")
print("Jumlah akhir dari bilangan 1 sampai 10 =", jumlah)
print("===================================")


