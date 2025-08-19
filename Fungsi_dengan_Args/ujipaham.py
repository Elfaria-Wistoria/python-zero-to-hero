
import string
'''Uji pemahaman'''
def hitung(*args: int) -> int:
  nilai = 0
  for i in args:
    nilai += i # args = args + 1 setiap putaran
  return nilai

x = hitung(1,2,3,4,5,6,7,8)
print(f"nilai yang di kembalikan {x + 2}")


def fungsi(*args):
  nama = args[0]
  umur = args[1]
  kelas= args[2]

  print(f"Bro bernama {nama} berumur {umur} tahun, dan berada di kelas {kelas} saat ini.")

fungsi('otong', 22, 3)
