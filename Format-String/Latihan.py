nama_produk = input("Masukan nama produk : ")
harga_produk = float(input("Masukan Harga Produk Yang Anda Beli : "))
jumlah_produk = int(input("Masukan Jumlah Produk Yang Anda Beli : "))

# Total harga
total_harga = harga_produk * jumlah_produk

# Hitung diskon
diskon = 0.10  # 10%
potongan = total_harga * diskon
harga_akhir = total_harga - potongan

# Output utama
print(f"\nNama produk  : {nama_produk}")
print(f"Harga satuan : Rp.{harga_produk:,.2f}")
print(f"Jumlah       : {jumlah_produk}")
print(f"Total harga  : Rp.{total_harga:,.2f}")

# Format angka lain
print(f"\nBinary       : {bin(int(total_harga))}")
print(f"Octal        : {oct(int(total_harga))}")
print(f"Hexadecimal  : {hex(int(total_harga))}")

# Diskon
print(f"\nDiskon       : {diskon:.0%} (Rp.{potongan:,.2f})")
print(f"Harga akhir  : Rp.{harga_akhir:,.2f}")
