'''
Kelas dalam (inner class) adalah kelas yang didefinisikan di dalam kelas lain. Kelas dalam dapat mengakses properti dan metode dari kelas luar (outer class).
Kelas dalam (inner class) berguna untuk mengelompokkan kelas yang hanya digunakan di satu tempat, sehingga kode Anda menjadi lebih terorganisir.
'''

#Buat kelas dalam (inner class):

class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)


#Akses kelas dalam dan buat objek:

class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()

#Teruskan instance kelas luar ke kelas dalam:

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()


#Gunakan kelas dalam (inner class) untuk merepresentasikan mesin mobil:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()


#Gunakan kelas dalam (inner class) untuk merepresentasikan mesin mobil: