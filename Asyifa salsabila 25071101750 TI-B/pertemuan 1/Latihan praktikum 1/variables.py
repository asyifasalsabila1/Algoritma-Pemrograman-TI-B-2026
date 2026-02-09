# Variabel dengan huruf kecil
nama = "Asyifa"
nama_depan = "Asyifa"
_nama = "ciput"

# Variabel dengan huruf besar/kecil campur
Nama = "Asyifa"
NAMa = "Asyifa"

# Variabel dengan angka
nama1 = "Asyifa"
_nama2 = "Asyifa"

# Variabel dengan underscore di tengah
nama_belakang = "Salsabila"

# Variabel sensitif terhadap huruf besar/kecil
print(nama)      # Asyifa
print(Nama)      # Asyifa(beda dengan nama)
print(NAMa)      # Asyifa (beda lagi)




#python numbers 
# Misal kita punya uang saku dan harga jajanan

# Integer (angka bulat)
uang_saku = 50000        # uang saku 50.000 rupiah
harga_bakso = 20000      # harga bakso 20.000 rupiah
jumlah_bakso = 2         # membeli 2 porsi

# Hitung total harga bakso
total_harga = harga_bakso * jumlah_bakso
print("Total harga bakso:", total_harga)

# Hitung sisa uang saku
sisa_uang = uang_saku - total_harga
print("Sisa uang saku:", sisa_uang)

# Float (angka desimal)
berat_buah = 1.5          # kg
harga_per_kg = 30000.5    # harga per kg dengan desimal
total_harga_buah = berat_buah * harga_per_kg
print("Total harga buah:", total_harga_buah)

# Complex (bilangan kompleks, misal contoh matematika)
bilangan_kompleks = 2 + 3j
print("Bilangan kompleks:", bilangan_kompleks)




#ptyhon multiple 
# List
buah = ["apel", "jeruk", "pisang"]
print("List buah:", buah)

# Tuple
hari = ("Senin", "Selasa", "Rabu")
print("Tuple hari:", hari)

# Dictionary
siswa = {"nama": "ciput", "umur": 21}
print("Dictionary siswa:", siswa)

# Set
angka = {1, 2, 3, 4, 4}  # duplikat 4 akan dihapus otomatis
print("Set angka:", angka)



# Number (angka)
harga_buku = 45000       #number untuk angka seperti harga atau berat
berat_buku = 1.2
print("Harga buku:", harga_buku)
print("Berat buku (kg):", berat_buku)

# String (teks)
nama_toko = "Toko Buku Pintar"      #string untuk nama toko atau kota
kota_toko = "Jakarta"
print("Nama toko:", nama_toko)
print("Kota toko:", kota_toko)

# Boolean (True / False)
tersedia = True                #boolean untuk menentukan true/false jika  kondisi ketersedian atau diskon
diskon_aktif = False
print("Apakah buku tersedia?", tersedia)
print("Apakah diskon aktif?", diskon_aktif)

# List (daftar nilai)
jenis_buku = ["Novel", "Komik", "Ensiklopedia"]         #list untuk daftar  nilai yang bisa di ubah,contohnya jenis buku 
print("Jenis buku di toko:", jenis_buku)

# Tuple (daftar yang tidak bisa diubah)
hari_buka = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat")   #tuple untuk daftar nilai yang tidak bisa di ubah contohnya hari buka toko
print("Hari buka toko:", hari_buka)

# Dictionary (key-value)
buku = {"judul": "Python untuk Pemula", "penulis": "Budi", "halaman": 250}   #ductionary untuk detail buku 
print("Data buku:", buku)
print("Judul buku:", buku["judul"])
print("Penulis buku:", buku["penulis"])


# Variabel global
nama_toko = "Toko Buku salsabila"

def tampil_nama_toko():
    # Mengakses variabel global dari dalam fungsi
    print("Nama toko:", nama_toko)

def ubah_nama_toko(nama_baru):
    # Mengubah variabel global
    global nama_toko
    nama_toko = nama_baru
    print("Nama toko telah diubah menjadi:", nama_toko)

# Mengakses global variabel
tampil_nama_toko()

# Mengubah global variabel
ubah_nama_toko("Toko Buku bila")

# Mengecek perubahan
tampil_nama_toko()

