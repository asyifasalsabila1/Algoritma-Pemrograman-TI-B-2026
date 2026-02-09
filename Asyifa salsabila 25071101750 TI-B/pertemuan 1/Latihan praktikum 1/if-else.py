#1
a= 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")



# ===============================
# Contoh Semua Jenis If-Else
# ===============================

nilai = 85
umur = 20
status = "mahasiswa"
angka = 15
x = 10
buah = ["apel", "jeruk", "mangga"]
y = None

# 1. if, elif, else
print("=== 1. if, elif, else ===")   #mengecek beberapa kondisi berurutan
if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
elif nilai >= 60:
    print("Grade C")
else:
    print("Grade D")

# 2. Shorthand if (ternary operator)
print("\n=== 2. Shorthand if ===")
hasil = "Lulus" if nilai >= 60 else "Tidak Lulus"
print("Hasil:", hasil)

# 3. Logical operators (and, or, not)
print("\n=== 3. Logical operators ===")
if umur >= 18 and status == "mahasiswa":        #and untuk semua kondisi harus True
    print("Boleh ikut kegiatan kampus")
if umur < 18 or status != "mahasiswa":          #or untuk satu kondisi True cukup
    print("Tidak memenuhi syarat")
if not status == "dosen":                        #not untuk membalik nilai True/False
    print("Bukan dosen")

# 4. Nested if 
print("\n=== 4. Nested if ===")      #mencocokkan pengecekkan lebih spesifik if di dalam if
if angka > 0:
    if angka % 2 == 0:
        print(angka, "adalah bilangan positif genap")
    else:
        print(angka, "adalah bilangan positif ganjil")
else:
    print(angka, "adalah bilangan nol atau negatif")

# 5. Pass statement
print("\n=== 5. Pass statement ===")
if x > 0:
    pass  #digunakan ketik belum ingin menulis kode di dalam if
print("Program tetap berjalan meskipun if kosong")

# 6. Multiple conditions dalam satu if
print("\n=== 6. Multiple conditions ===")     #memeriksa kondisi manggunakan and atau or
if nilai >= 75 and umur >= 18 and status == "mahasiswa":
    print("Memenuhi semua syarat untuk program beasiswa")

# 7. If dengan membership (in)
print("\n=== 7. Membership (in) ===")
if "apel" in buah:                 # in untuk mengecek item ada di list atau tidak
    print("Apel tersedia di daftar buah")
if "pisang" not in buah:           #not in untuk cek apakah  item tidak ada
    print("Pisang tidak tersedia di daftar buah")

# 8. If dengan identity (is)
print("\n=== 8. Identity (is) ===")
if y is None:                    #is di gunakan untuk memeriksa apakah variabel objek tertentu 
    print("Variabel y belum diberi nilai")


