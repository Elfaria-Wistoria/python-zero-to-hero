#Latihan sesuai video youtube
import datetime as dt
import os
import string
import random

mahasiswa_template = { # template data dict
  'nama': 'nama',
  'nim': '000000000000',
  'sks_lulus': 0,
  'lahir': dt.datetime(1111,1,11)
}

data_mahasiswa = {}
while True:
  os.system('clear')
  print(f"{'SELAMAT DATANG':^20}")
  print(f"{'PARA MAHASISWA':^20}")
  print(f"{'-' * 20}")

  mahasiwa = dict.fromkeys(mahasiswa_template.keys())
  mahasiwa['nama'] = input("Nama Anda\t: ")
  mahasiwa['nim'] = input("Nim Anda\t: ")
  mahasiwa['sks_lulus'] = int(input("Sks Lulus\t: "))
  TAHUN_LAHIR = int(input("Tahun Lahir (yyyy)\t: "))
  BULAN_LAHIR = int(input("Bulan Lahir (1-12)\t: "))
  TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31)\t: "))
  mahasiwa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

  KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
  data_mahasiswa.update({KEY:mahasiwa})

  print(f"{'KEY':<6} {'Nama':<15} {'Nim':^5} {'SkS':^8} {'Lahir':^10}")
  print("-"*56)
  for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<15} {NIM:^5} {SKS:^8} {LAHIR:^10}")
    print("-"*56)

  print("\n")
  is_done = input("Tambah data baru ? (y/n) : ")
  if is_done == "n":
    break

print("\nAkhir dari program")
