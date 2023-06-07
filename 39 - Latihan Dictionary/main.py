import datetime, os, random, string

# Template Dict
siswa_template = {
    'nama':'nama',
    'lahir':datetime.datetime(1111,1,11),
    'nis':'nis',
    'nilai':0,
    'lulus':True
}

data_siswa = {}

while True:
    os.system('cls')
    print(f"{'SELAMAT DATANG':^25}")
    print(f"{'DATA SISWA SMK PU 2023':^25}")
    print(f"-"*25)

    siswa = dict.fromkeys(siswa_template.keys())
    siswa['nama'] = input("Nama Siswa : ")
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan Lahir (MM) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (DD) : "))
    siswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    siswa['nis'] = input("NIS : ")
    siswa['nilai'] = float(input("Nilai : "))
    siswa['lulus'] = input("Lulus (True/False) : ")

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_siswa.update({KEY:siswa})

    print("\n")
    print(f"{'KEY':^6} {'Nama':^20} {'Lahir':^10} {'NIS':^10} {'Nilai':^10} {'Lulus':^10}")
    print("-"*70)

    for siswa in data_siswa:
        KEY = siswa

        NAMA = data_siswa[KEY]['nama']
        LAHIR = data_siswa[KEY]['lahir'].strftime('%x')
        NIS = data_siswa[KEY]['nis']
        NILAI = data_siswa[KEY]['nilai']
        LULUS = data_siswa[KEY]['lulus']
        
        print(f"{KEY:^6} {NAMA:^20} {LAHIR:^10} {NIS:^10} {NILAI:^10} {LULUS:^10}")

    print("\n")
    is_done = input("Apakah ada yang ingin ditambahkan? (y/n) ")

    if is_done.lower() == "n":
        break

print("\nProgram berakhir. Terimakasih")