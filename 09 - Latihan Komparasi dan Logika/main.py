# Latihan logika dan komparasi
# membuat gabungan area rentang dari angka


# +++++3-----10+++++
inputUser = float(input("Masukan angka yang bernilai kurang dari 3\natau lebih dari 10 [>] "))

# +++++3----------
# Memeriksa angka kurang dari 3
isKurangDari = inputUser < 3
print("Kurang dari 3 =",isKurangDari)

# ----------10+++++
# Memeriksa angka lebih dari 10
isLebihDari = inputUser > 10
print("Lebih dari 10 =",isLebihDari)

# +++++3------10+++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan =",isCorrect)

print(15*"=")

# -----3+++++10-----
inputUser = float(input("Masukan angka yang bernilai lebih dari 3\ndan kurang dari 10 [>] "))

# -----3++++++++++
# Memeriksa angka lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =",isLebihDari)

# ++++++++++10-----
# Memeriksa angka kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 =",isKurangDari)

# -----3+++++10-----
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan =",isCorrect)