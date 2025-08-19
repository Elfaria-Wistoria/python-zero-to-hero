# membuat sebuah fungsi

def tambah(nilai_1,nilai_2):
  return nilai_1 + nilai_2

def kali(nilai_1,nilai_2):
  hasil = nilai_1 * nilai_2
  return hasil

x = tambah(5,5)
y = kali(5,5)
print(x)
print(y)

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")
