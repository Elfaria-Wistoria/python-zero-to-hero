# Uji pemahaman dictionary

# buat data pakai list
data_list = ['ucup','otong','dudung'] #data list
print(data_list[0]) # mengambil index (0) -->'ucup'

# Dict: pakai key
data_dict = {
  'key': 'value',
  'ed': 'Edwinsyah',
  'mmt': 'mamat',
  'ang': 'angga',
  'list': data_list
}

print(data_dict['ed']) #memanggil seperti indexing
print(data_dict['list']) # --> bisa mengisi list di dictionary


#Add a new data
kamus = {"sapi": "cow"}
print(f"before I add a data : {kamus}\n")
kamus["kucing"] = "cat"
print(f"after I added a new data : {kamus}\n")

#change of modify the data
kamus = {"sapi": "cow", "kucing": "cat"}
kamus["kucing"] = "kitty"
print(f"After I changed the cat from 'cat' to 'kitty' --> {kamus}\n")

#Delete the data
kamus = {"sapi": "cow", "kucing": "kitty"}
print(f"Before I delete the data : {kamus}\n")
del kamus["sapi"]
print(f"After I deleted the data : {kamus}\n")

#check the key.
print(f"The data : {kamus}\n")
print(f"is the sapi there? : {"sapi" in kamus}\n")
print(f"is the kucing there? : {"kucing" in kamus}\n")

#Looping the dictionary
kamus = {"sapi": "cow", "kucing": "kitty"}

for key, value in kamus.items():
  print(f"key : {key, "value :" ,value}\n")


data_dict = {
  "cup" :"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung"
}

#Check the length of a dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary : {LENDICT}")

#Check the key of a dictionary
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict : {CHECKKEY}")

#Access the value
print(data_dict["cup"])       # cara biasa
print(data_dict.get("cup"))   # cara aman
print(data_dict.get("kis","key tidak ditemukan"))
# Output: key tidak ditemukan

#Update the Data
data_dict["cup"] = "icip siriting"
print(data_dict)

#adding a new key
data_dict["ed"] = "edwinsyah"
print(data_dict)

#update data with update()
data_dict.update({"cup":"ucup surucup"})
print(data_dict)
# Kalau key ada → value diganti.
# Kalau key belum ada → key baru ditambahkan.

data_dict.update({"faqih":"faqihza si kweren"})
print(data_dict)

del data_dict ["faqih"]
print(data_dict)

# Ringkasan Cepat

# len(dict) → jumlah data

# key in dict → cek key ada/tidak

# dict["key"] → ambil value (error kalau tidak ada)

# dict.get("key","default") → ambil value (aman)

# dict["key"] = value → tambah / ubah data

# dict.update({...}) → tambah / ubah banyak data

# del dict["key"] → hapus data
