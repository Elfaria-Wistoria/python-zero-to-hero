#Latihan Nested List

print(f"{"==" * 5} Latihan Nested List! {"==" * 5}")

print(f"{"==" * 5} Tugas 1 {"==" * 5}")
angka_genap = [2, 4, 6]
angka_ganjil = [1, 3, 5]

list_angka = [angka_genap,angka_ganjil]
print(f"List angka 2D : {list_angka}")
print(f"Angka 6 dari list : {angka_genap[2]}")
print(f"Angka 3 dari list : {angka_ganjil[1]}")


print(f"{"==" * 5} Tugas 2 {"==" * 5}\n")
peserta1 = ["edwinsyah", 22, "sorong"]
peserta2 = ["gunawan", 23, "sorong"]
peserta3 = ["nita", 20, "sorong"]
peserta4 = ["samantha", 20, "sorong"]

peserta = [peserta1, peserta2, peserta3, peserta4]

for data_peserta in peserta:
  print(f"Nama\t : {data_peserta[0]}")
  print(f"Umur\t : {data_peserta[1]}")
  print(f"Kota\t : {data_peserta[2]}\n")

print(f"Cetak nama saja\n")
for data_nama in peserta:
  print(f"Nama\t : {data_nama[0]}\n")

print(f"Cetak peserta yang umurnya 20 keatas\n")
for data_peserta in peserta:
  if data_peserta[1] > 20:
    print(f"Nama\t : {data_peserta[0]}")
    print(f"Umur\t : {data_peserta[1]}")
    print(f"Kota\t : {data_peserta[2]}\n")


print(f"{"==" * 5} Tugas 3 {"==" * 5}\n")

peserta1 = ["edwinsyah", 22, "sorong"]
peserta2 = ["gunawan", 23, "sorong"]
peserta3 = ["nita", 20, "sorong"]
peserta4 = ["samantha", 20, "sorong"]

peserta = [peserta1, peserta2, peserta3, peserta4]

list_copy = peserta.copy()
print(f"List hasil copy : {list_copy}\n")
peserta1[0] = "Michael"
print(f"List hasil ganti nama\t: {list_copy}\n")
print(f"List peserta\t: {peserta}\n")

#peserta ikut berubah karena id adress nya sama
print(f"{"==" * 5} Pakai Deepcopy {"==" * 5}\n")
import copy as cp

list_deep_copy = cp.deepcopy(peserta)
print(f"Hasil Deep Copy : {list_deep_copy}\n")
peserta2[1] = 99
print(f"List peserta\t: {peserta}\n")
print(f"List hasil ganti umur\t: {list_deep_copy}\n")
