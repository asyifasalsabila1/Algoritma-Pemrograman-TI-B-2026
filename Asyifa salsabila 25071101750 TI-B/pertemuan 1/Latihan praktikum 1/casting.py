'''
melengkapi
'''

string = '1'

string_to_numbers = int(string)

print (type (string))
print (type (string_to_numbers))

#2
a = int(5.9)     # akan dibulatkan ke bawah menjadi 5
b = int("10")    # string "10" menjadi integer 10
c = int(True)    # boolean True menjadi 1

print(a)
print(b)
print(c)


#3
# Integer (int)
x = int(5)           # dari int → int tetap 5
y = int(3.7)         # dari float → int akan dibulatkan ke bawah (3)
z = int("10")        # dari string → int 10
# print tipe data
print(x, y, z)
print(type(x), type(y), type(z))

# Float
a = float(5)         # dari int → float 5.0
b = float("3.14")    # dari string → float 3.14
c = float(2 + 3j)    # dari complex → float tidak bisa langsung, ini akan error jika dijalankan
# print(a, b)
print(a, b)
print(type(a), type(b))

# String
s1 = str(5)           # int → string "5"
s2 = str(3.7)         # float → string "3.7"
s3 = str(2 + 3j)      # complex → string "(2+3j)"
print(s1, s2, s3)
print(type(s1), type(s2), type(s3))

# Complex
c1 = complex(5)       # int → complex (5+0j)
c2 = complex(3.7)     # float → complex (3.7+0j)
c3 = complex("2+3j")  # string → complex (2+3j)
print(c1, c2, c3)
print(type(c1), type(c2), type(c3))

