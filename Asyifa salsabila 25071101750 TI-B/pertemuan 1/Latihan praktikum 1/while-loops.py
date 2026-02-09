#while  loops
# Program: Mencetak angka dari 1 sampai 10, tapi berhenti di angka tertentu

i = 1
batas = 7  # Angka dimana perulangan berhenti

print("=== Program Perulangan Sederhana ===")
print(f"Akan mencetak angka dari {i} sampai {batas}")
print("Perulangan akan berhenti jika mencapai batas.\n")

while i <= 10:
    print(f"Angka sekarang: {i}")
    
    if i == batas:
        print(f"Berhenti! Angka sudah mencapai batas ({batas})")
        break  # Hentikan perulangan
    
    if i % 2 == 0:
        print(f"{i} adalah angka genap")
    else:
        print(f"{i} adalah angka ganjil")
    
    i += 1  # Tambah nilai i
    print("Lanjut ke angka berikutnya...\n")

print("Perulangan selesai. Terima kasih!")


#for loops
# Daftar buah
fruits = ["apple", "banana", "cherry", "mango", "kiwi", "orange"]

print("=== Daftar Buah ===")
print("Kita akan memeriksa setiap buah di daftar.\n")

for fruit in fruits:
    print(f"Buah saat ini: {fruit}")
    
    # Cek panjang nama buah
    if len(fruit) > 5:
        print(f"{fruit} memiliki nama panjang.")
    else:
        print(f"{fruit} memiliki nama pendek.")
    
    # Cek apakah buahnya mengandung huruf 'a'
    if "a" in fruit:
        print(f"{fruit} mengandung huruf 'a'.")
    else:
        print(f"{fruit} tidak mengandung huruf 'a'.")
    
    print("------")  # pemisah antar buah

print("Selesai memeriksa semua buah!")
 
