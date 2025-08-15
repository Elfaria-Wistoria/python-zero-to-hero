daftar_belanja = []

while True:
    print("\n(1) Tambah barang\n(2) Ubah jumlah barang\n(3) Hapus barang\n(0) Keluar")
    pilihan = input("Silahkan pilih : ")

    if pilihan == "1":
        nama_barang = input("Masukan nama barang\t : ")
        jumlah = int(input("Masukan jumlah barang\t : "))

        data_belanja = [nama_barang, jumlah]
        daftar_belanja.append(data_belanja)

    elif pilihan == "2":
        if not daftar_belanja:
            print("Daftar belanja masih kosong!")
            continue

        print("\nDaftar Belanja:")
        for index, item in enumerate(daftar_belanja, start=1):
            print(f"{index}. {item[0]} - {item[1]}")

        nomor_barang = int(input("Pilih nomor barang yang mau diubah: "))
        if 1 <= nomor_barang <= len(daftar_belanja):
            jumlah_baru = int(input("Masukan jumlah barang terbaru: "))
            daftar_belanja[nomor_barang - 1][1] = jumlah_baru
            print("Jumlah barang berhasil diubah!")
        else:
            print("Nomor barang tidak valid!")

    elif pilihan == "3":
        if not daftar_belanja:
            print("Daftar belanja masih kosong!")
            continue

        print("\nDaftar Belanja:")
        for index, item in enumerate(daftar_belanja, start=1):
            print(f"{index}. {item[0]} - {item[1]}")

        nomor_hapus = int(input("Pilih nomor barang yang mau dihapus: "))
        if 1 <= nomor_hapus <= len(daftar_belanja):
            daftar_belanja.pop(nomor_hapus - 1)
            print("Barang berhasil dihapus!")
        else:
            print("Nomor barang tidak valid!")

    elif pilihan == "0":
        break

    else:
        print("Pilihan tidak valid!")

    # Tampilkan daftar belanja setiap selesai aksi
    print("\n","="*10,"Daftar Belanja","="*10)
    for index, item in enumerate(daftar_belanja, start=1):
        print(f"{index}. {item[0]} - {item[1]}")
    print("="*30)

print("\nPROGRAM SELESAI!")
