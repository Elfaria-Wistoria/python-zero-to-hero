'''global dan lokal scope pada python'''

#GLOBAL SCOPE
nilai = 0 # Global Scope

def fungsi():
  print(f"Nilai dari variabel nilai adalah : {nilai}")

fungsi()

#Global scope juga bisa di pakai untuk for and if

for i in range(0,6):
  print(f"Looping {i} - {nilai}")

if True:
  print(f"Menampilkan global {nilai}")


#LOCAL SCOPE
def fungsi2():
  lokal = 1
  print(f"Nilai lokal : {lokal}")

fungsi2()
#print(lokal) # tidak bisa karena variable lokal adalah local scope


#Cara membuat local scope menjadi global scope
def fungsi3():
  global convert
  convert = 2
  print(f"Ini adalah convert : {convert}")


fungsi3()
print(f"Mengeprint convert : {convert}")
