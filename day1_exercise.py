# Variabel dan print()
name = "Edwin"        # Menyimpan teks (string)
age = 25              # Menyimpan angka bulat (integer)
is_founder = True     # Menyimpan nilai boolean (True/False)

print(f"Name: {name}, Age: {age}, Founder: {is_founder}")


#Tipe Data Dasar
# String (teks)
text = "AI Startup"

# Integer (angka bulat)
year = 2025

# Float (angka desimal)
growth = 12.5

# Boolean (True/False)
is_scaling = True


startup = "DeepAI"
founded_year = 2025
print(startup + " was founded in " + str(founded_year))
#str() digunakan untuk mengubah angka jadi string.



# List, Tuple, Dictionary, Set
#Ini adalah struktur data untuk menyimpan banyak nilai.

# List (urutan data, bisa diubah)
languages = ["Python", "JavaScript", "Go"]   # isi rak awal
print(languages[0])  # ambil barang di rak nomor 0 → "Python"
languages.append("Rust")  # tambah barang "Rust" di ujung rak
print(languages)          # lihat isi rak sekarang


#Tuple (urutan data, tidak bisa diubah)
startup = ("DeepAI", 2025)
print(startup[0])

#Dictionary (key → value)
founder = {"name": "Edwin", "role": "CEO"}
print(founder["name"])

#Set (data unik, tidak ada duplikat)
unique_users = {"alice", "bob"}
unique_users.add("charlie")
print(unique_users)


#Control Flow (Percabangan & Perulangan)
users = ["Alice", "Bob", "Charlie"]

for user in users:
    print(f"Welcome {user}")


#Fungsi
#Fungsi = blok kode yang bisa dipanggil berulang.
def greet(name):
    return f"Hello, {name}!"

print(greet("Edwin"))

