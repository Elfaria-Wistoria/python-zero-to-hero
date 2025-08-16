#Multi keys & Nesting Dictionary
import datetime as dt

mahasiswa1 = {
	'nama':'Ucup Surucup',
	'nim':'19022001',
	'sks_lulus':130,
	'beasiswa':False,
	'lahir':dt.datetime(2001,4,10)
}
mahasiswa2 = {
	'nama':'Otong Surotong',
	'nim':'19022002',
	'sks_lulus':140,
	'beasiswa':True,
	'lahir':dt.datetime(2001,5,12)
}
mahasiswa3 = {
	'nama':'Edwinsyah',
	'nim':'19022003',
	'sks_lulus':140,
	'beasiswa':True,
	'lahir':dt.datetime(2003,3,23)
}

data_mahasiswa = {
  'MHS1': mahasiswa1,
  'MHS2': mahasiswa2,
  'MHS3': mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<15} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
  KEY = mahasiswa

  NAMA = data_mahasiswa[KEY]['nama']
  NIM = data_mahasiswa[KEY]['nim']
  SKS = data_mahasiswa[KEY]['sks_lulus']
  BEASISWA = data_mahasiswa[KEY]['beasiswa']
  LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

  print(f"{KEY:<6} {NAMA:<15} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
  print("-"*50)
