'''
Enkapsulasi adalah tentang melindungi data di dalam sebuah kelas.Artinya, data (properti) dan metode disimpan bersama dalam satu kelas, sambil mengontrol bagaimana data tersebut dapat diakses dari luar kelas. 
Hal ini mencegah perubahan yang tidak disengaja pada data Anda dan menyembunyikan detail internal tentang cara kerja kelas Anda.
-Catatan: Garis bawah tunggal _hanyalah konvensi. Ini memberi tahu programmer lain bahwa properti tersebut ditujukan untuk penggunaan internal, tetapi Python tidak memberlakukan batasan ini.
'''

#buat metode privat:
class Calculator:
  def __init__(self):  #tidak bisa di akses di luar 
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error


'''
Name mangling adalah cara Python mengimplementasikan properti dan metode privat.
Saat Anda menggunakan garis bawah ganda __, Python secara otomatis mengubah namanya secara internal dengan menambahkan _ClassNamedi depannya.Misalnya, __agemenjadi _Person__age.
'''
#metod mangling
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!