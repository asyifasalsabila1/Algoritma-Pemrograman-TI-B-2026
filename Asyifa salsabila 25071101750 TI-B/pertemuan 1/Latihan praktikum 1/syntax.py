print("hello word")
print('hello word')

nama = 'asyifa'
print(f'hello nama  saya {nama }')

tanggallahir = 28
bulan = 5
tahun = 2006

print(f'saya  lahir pada tanggal {tanggallahir} {bulan} {tahun}')

namalengkap ='asyifa salsabila'
panggilan = 'ciput'
alamatsekarang = 'balam sakti ,pekanbaru'
tempatlahir = 'sorek'
tahun = 2006 
usia  = 20
print(f'hallo nama  saya,panggilan  {namalengkap}, {panggilan}')
print(f'saya lahir di {tempatlahir} {tanggallahir} {bulan} {tahun}')
print(f'saya beralamat di {alamatsekarang}')
print(f'usia saya saat ini {usia}')



# Program ucapan Selamat Pagi

# Menampilkan pesan pembuka
print("Selamat Pagi!")
nama = "Asyifa"
print(f"Halo {nama}, selamat pagi semogaharimu bahagia selalu.")
print("Semoga hari ini menyenangkan dan penuh semangat.")

# Menampilkan motivasi
print("tersenyumlah di setiap pagi ")
print("Jangan lupa sarapan.")
print("semangat pagi ituu penting!")


# Menampilkan penutup
print("Selamat beraktivitas hari ini!")
print("Tetap semangat dan terus berdoa!")



# Program ucapan selamat pag
# 1statment menyimpan nilai ke variabel 
nama = "Asyifa"    #nama = string, umur = integer 20
umur = 20 

# Function & Expression
def ucapan(nama):      #mendefinisikan function ucapan dengan parameter nama.
    print(f"Halo {nama}, selamat pagi! Semoga harimu menyenangkan.")

ucapan(nama)              #memanggil function ucapan dengan argumen nama

# Compound Statement & Logical Operator
hari = "Senin"         #assignment string ke variabel hari dan cuaca
cuaca = "cerah"

if hari == "Senin" or hari == "Selasa":                #if dan else adalah statement dengan blok.
    print("Hari ini semangat olahraga pagi!")          #or digunakan untuk mengecek dua kondisi.
else:                                                   
    print("Nikmati harimu dengan senyuman :)")          #blok di dalam if/else ditandai dengan spasi.  

# Class Syntax
class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"{self.nama}, umur {self.umur} tahun. Semangat belajar!")

mhs = Mahasiswa(nama, umur)
mhs.info()                           #Menampilkan informasi mahasiswa di console.

# 5️⃣ Import Statement & Expression
import math                             #memuat modul math agar bisa menggunakan fungsi dan konstanta math.
print("Nilai pi =", math.pi)             #math.pi dievaluasi menjadi angka, lalu dicetak dengan print().
z = umur + 5                             #umur + 5 dihitung.
print("Umur + 5 =", z)                    #assignment ke variabel z.
