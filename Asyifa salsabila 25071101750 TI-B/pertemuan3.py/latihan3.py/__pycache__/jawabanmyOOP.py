import myOOP

y = myOOP.ProdukElektronika("TV","3.000.000",2)
y.info_produk()

x = myOOP.ProdukMakanan("Roti","15.000","12-12-2026")
x.info_produk()

a = myOOP.Email("Email terkirim")
a.kirim()

a = myOOP.SMS("SMS terkirim")
a.kirim()

z = myOOP.Mahasiswa("asyifa",-95)
print(z.get_nilai())