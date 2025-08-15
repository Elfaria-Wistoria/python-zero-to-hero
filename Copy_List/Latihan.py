#Latihan copy list

bahan_a = ["Susu", "Beras", "Tepung", "Ikan"]
bahan_b = bahan_a

print(f"Bahan a : {bahan_a}\n")
print(f"Bahan b : {bahan_b}\n")

bahan_a[0] = "Udang"

print(f"Bahan a : {bahan_a}\n")
print(f"Bahan b : {bahan_b}\n")

print(f"Alamat object : {hex(id(bahan_a))}")
print(f"Alamat object : {hex(id(bahan_b))}")

bahan_c = bahan_a.copy()
bahan_c[0] = "Daging Sapi"
bahan_c.remove("Daging Sapi")
print(f"Bahan a : {bahan_a}\n")
print(f"Bahan b : {bahan_b}\n")
print(f"Bahan c : {bahan_c}\n")

print(f"Alamat object a : {hex(id(bahan_a))}")
print(f"Alamat object b : {hex(id(bahan_b))}")
print(f"Alamat object c : {hex(id(bahan_c))}")
