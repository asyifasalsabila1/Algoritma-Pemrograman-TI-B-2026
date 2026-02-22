print("=== SISTEM PEMESANAN TIKET BIOSKOP ===")

HARGA_TIKET = 50000

try:
    nama = input("Masukkan nama pembeli: ")
    
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))
    if jumlah_tiket <= 0:
        raise ValueError("Jumlah tiket harus lebih dari 0!")
    
    total_harga = jumlah_tiket * HARGA_TIKET
    print("Total harga: Rp", total_harga)
    
    pembayaran = float(input("Masukkan jumlah pembayaran: "))
    if pembayaran < total_harga:
        raise ValueError("Uang pembayaran kurang!")
    
    kembalian = pembayaran - total_harga
    
    print("\n=== PEMESANAN BERHASIL ===")
    print("Nama:", nama)
    print("Jumlah tiket:", jumlah_tiket)
    print("Total bayar: Rp", pembayaran)
    print("Kembalian: Rp", kembalian)

except ValueError as e:
    print("Terjadi kesalahan:", e)
except Exception as e:
    print("Error tidak terduga:", e)
finally:
    print("\nTerima kasih telah memesan tiket.")

