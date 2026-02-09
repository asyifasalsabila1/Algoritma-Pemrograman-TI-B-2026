tipe1 = '1'
tipe2 = 1
tipe3 = 1.5 
tipe4 = True 
tipe5 = [1, 3, 4, 5]
tipe6 = ['Asyifa', 2,3]
tipe7 = (1, 2, 3)
tipe8 = {
    'nama' :'Asyifa',
    'kelas' : 'TI B',
    'nim' : '25071101750',
    'mahasiswa aktif' : True 
}

print (type (tipe1))
print (type (tipe2))
print (type (tipe3))
print (type (tipe4))
print (type (tipe5))
print (type (tipe6))
print (type (tipe7))
print (type (tipe8))
print ()

print (tipe5 [3])
print (tipe6 [0])
print (tipe7 [1])
print (tipe8 ['nim'])        #kalau mau ambil indeks 



#2
# Integer
x = 10
print(x, "adalah tipe", type(x))  # <class 'int'>

# Float
y = 3.5
print(y, "adalah tipe", type(y))  # <class 'float'>

# String
nama = "Amel"
print(nama, "adalah tipe", type(nama))  # <class 'str'>

# Boolean
is_senang = True
print(is_senang, "adalah tipe", type(is_senang))  # <class 'bool'>


#3
# Program contoh tipe data di Python

# 1. Integer (bilangan bulat)
umur = 20
print("umur:", umur, "| tipe:", type(umur))

# 2. Float
tinggi = 165.5          #variabel bertipe float(bilangan desimal)
print("tinggi:", tinggi, "| tipe:", type(tinggi))

# 3. String (teks)
nama = "Budi"
print("nama:", nama, "| tipe:", type(nama))

# 4. Boolean
lulus = True          #variabel  yang hanya bisa True atau False 
print("lulus:", lulus, "| tipe:", type(lulus))

# 5. List 
buah = ["apel", "jeruk", "mangga"]      #variabel daftar data bisa diubah
print("buah:", buah, "| tipe:", type(buah))

# 6. Tuple 
angka = (1, 2, 3)         #variabel daftar  data tidak bisa di ubah 
print("angka:", angka, "| tipe:", type(angka))

# 7. Dictionary (pasangan key: value)
mahasiswa = {"nama": "Ani", "umur": 21}
print("mahasiswa:", mahasiswa, "| tipe:", type(mahasiswa))

# 8. Set (kumpulan unik)
warna = {"merah", "hijau", "biru"}
print("warna:", warna, "| tipe:", type(warna))
