print(f'{20*"=="} \nWelcome to my fucking calculator\n{20*"=="}')

angka_1 = float(input("Masukan angka pertama\t\t: "))
operator = input("Masukan operator (+ - * / %)\t: ")
angka_2 = float(input("Masukan angka kedua\t\t: "))

if operator == "+":
  tambah = angka_1 + angka_2
  print(f'{20*"=="}')
  print(f"Hasilnya adalah -->  {int(tambah)}")
elif operator == "-":
  kurang = angka_1 - angka_2
  print(f'{20*"=="}')
  print(f"Hasilnya adalah -->  {int(kurang)}")
elif operator == "*":
  kali = angka_1 * angka_2
  print(f'{20*"=="}')
  print(f"Hasilnya adalah -->  {int(kali)}")
elif operator == "/":
  bagi = angka_1 / angka_2
  print(f'{20*"=="}')
  print(f"Hasilnya adalah -->  {int(bagi)}")
elif operator == "%":
  modulus = angka_1 % angka_2
  print(f'{20*"=="}')
  print(f"Hasilnya adalah -->  {int(modulus)}")

print(f'{20*"=="} \nProgram selesai, terimakasih banyak!\n{20*"=="}')
