print("===================== Fahrenheit Ke Kelvin =====================")
#konversi dari fahrenheit ke kelvin
fahrenheit = float(input("Masukan fahreinheit : "))

#auto konversi ke celcius
celcius = 5 / 9 * (fahrenheit - 32)

#konversi dari celcius ke kelvin
kelvin = celcius + 273

print(f"Hasil dari fahrenheit anda ke kelvin adalah {kelvin}")

print("===================== Kelvin Ke Fahrenheit =====================")
kelvin = float(input("Masukan Nilai Kelvin : "))

reamur = 4 /5 * (kelvin - 273)

nilai_fahrenheit = 9 / 4 * reamur + 32

print(f"Hasil konversi nilai kelvin anda ke fahrenheit adalah = {nilai_fahrenheit}")



#Kecepatan
kmph = float(input("masukan kmph : "))
mps = (kmph * 1000) / 3600

print(f"hasil mps = {mps:.2f}")
