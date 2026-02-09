#1
a = min(12, 7, 19)
b = max(12, 7, 19)

print("Nilai minimum:", a)
print("Nilai maksimum:", b)


#penjelasaan  
# Daftar angka
angka1 = 12
angka2 = 7
angka3 = 19
angka4 = 25
angka5 = 3

print("=== Program Min & Max ===")
print("Daftar angka:", angka1, angka2, angka3, angka4, angka5)

# Mencari nilai terkecil dan terbesar
nilai_min = min(angka1, angka2, angka3, angka4, angka5)
nilai_max = max(angka1, angka2, angka3, angka4, angka5)

# Menampilkan hasi
print(f"Nilai minimum dari daftar angka adalah: {nilai_min}")
print(f"Nilai maksimum dari daftar angka adalah: {nilai_max}")



#2
# Program Menu Restoran Sederhana menggunakan match-case

print("=== Selamat datang di Restoran salsa ===")
print("Menu tersedia:")
print("1. Nasi Goreng")
print("2. bakso")
print("3. Soto medan")
print("4. Es Teh")
print("5. Air Mineral")
# Input pilihan dari user
pilihan = input("Masukkan nama menu: ")

# Match statement untuk menentukan harga dan kategori
match pilihan:
    case "Nasi Goreng":
        harga = 20000
        kategori = "Makanan Berat"
        print(f"{pilihan} | {kategori} | Harga: Rp{harga}")
    case "bakso":
        harga = 12000
        kategori = "Makanan Berat"
        print(f"{pilihan} | {kategori} | Harga: Rp{harga}")
    case "Soto medan":
        harga = 15000
        kategori = "Makanan Ringan"
        print(f"{pilihan} | {kategori} | Harga: Rp{harga}")
    case "Es Teh" | "Teh Manis":
        harga = 5000
        kategori = "Minuman"
        print(f"{pilihan} | {kategori} | Harga: Rp{harga}")
    case "Air Mineral":
        harga = 3000
        kategori = "Minuman"
        print(f"{pilihan} | {kategori} | Harga: Rp{harga}")
    case _:  # default jika menu tidak dikenal
        print("Menu tidak tersedia. Silakan pilih menu yang ada.")
