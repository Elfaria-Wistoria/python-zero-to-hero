depan = "edwin"
tengah = "syah"
belakang = "umasugi"

nama_saya = depan + " " + tengah + " " + belakang
print(f"{nama_saya}")

print(f"{len(nama_saya)}")

status = "a" in nama_saya
print(f"Apakah ada 'a' di dalam {nama_saya} : {status}")

print(f"karakter pertama  : {nama_saya[0]}")
print(f"karakter Ketiga   : {nama_saya[2]}")
print(f"karakter terakhir : {nama_saya[-1]}")

print((nama_saya + " ") * 5)

print(f"karakter terkecil : {min(nama_saya)}")
print(f"karakter terbesar : {max(nama_saya)}")
print(f"huruf \"e\" keluar sebanyak : {nama_saya.count("e")}x")
