'''
Pewarisan memungkinkan kita untuk mendefinisikan sebuah kelas yang mewarisi semua metode dan properti dari kelas lain.Kelas induk adalah kelas yang diwarisi, juga disebut kelas dasar.Kelas anak adalah kelas yang mewarisi dari kelas lain, juga di sebut kelas turunan 
'''

#Buat kelas bernama person
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()
#penjelasan 
class Student(Person): #menjelaskan kelas strudent yang mewakili person kelas
     def __init__(self, nama, gender,age):
        selfnama=nama
        selfgender=gender
        selfage=age

     def walking():
              pass
     def talking():
                 pass
     def sleep():
          pass
     def human():
          
          #2
          class student():
              def __init__(self,nama,gender,age):
                  super().__init__(self,nama,gender,age)   #bisa mengakekses semua punya indu ny krn pakai 
                  self.birthyear =2006    #hanya di punyai kelas turunan


                  x = student("syifa,girl,20")
                  print(x.nama)
                  print(x.birthyear)

#contoh inheritance 1 yang terakhir
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()
