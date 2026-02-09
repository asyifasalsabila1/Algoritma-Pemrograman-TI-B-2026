# 1. Function dengan parameter biasa
def greet(nama):
    print("Halo, " + nama + "!")

# 2. Function dengan parameter default
def greet_with_time(nama, waktu="pagi"):
    print("Selamat " + waktu + ", " + nama + "!")

# 3. Function dengan *args (bisa banyak input)
def youngest_child(*kids):
    print("Anak termuda adalah " + kids[-1])

# 4. Function dengan **kwargs (keyword argument)
def student_info(**info):
    print("Informasi Mahasiswa:")
    for key, value in info.items():
        print(key + ":", value)

# 5. Function dengan return
def total_price(*harga):
    total = sum(harga)
    return total

# ============================
# Memanggil semua function

# 1. Parameter biasa
greet("ciput")

# 2. Parameter default
greet_with_time("ani")            # pakai default
greet_with_time("Ani", "malam")   # ganti default

# 3. *args
youngest_child("Emil", "Tobias", "Linus")

# 4. **kwargs
student_info(Nama="Asyifa", Jurusan="TI", Umur=19)

# 5. Return value
harga_total = total_price(10000, 15000, 20000)
print("Total harga:", harga_total)



# DECORATOR
def auth(func):
    def wrapper(*args, **kwargs):
        print("\nAkses diverifikasi...")
        return func(*args, **kwargs)
    return wrapper

# GLOBAL SCOPE
# =====================================
nilai_lulus = 75          #variabel global, bisa diakses di semua function.
# GENERATOR
# =====================================
def generate_id():
    i = 1
    while True:          #loop tak terbatas, generator bisa dipanggil berkali-kali.
        yield f"MHS{i:03}"
        i += 1


id_mahasiswa = generate_id()       #Membuat instance generator, bisa dipanggil next(id_mahasiswa) untuk dapat ID berikutnya.

# RECURSION
# =====================================
def rata_rata(nilai_list, total=0):
    if not nilai_list:
        return total
    return rata_rata(nilai_list[1:], total + nilai_list[0])


# =====================================
# FUNCTION UTAMA
# =====================================
@auth
def proses_nilai(nama, *nilai, bonus=0, **info):
    """
    nama   : nama mahasiswa
    *nilai : nilai ujian
    bonus  : default argument
    **info : info tambahan
    """

    # local scope
    total = rata_rata(nilai)
    jumlah_nilai = len(nilai)
    rata = total / jumlah_nilai

    # lambda
    tambah_bonus = lambda x: x + bonus
    nilai_akhir = tambah_bonus(rata)

    # kelulusan (pakai global)              #Ternary operator: mengecek apakah mahasiswa lulus
    status = "LULUS" if nilai_akhir >= nilai_lulus else "TIDAK LULUS"

    print(f"Nama   : {nama}")              #Mencetak informasi mahasiswa.
    print(f"Nilai  : {nilai}")             
    print(f"Bonus  : {bonus}")
    print(f"Rata   : {nilai_akhir:.2f}")    #:.2f format angka 2 desimal.
    print(f"Status : {status}")

    # kwargs                   #Mengecek keyword argument (info) mencetaknya.

    if info:
        print("Info tambahan:") 
        for k, v in info.items():
            print(f"- {k}: {v}")

    return nilai_akhir               #Mengembalikan nilai akhir.


# PROGRAM UTAMA
# =====================================
if __name__ == "__main__":

    # generator dipakai               #Memanggil generator untuk mendapatkan 2 ID mahasiswa.
    id1 = next(id_mahasiswa)
    id2 = next(id_mahasiswa)

    print("ID Mahasiswa:", id1)      #Memanggil function utama dengan positional argument,args, default argument, dan kwargs.Output akan melewati decorator (auth) dulu.
    proses_nilai(
        "Andi",
        80, 85, 90,
        bonus=5,
        jurusan="Informatika",
        semester=4
    )

    print("\nID Mahasiswa:", id2)
    proses_nilai(
        "Budi",
        60, 65, 70,
        bonus=3,
        jurusan="Sistem Informasi",
        semester=2
    )
