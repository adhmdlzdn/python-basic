import datetime

siswa1 = {
    'nama':'Juju Suka Maju',
    'nis':'2223001',
    'nilai':8.0,
    'beasiswa':False,
    'lahir':datetime.datetime(2005,1,29)
}

siswa2 = {
    'nama':'Jaja Suka Jajan',
    'nis':'2223002',
    'nilai':10.0,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,8,22)
}

siswa3 = {
    'nama':'Jeje Suka JJ',
    'nis':'2223003',
    'nilai':7.8,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,2,29)
}

data_siswa = {
    'SIS001':siswa1,
    'SIS002':siswa2,
    'SIS003':siswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'NIS':<7} {'Nilai':<5} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*60)

for siswa in data_siswa:
    KEY = siswa

    NAMA = data_siswa[KEY]['nama']
    NIS = data_siswa[KEY]['nis']
    NILAI = data_siswa[KEY]['nilai']
    BEASISWA = data_siswa[KEY]['beasiswa']
    LAHIR = data_siswa[KEY]['lahir'].strftime('%x')
    
    print(f"{KEY:<6} {NAMA:<17} {NIS:<7} {NILAI:<5} {BEASISWA:^9} {LAHIR:<10}")