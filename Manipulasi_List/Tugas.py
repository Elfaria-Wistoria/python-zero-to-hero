# #Tugas-1
# # 0,1,2,3,4 | -1 -2 -3 -4 -5
# print(f"\n{"==" * 5} Tugas Dasar Indexing & Slicing {"==" * 5}" )
# teman = ["gunawan", "ubai", "awal", "kifli", "nita"]

# print(f"Elemen Pertama : {teman[0]}\nElemen Kedua\t : {teman[-1]}\nElemen Ketiga Dari Delakang : {teman[-3]}\n")

# #Tugas-2
# print(f"{"==" * 5} Tugas Manipulasi Data {"==" * 5}" )

# teman.append("angga")
# teman.append("rahmat")
# teman.insert(1, "edwin")

# teman[3] = "awaludin"

# teman.remove("nita")
# teman.pop()

# print(f"Result akhir tugas-2 : \n{teman}\n")

# # Tugas-3
# print(f"{"==" * 5} Tugas List dengan Data Campuran {"==" * 5}" )

# list_campuran = ["edwinsyah", 23, True]
# list_lain = ["sorong", 99, False]
# list_campuran[1] = 33
# list_campuran.insert(1, "umasugi")
# list_campuran.extend(list_lain)

# print(f"Result akhri tugas-3 : \n{list_campuran}\n")


# #Mini Project Challenge

# bahan = ["Telur", "Gula", "Tepung"]

# print(f"Ini adalah list bahan anda saat ini : \n{bahan}")

# pilihan = int(input("mau mengedit ?\n 0 = tidak\n 1 = tambah bahan\n 2 = hapus bahan\n Pilihan anda : "))

# if pilihan == 1:
#   bahan_baru = str(input("Nama bahan : "))
#   bahan_baru = [bahan_baru]
#   bahan.extend(bahan_baru)
#   print(f"Daftar bahan anda sekarang : {bahan}")

# elif pilihan == 2:
#     bahan_hapus = input("Bahan apa yang ingin anda hapus : ")
#     if bahan_hapus in bahan:  # cek dulu biar tidak error
#         bahan.remove(bahan_hapus)
#         print(f"bahan anda saat ini : {bahan}")
#     else:
#         print("Bahan tidak ditemukan di daftar.")

# elif pilihan == 0:
#   print(f"Terimakasih")

# else:
#   print(f"program error")

# print(f"program selesai!")



#mini project hasil dari gpt
bahan = ["Telur", "Gula", "Tepung"]

while True:
    print(f"\nDaftar bahan saat ini: {bahan}")
    pilihan = input("Pilih aksi: 1 = tambah, 2 = hapus, 0 = keluar\n> ")

    if pilihan == "1":
        bahan_baru = input("Nama bahan baru: ")
        bahan.append(bahan_baru)
    elif pilihan == "2":
        bahan_hapus = input("Bahan yang ingin dihapus: ")
        if bahan_hapus in bahan:
            bahan.remove(bahan_hapus)
        else:
            print("Bahan tidak ditemukan!")
    elif pilihan == "0":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
