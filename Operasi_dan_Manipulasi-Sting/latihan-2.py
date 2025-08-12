kalimat = input("masukan kalimat mu : ")

print(f"kalimat yang anda masukan adalah : {kalimat}")
print(f"Konversi ke UpperCase : {kalimat.upper()}")
print(f"Konversi ke LowerCase : {kalimat.lower()}")

print(f"Apakah kalimat anda semuanya huruf besar : {kalimat.isupper()}")
print(f"Apakah kalimat anda semuanya huruf kecil : {kalimat.islower()}")
print(f"Apakah kalimat anda tittle case : {kalimat.istitle()}")

print(f"Apakah kalimat anda di awali dengan kata \"Hallo\" : {kalimat.startswith("Hallo")} ")
print(f"Apakah kalimat anda di akhiri dengan kata \"Bye\" : {kalimat.endswith("Bye")} ")

print(f"Memisahkan kalimat menjadi list kata : {kalimat.split()}")
print(f"Menggabungkan kata-kata dengan tanda - : {"-".join(kalimat.split())}")

print(f"Rata kanan : {kalimat.rjust(30)}")
print(f"bersihkan . : {kalimat.strip(".")}")
