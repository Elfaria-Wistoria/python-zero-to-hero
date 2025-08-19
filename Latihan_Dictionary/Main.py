# Latihan Dictionary
import os
import string
import random

data_template = {
  'nama':'nama',
  'umur':'umur',
  'alamat':'alamat'
}

data_peserta ={}

while True:
  os.system('clear')
  print(f"{'SELAMAT DATANG':^20}")
  print(f"{'PARA MAHASISWA':^20}")
  print(f"{'-' * 20}")

  peserta = dict.fromkeys(data_peserta.keys())

  peserta['nama'] = input("Masukan Nama Peserta\t: ")
  peserta['umur'] = int(input("Masukan Umur Peserta\t: "))
  peserta['alamat'] = input("Masukan Alamat Peserta\t: ")

  KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
  data_peserta.update({KEY:peserta})

  print(f"{'KEY':<6}\t {'Nama':<10} {'Umur':^5}\t {'Alamat':^18}")
  print("-"*56)
  for peserta in data_peserta:
    KEY = peserta
    NAMA = data_peserta[KEY]['nama']
    UMUR = data_peserta[KEY]['umur']
    ALAMAT = data_peserta[KEY]['alamat']
    print(f"{KEY:<6}\t {NAMA:<10} {UMUR:^5}\t {ALAMAT:^18}")
    print("-"*56)

  print("\n")
  is_lanjut = input("Apakah sudah selesai ? (y/n) : ")
  if is_lanjut == 'y':
    break

print("TERIMAKASIH")
