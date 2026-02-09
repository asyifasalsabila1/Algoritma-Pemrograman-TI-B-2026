#1
#operator arithmetic 
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)


#operstor logical
umur = 25
punya_sim = True

print("Umur:", umur)
print("Punya SIM:", punya_sim)

# Cek apakah boleh mengendarai kendaraan
boleh_mengemudi = (umur >= 18 and umur <= 60) and punya_sim

print("Boleh mengemudi:", boleh_mengemudi)

# Cek kondisi lain
print("Umur terlalu muda atau terlalu tua:",
      umur < 18 or umur > 60)

# Menggunakan operator NOT
print("Tidak punya SIM:",
      not punya_sim)


#operator  identity
data1 = ["pensil", "pulpen", "penghapus"]
data2 = ["pensil", "pulpen", "penghapus"]
data3 = data1

print("Data awal:")
print("data1:", data1)
print("data2:", data2)
print("data3:", data3)

print("\nHasil perbandingan:")
print("data1 is data3:", data1 is data3)   # True (objek sama)
print("data1 is data2:", data1 is data2)   # False (objek berbeda)
print("data1 == data2:", data1 == data2)   # True (isi sama)

# Mengubah isi data3
data3.append("penggaris")

print("\nSetelah data3 diubah:")
print("data1:", data1)
print("data2:", data2)
print("data3:", data3)

print("\nPerbandingan setelah perubahan:")
print("data1 is data3:", data1 is data3)
print("data1 == data2:", data1 == data2)



#2
# Arithmetic
a, b = 10, 3
print("Arithmetic:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print()

# Assignment
x = 5
x += 2
print("Assignment:")
print("x += 2 ->", x)
x *= 3
print("x *= 3 ->", x)
print()

# Comparison
print("Comparison:")
print("a == b:", a == b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print()

# Logical
p, q = True, False
print("Logical:")
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print()

# Identity
list1 = [1,2]
list2 = list1
list3 = [1,2]
print("Identity:")
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print()

# Membership
fruits = ["apple","banana"]
print("Membership:")
print("'apple' in fruits:", 'apple' in fruits)
print("'orange' not in fruits:", 'orange' not in fruits)
print()

# Bitwise
a, b = 6, 3
print("Bitwise:")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
print()

# Precedence
print("Precedence:")
print("3 + 2 * 4 ** 2 =", 3 + 2 * 4 ** 2)
print("(3 + 2) * 4 ** 2 =", (3 + 2) * 4 ** 2)
