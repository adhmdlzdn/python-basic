# Tugas Operasi Komparasi dan Logika
# Nama : Adrian Ahmad Al Zidan

# lebih dari 0, kurang dari 5, lebih dari 8, kurang dari 11
print("1. Soal : -----0+++++5--------8+++++11-----")
iU = float(input("Masukan angka lebih dari 0, kurang dari 5\nlebih dari 8, kurang dari 11 [>] "))
# Memeriksa angka
# -----0+++++5-----
i1 = iU > 0
i2 = iU < 5
iC1 = i1 and i2
print("Angka pertama =",iC1)
# -----8+++++11-----
i3 = iU > 8
i4 = iU < 11
iC2 = i3 and i4
print("Angka kedua =",iC2)
# -----0+++++5--------8+++++11-----
iC3 = iC1 or iC2
print("Angka terakhir =",iC3)
# Final
iC = iU > 0 and iU < 5 or iU > 8 and iU < 11
print("Angka yang anda masukan =",iC)

print("\n",15*"="+"\n")

# kurang dari 0, lebih dari 5, kurang dari 8, lebih dari 11
print("2. Soal : +++++0-----5++++++++8-----11+++++")
# Memeriksa angka
# +++++0-----5+++++
i1 = iU < 0
i2 = iU > 5
iC1 = i1 or i2
print("Angka pertama =",iC1)
# +++++8-----11+++++
i3 = iU < 8
i4 = iU > 11
iC2 = i3 or i4
print("Angka kedua =",iC2)
# +++++0-----5++++++++8-----11+++++
iC3 = iC1 and iC2
print("Angka terakhir =",iC3)
# Final
iC = iU < 0 or iU > 5 and iU < 8 or iU > 11
print("Angka yang anda masukan =",iC)
