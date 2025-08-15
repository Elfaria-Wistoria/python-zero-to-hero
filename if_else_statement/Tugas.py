#Latihan

nama = input("Masukan nama anda   : ")
nilai = float(input("Masukan nilai anda  :"))

if nilai >= 90:
  print(f"Selamat {nama}, kamu lulus dengan nilai A!")
elif nilai >= 75:
  print(f"Bagus {nama}, kamu lulus dengan nilai B!")
elif nilai >= 60:
  print(f"Cukup {nama}, kamu lulus dengan nilai C.")
else:
  print(f"Maaf {nama}, kamu tidak lulus.")

if nilai >= 85:
  print(f"Kamu mendapatkan kartu diskon 20% di toko buku.")

print(f"Program Selesai!")
