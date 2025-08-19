import os



def header():
    '''fungsi Header'''
    os.system("clear")
    # os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
  '''fungsi input dari users'''
  lebar = int(input("Masukan Nilai Lebar : "))
  panjang = int(input("Masukan Nilai Panjang : "))
  return lebar,panjang

def hitung_luas(panjang,lebar):
  '''fungsi menghitung luas'''
  return lebar*panjang

def hitung_keliling(panjang,lebar):
  '''fungsi menghitung keliling'''
  return 2 * (lebar + panjang)

def display(pesan,nilai):
  '''fungsi menampilkan hasil'''
  print(f"hasil perhitungan {pesan} = {nilai}")

while True:
  header()
  LEBAR,PANJANG = input_user()
  LUAS = hitung_luas(LEBAR,PANJANG)
  KELILING = hitung_keliling(LEBAR,PANJANG)

  display("Luas", LUAS)
  display("Keliling", KELILING)

  is_lanjut = input("Apakah lanjut (y/n) ? : ")
  if is_lanjut == "n":
    break
print("Program Selesai, Terimakasih")
