#soal 5 (fungsi)
# Program menggunakan fungsi untuk penjumlahan dan pengurangan

print("===================================")
print("Program Fungsi Penjumlahan & Pengurangan")
print("===================================\n")

#Membuat fungsi bernama hitung yang menerima dua parameter a dan b
def hitung(a, b):
    print("Menghitung penjumlahan dan pengurangan...")
    print(f"Nilai a = {a}, Nilai b = {b}")
    
    # Menghitung penjumlahan
    penjumlahan = a + b
    print(f"Langkah: {a} + {b} = {penjumlahan}")
    
    # Menghitung pengurangan
    pengurangan = a - b
    print(f"Langkah: {a} - {b} = {pengurangan}")
    
    # Mengembalikan hasil penjumlahan dan pengurangan
    return penjumlahan, pengurangan

#Memanggil fungsi dengan nilai contoh
a = 5
b = 3
print("\nMemanggil fungsi hitung() dengan a=5, b=3")
hasil_jumlah, hasil_kurang = hitung(a, b)
