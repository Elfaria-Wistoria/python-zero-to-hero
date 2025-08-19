# lambda argument: ekspresi
# def = panjang, jelas, cocok untuk fungsi kompleks.
# lambda = singkat, cocok untuk fungsi sekali pakai.

# # fungsi biasa
# def kuadrat(angka):
#     return angka**2

# print(kuadrat(3))   # 9

# # fungsi lambda (lebih singkat)
# kuadrat = lambda angka: angka**2 # lambda argument: ekspresi
# print(kuadrat(3))   # 9

# coba = lambda nilai_1,nilai_2: nilai_1+nilai_2 + 5
# print(f"Hasilnya adalah : {coba(5,5)}")

# def pangkat(*args):
#   hasil = 1
#   for i in args:
#     hasil *= i **2 #hasil = hasil * i
#   print(hasil)
#   return hasil

# print(f"Hasil dari penggunaan args = {pangkat(8)}")

# '''Lambda dengan 2 argumen'''
# pangkat = lambda num, pow: num**pow
# print(f"Hasil dari penggunaan lamda 2 argumen : {pangkat(2,2)}")


#Kenapa butuh lambda?
#Karena sering dipakai di dalam fungsi lain, contohnya sort atau filter.

#sort biasa tanpa lambda
nilai = [1,2,3,4,5,6,7,8,9,10] #data list

nilai.sort()
print(nilai)

#sort string biasa tanpa lambda
huruf = ["ucup", "ahmad", "adi"] #data list
huruf.sort(key=lambda nama: len(nama))
print(huruf)

nilai = [1,2,3,4,5,6,7,8,9,10] #data list

kecil = list(filter(lambda x: x < 5, nilai))
print(kecil)
