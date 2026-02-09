# List angka favorit
angka_favorit = [3, 7, 9, 12, 15]

# 1. For loop biasa
print("=== For loop biasa ===")
for angka in angka_favorit:
    print("Angka:", angka)

# 2. For loop dengan break
print("\n=== For loop dengan break ===")
for angka in angka_favorit:
    print("Cek angka:", angka)
    if angka == 9:
        print("Ketemu angka 9, keluar loop!")
        break

# 3. For loop dengan continue
print("\n=== For loop dengan continue ===")
for angka in angka_favorit:
    if angka % 2 == 0:
        print("Lewati angka genap:", angka)
        continue
    print("Angka ganjil:", angka)

# 4. While loop (Tebak angka)
print("\n=== While loop Tebak angka ===")
tebakan = 0
target = 5
while tebakan != target:
    tebakan += 1
    if tebakan < target:
        print("Tebakan", tebakan, "terlalu kecil")
    elif tebakan > target:
        print("Tebakan", tebakan, "terlalu besar")
    else:
        print("Tebakan", tebakan, "benar!")
        break
