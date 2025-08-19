'''Belajar Kwargs'''

def tes(*args): # args menghasilkan tuple
  print(args)

tes("ucup",22,"baik hati")

def fungsi(**kwargs): # kwargs menghasilkan dictionary
  print(kwargs)

fungsi(nama = "edwin", umur = 22)


def keren(*args,**kwargs):
  if kwargs["nama"] == "setuju":
    print("hello World")
  else:
    print("kamu jelek")
  return kwargs


keren(nama = "setuju")



def math(*args, **kwargs):
  hasil = 0
  if kwargs["option"] == "tambah":
    for i in args:
      hasil += i
  elif kwargs["option"] == "kali":
    hasil = 1
    for i in args:
      hasil *= i
  else:
    print("Tidak ada operasi. Maaf yah")

  return hasil

hasil = math(1,2,3,4, option = "tambah")
print(f"Hasil dari penjumlahan = {hasil}")

hasil = math(1,2,3,4, option = "kali")
print(f"Hasil dari perkalian = {hasil}")

