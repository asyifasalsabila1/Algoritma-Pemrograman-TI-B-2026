cars = ["Ford", "Volvo", "BMW"]
#berapa banyak anggota dari variabel 

x = cars[0]
cars[0] = "Toyota"

#length
x = len(cars)       #len()

#adding array element==============
cars.append("Honda")   #append artinya menambahkan

for x in cars:     #for in artinya  
  print(x)

cars.pop(1)      #pop (keluar)

cars.remove("Volvo")  #remov(menghilangkan /menghapus)
#clear menghapus semua elemen 
#copy memberi salinan dari salinan
#cound ada berapa dalam 
#extend menambahkan 1 list tp tambh 1slot lg
#iter mengeprint semua element 


conoth 
# Membuat list
fruits = ['apel', 'pisang', 'jeruk']

# Menambahkan elemen baru
fruits.append('mangga')

print(fruits)

# Menghapus elemen terakhir
last_fruit = fruits.pop()
print("Yang dihapus:", last_fruit)
print(fruits)