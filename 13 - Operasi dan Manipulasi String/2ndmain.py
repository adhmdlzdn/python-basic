# Operator dalam bentuk methods

# 1. Merubah case dari string
# Merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)
# Merubah semua ke lower case
alay = "aKu KeCe AbieeezzzZzzZzzz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# 2. Pengecekan dengan isX method
# Contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower " + str(apakah_lower))
# Contoh pengecekan upper case
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper " + str(apakah_upper))
# isalpha() <-- untuk mengecek semuanya huruf
apakah_aplha = salam.isalpha() # hasilnya bool
print(salam + " is alpha " + str(apakah_aplha))
# isalnum() <-- untuk mengecek huruf dan angka
apakah_alnum = salam.isalnum() # hasilnya bool
print(salam + " is alnum " + str(apakah_alnum))
# isdecimal() <-- untuk mengecek angka saja
apakah_decimal = salam.isdecimal()
print(salam + " is decimal " + str(apakah_decimal))
# isspace() <-- untuk mengecek spasi kosong, tab, newline(\n)
apakah_space = salam.isspace()
print(salam + " is space " + str(apakah_space))
# istitle() <-- untuk mengecek kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bool
print(judul + " is title = " +str(cek_judul))

# 3. Pengecekan komponen startswith() dan endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

# 4. Penggabungan komponen join() dan split()
# join()
pisah = ['aku','sayang','kamu']
gabungan = ",".join(pisah)
print(pisah)
print(gabungan)
gabungan = ' '.join(pisah)
gabungan = ' ehm '.join(pisah)
print(gabungan)
# split()
gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# 5. Alokasi karakter rjust(), ljust(), center()
# rjust()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
# ljust()
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
# center()
tengah = "tengah".center(20,"=")
print("'"+tengah+"'")
# kebalikannya -> strip()
tengah = "tengah".strip("=")
print("'"+tengah+"'")