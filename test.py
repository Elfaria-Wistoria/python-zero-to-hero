'''Membuat fungsi daftar nama mahasiswa'''
import string
import os

# def input_data(*args):
#   nama = input("Masukan nama anda : ")
#   nim = input("Masukan nim anda : ")
#   alamat = input("Masukan alamat anda : ")
#   umur = int(input("Masukan umur anda : "))

#   return nama,nim,alamat,umur


# def data_user():
#   nama = input("Masukan nama anda : ")
#   nim = input("Masukan nim anda : ")
#   alamat = input("Masukan alamat anda : ")
#   umur = int(input("Masukan umur anda : "))

#   return {
#     "nama" : nama,
#     "nim" : nim,
#     "alamat" : alamat,
#     "umur" : umur
#   }

# data_peserta = []

# while True:
#   peserta = data_user()
#   data_peserta.append(peserta)

#   is_lanjut = input("Apakah mau lanjut (y/n) ?")
#   if is_lanjut == "n":
#     break

# print("\nProgram Selesai Bung")
# print("Data Peserta:")
# for idx, p in enumerate(data_peserta, start=1):
#     print(f"{idx}. Nama: {p['nama']}, NIM: {p['nim']}, Alamat: {p['alamat']}, Umur: {p['umur']}")


print(f"\n{'-'*10}HALLO SELAMAT DATANG GUYS{'-'*10}\n")

def belanjaan():
  nama_barang = input("nama barang anda : ")
  jumlah_barang = int(input("jumlah barang anda : "))
  kualitas_barang = input("kualitas barang : ")

  return{
    'nama_barang' : nama_barang,
    'jumlah_barang' : jumlah_barang,
    'kualitas_barang' : kualitas_barang
    }

daftar_barang = []

while True:
  barang = belanjaan()
  daftar_barang.append(barang)

  for index, i in enumerate(daftar_barang, start=1):
    print(f"{index}. Nama : {i['nama_barang']}\n Jumlah Barang : {i['jumlah_barang']}\n Kualitas Barang : {i['kualitas_barang']}")


  is_lanjut = input("ingin menambah barang baru (y/n) ?")
  if is_lanjut == "n":
    break


print("program selesai.")
