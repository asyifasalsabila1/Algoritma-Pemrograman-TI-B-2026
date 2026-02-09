#1
# 1. String single quote
nama = 'Asyifa salsabila '

# 2. String double quote
jurusan = "Teknik Informatika"

# 3. String berisi angka
nim = "25071101750"

# 4. String berisi simbol
email = "asyifa.salsabiila1750student.unri.ac.id"

# 5. String dengan spasi
alamat = "balam sakti, pekanbaru"

# 6. String multi-line (triple quote)
biodata = """BIODATA MAHASISWA
------------------
Nama    : Asyifa salsabila
Jurusan : Teknik Informatika
"""

# 7. Penggabungan string
info = "Nama: " + nama + " | Jurusan: " + jurusan

# 8. Escape character
catatan = "Status:\n\tMahasiswa Aktif"

# 9. Index string
huruf_pertama_nama = nama[0]

# 10. Slice string
potong_nama = nama[0:4]

# 11. String diambil dari belakang
akhir_nim = nim[-3:]

# 12. Reverse string
nama_terbalik = nama[::-1]

# Menampilkan hasil
print(nama)
print(jurusan)
print(nim)
print(email)
print(alamat)
print(biodata)
print(info)
print(catatan)
print(huruf_pertama_nama)
print(potong_nama)
print(akhir_nim)
print(nama_terbalik)



#2
# Variabel string
teks = "Selamat Datang"
nama = "ciput"
umur = 19
kata = " kota "

# 1️⃣ Slicing
print("=== Slicing ===")
print(teks[:7])   # Selamat
print(teks[8:])   # Datang
print(teks[-6:])  # Datang

# 2️⃣ Modifikasi
print("\n=== Modifikasi ===")
print(teks.upper())   # SELAMAT DATANG
print(teks.lower())   # selamat datang
print(teks.title())   # Selamat Datang

# 3️⃣ Concatenate
print("\n=== Concatenate ===")
print("Halo " + nama + "!")  # Halo ciput!

# 4️⃣ Format
print("\n=== Format ===")
print(f"{nama} berumur {umur} tahun")   # f-string
print("Nama {} umur {} tahun".format(nama, umur))  # format()

# 5️⃣ Escape Character
print("\n=== Escape Character ===")
print("Alamat: \"Jl. balam sakti\"")  # tanda kutip
print("Baris1\nBaris2")               # newline
print("Kolom A\tKolom B")             # tab

# 6️⃣ String Method
print("\n=== String Method ===")
print("Strip:", kata.strip())                         # hapus spasi
print("Replace:", kata.replace("kota", "desa"))      # ganti kata
print("Huruf kecil semua?", kata.islower())          # cek huruf kecil
print("Apakah angka?", kata.isdigit())               # cek angka

# 7️⃣ Exercise
print("\n=== Exercise ===")
# Ambil kata "Datang", ubah huruf besar, gabungkan kata lain
hasil = teks[8:].upper() + " ke acara"
print(hasil)

# Tambahan exercise sederhana
# Gabungkan nama + teks + umur menjadi kalimat
kalimat = f"{nama} menyapa: {teks}! Umurnya {umur} tahun."
print(kalimat)
