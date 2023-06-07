data_angka = [1,5,3,4,2,5,4,5,6,7,4,5,6,2,3,4,3,7,5,8,9]

print(f"data angka = \n {data_angka}")

# Count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_1 = data_angka.count(1)

print(f"jumlah data 4 = {jumlah_data_4}")
print(f"jumlah data 1 = {jumlah_data_1}")

# Ambil posisi data (index)
data = ["Ucup", "Asep", "Dadang", "Maul"]

print(f"data = {data}")

index_dadang = data.index("Dadang")
index_maul = data.index("Maul")

print(f"index si Dadang = {index_dadang}")
print(f"index si Maul = {index_maul}")

# Mengurutkan list 
print(f"data angka sebelum di sort = \n {data_angka}")
data_angka.sort()
print(f"data angka setelah di sort = \n {data_angka}")

print(f"data sebelum di sort = \n {data}")
data.sort()
print(f"data setelah di sort = \n {data}")

# Membalik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n {data_angka} \n {data}")