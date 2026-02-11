#A. INHERITANCE(pewarisan)
#1. Buatlah class induk bernama:
class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk  #menyimpan nilai ke dalam atribut objek
        self.harga = harga

    def info_produk(self):  #menampilkan informasi produk.
        print('barang tersedia')

#2. buatlah class turunan 
#.ProdukElektronik
# CLASS INDUK
class ProdukElektronika(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi

    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga} dengan garansi {self.garansi} tahun"

#b. ProdukMakanan 
#class induk 
class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        print(f"{self.nama_produk} seharga {self.harga} kadaluarsa {self.tanggal_kadaluarsa}")
    
#class  turunan : produk makanan 
class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        print(f"{self.nama_produk} seharga {self.harga} kadaluarsa {self.tanggal_kadaluarsa}")


#B.POLYMORPHISM
#3. Buatlah class:
#Notifikasi 
class Notifikasi:
    def __init__(self,pesan):
        self.pesan=pesan

        def kirim(self):
            print('notifikasi baru')
#4. KELAS TURUNAN
class  Email(Notifikasi):
    def __init__(self,pesan):
        super().__init__(pesan)

    def kirim(self):
        print("Mengirim notifikasi melalui Email")

class SMS:
    def __init__(self, pesan):
        self.pesan = pesan

    def kirim(self):
        print("Mengirim notifikasi melalui SMS")


#C.ENCAPSULATION
#5. Buatlah class:
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        
        if nilai < 0 or nilai > 100:
            print("Nilai tidak valid, diubah menjadi 0")
            self.nilai = 0
        else:
            self.nilai = nilai

    def get_nilai(self):
        return self.nilai

