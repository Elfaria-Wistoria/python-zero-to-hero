print("==============================Latihan-1==============================")
#masukan angka
angka = float(input("Masukan Angka Anda : "))

lebihdari = ( angka > 0 )
kurangdari = (angka < 5 )

lebihdari2 = ( angka > 8 )
kurangdari2 = (angka < 11 )

correct2 = lebihdari2 and kurangdari2
correct = lebihdari and kurangdari
kebenaran = correct or correct2

print(f"Apakah angka yang di masukan lebih dari 0 dan kurang dari 5?\n atau lebih dari 8 dan kurang dari 11 ? : ", kebenaran)


print("==============================Latihan-2==============================")
#masukan angka
angka = float(input("Masukan Angka Anda : "))

kurangdari = ( angka < 0 )
lebihdari = (angka > 5 )

kurangdari2 = ( angka < 8 )
lebihdari2 = (angka > 11 )

correct = kurangdari or lebihdari
correct2 = kurangdari2 or lebihdari2
kebenaran2 = correct and correct2

print(f"Apakah angka yang di masukan kurang dari 0 dan lebih dari 5?\n atau kurang dari 8 dan lebih dari 11 ? : ", kebenaran2)
