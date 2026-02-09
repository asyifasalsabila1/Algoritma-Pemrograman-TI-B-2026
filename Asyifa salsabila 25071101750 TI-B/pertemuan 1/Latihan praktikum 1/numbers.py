#1
# Jumlah barang (int)
manggis = 5
kelapa = 3

# Harga per buah (float)
harga_manggis = 2500.5
harga_kelapa = 3000.0

# Angka kompleks (contoh saja)
bilangan_complex = 2 + 3j

# Hitung total buah
total_buah = manggis + kelapa

# Hitung total harga
total_harga = (manggis * harga_manggis) + (kelapa * harga_kelapa)

# Konversi tipe data
total_harga_int = int(total_harga)      # float → int
manggis_float = float(manggis)                 # int → float
manggis_complex = complex(manggis)             # int → complex


# Menampilkan hasil
print("Jumlah manggis:", manggis)
print("Jumlah kelapa:", kelapa)
print("Total buah:", total_buah)

print("Total harga:", total_harga)
print("Total harga (int):", total_harga_int)

print("manggis sebagai float:", manggis_float)
print("manggis sebagai complex:", manggis_complex)

# Cek tipe data
print(type(manggis))
print(type(harga_manggis))
print(type(bilangan_complex))
