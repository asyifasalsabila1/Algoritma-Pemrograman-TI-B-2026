#1
print (10 > 9)
print  (10 == 9)
print (10 < 9)

a = 200
b = 33 

if b > a:
    print(" b lebih kecil dar a")  #karna  nilai b adalah 33 dan a 200
else:
    print("a lebih besar dari  b")   #karna nilai a adalah 200 dan b 33




#2
    nama = "asyifa"     #nama mahasiswa yang lulus
nilai = 85              #nilai lulus mahasiswa

print("Nama mahasiswa:", nama)
print("Nilai:", nilai)

if nilai >= 85:
    print("Status: Lulus")
    print("Selamat,", nama, "kamu dinyatakan lulus.")
else:
    print("Status: Tidak Lulus")
    print("Maaf,", nama, "kamu harus mengikuti ujian ulang.")



#3
# Jumlah uang dan harga barang
uang_saku = 50_000
harga_buku = 30_000

# Mengecek apakah uang cukup untuk membeli buku
if uang_saku >= harga_buku:
    print("Uang cukup untuk membeli buku")
else:
    print("Uang tidak cukup untuk membeli buku")

# Contoh boolean langsung
lebih_besar = uang_saku > harga_buku   # menghasilkan True atau False
sama_dengan = uang_saku == harga_buku  # menghasilkan True atau False

print("Apakah uang_saku lebih besar dari harga_buku?", lebih_besar)
print("Apakah uang_saku sama dengan harga_buku?", sama_dengan)


#4
# Program pengecekan tiket bioskop

print("=== Selamat datang di Bioskop sukaramai ===")

# Data input user
umur = int(input("Masukkan umur Anda: "))
memiliki_id = input("Apakah Anda memiliki KTP/SIM? (ya/tidak): ").lower()
jenis_tiket = input("Masukkan jenis tiket (regular/vip): ").lower()

# Konversi input ke Boolean
memiliki_id_bool = True if memiliki_id == "ya" else False

# Aturan bioskop:
# - Harus minimal 17 tahun untuk menonton film dewasa
# - Harus memiliki ID
# - Tiket VIP hanya bisa untuk yang umur >= 21
boleh_masuk_film_dewasa = umur >= 17 and memiliki_id_bool
boleh_masuk_vip = umur >= 21 and memiliki_id_bool and jenis_tiket == "vip"

# Boolean kombinasi
boleh_masuk = boleh_masuk_film_dewasa or boleh_masuk_vip

# Menampilkan hasil
print("\n=== Hasil Pengecekan ===")
print("Boleh masuk film dewasa:", boleh_masuk_film_dewasa)
print("Boleh masuk VIP:", boleh_masuk_vip)
print("Boleh masuk bioskop:", boleh_masuk)

# Penjelasan berdasarkan kondisi
if boleh_masuk_vip:                 #Jika boleh_masuk_vip = True → tampil pesan VIP
    print("Selamat! Anda bisa masuk area VIP dan menonton film dewasa.")
elif boleh_masuk_film_dewasa:       #Jika boleh_masuk_film_dewasa = True → tampil pesan film dewasa regular
    print("Anda bisa menonton film dewasa dengan tiket regular.")
else:
    if umur < 17:                  #Jika kedua kondisi False → tampil pesan kenapa tidak boleh masuk:
        print("Maaf, umur Anda belum cukup untuk menonton film dewasa.")
    if not memiliki_id_bool:
        print("Maaf, Anda harus memiliki ID untuk menonton film.")
