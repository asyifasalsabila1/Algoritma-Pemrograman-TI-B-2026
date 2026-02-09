mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))    #me nevt  kan kalau mau print buat selanjut nya wajib pakai next 
print(next(myit))

#contoh 
# List biasa
my_list = [10, 20, 30]

# Membuat iterator
my_iter = iter(my_list)

# Mengakses elemen satu per satu
print(next(my_iter))  # Output: 10
print(next(my_iter))  # Output: 20
print(next(my_iter))  # Output: 30

# Kalau next lagi, StopIteration akan muncul
# print(next(my_iter))  # StopIteration