'''''
 Kata "polimorfisme" berarti "banyak bentuk", dan dalam pemrograman, ini merujuk pada metode/fungsi/operator dengan nama yang sama yang dapat dieksekusi pada banyak objek atau kelas.
'''''

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

#
class person:
  def __init__(self, name,age):
    self.name = name
    self.__age =age

def getAge(self):
  return self.__age

  def setAge(self, newAge):
        self.__age = newAge   

# Membuat objek
p1 = getAge("Syifa", 20)
print("Nama :", p1.name)
print("Umur sebelum diubah :", p1.getAge())

# Mengubah umur menggunakan setter
p1.setAge(15)

print("Umur setelah diubah :", p1.getAge())