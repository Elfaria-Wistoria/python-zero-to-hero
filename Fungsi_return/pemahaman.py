# contoh print (tanpa return)
def tambah_print(a, b):
    print(a + b)

# contoh return
def tambah_return(a, b):
    return a + b

# coba panggil
x = tambah_print(3, 4)
print("Nilai x:", x)   # x = None, tidak bisa dipakai

y = tambah_return(3, 4)
print("Nilai y:", y)   # y = 7, bisa dipakai lagi
print("y * 2 =", y * 2) # bisa diproses lagi → 14
