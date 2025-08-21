'''belajar menggunakan try and except'''
'''
try:
    # kode yang mungkin error
except:
    # kode kalau error terjadi
'''

# try:
#   hasil = 10/0
#   print(hasil)
# except:
#   print("Gabisa di bagi tong! pembagi nol!")

# import os

# while True:
#   os.system("clear")
#   try:
#     angka_1 = int(input("Masukan angka 1 = "))
#     angka_2 = int(input("Masukan angka 2 = "))
#     hasil = angka_1 / angka_2
#     print(f"Hasilnya dari pembagian {angka_1} dan {angka_2} = {hasil}")

#     is_lanjut = input("Lanjutkan (y/n) ? : ")
#     if is_lanjut == 'n':
#       break
#   except ZeroDivisionError:
#     print(f"❌ Error: Tidak boleh bagi 0.")
#     break
#   except ValueError:
#     print("❌ Error: Input harus angka.")
#     break

# # File Handling
# try:
#   with open("data.txt", 'r', encoding='utf-8') as f:
#     print(f.read())
# except:
#   print(f"Data tidak di temukan, membuat file baru.....")
#   with open("data.txt", 'w', encoding='utf-8') as f:
#     f.write("Hallo ini data baru")
#   with open("data.txt", 'r', encoding="utf-8") as f:
#     print(f.read())

# else → jalan kalau tidak ada error.
try:
  angka = 5
  hasil = angka / 2
except ZeroDivisionError:
  print("gabisa di bagi 0 bang.")
else:
  print(f"Hasilnya adalah = {hasil}")

try:
  with open("data.txt", 'r', encoding="utf-8") as f:
    print(f"isi dari data.txt adalah : {f.read()}")
except FileNotFoundError:
  print(f"file tidak ada bang")
finally:
  print(f"Program nya kelar bang")

