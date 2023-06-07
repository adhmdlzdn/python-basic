# Latihan Fungsi

import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # mengambil input user
# LEBAR = int(input("Masukkan nilai lebar : "))
# PANJANG = int(input("Masukkan nilai panjang : "))

# # program menghitung luas dan keliling
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # menampilkan hasil
# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan keliling = {KELILING}")

def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    # mengambil input user
    lebar = int(input("Masukkan nilai lebar : "))
    panjang = int(input("Masukkan nilai panjang : "))

    return lebar, panjang

def hitung_luas(lebar, panjang):
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    return 2*(lebar+panjang)

def display(message, value):
    print(f"Hasil perhitungan {message} = {value}")

while True:
    header()

    opsi = input("Pilih 1 untuk opsi menghitung luas, dan pilih 2 untuk opsi menghitung keliling : ")
    if opsi == "1":
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR, PANJANG)
        display("luas", LUAS)
        
    elif opsi == "2":
        LEBAR, PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("keliling", KELILING)

    isContinue = input("Apakah ingin lanjut? (y/n) ")
    if isContinue == "n":
        break

print("Program berakhir, terimakasih")