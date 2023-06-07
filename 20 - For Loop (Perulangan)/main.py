# Perulangan (loop)

# for kondisi:
#   aksi

# 1. Dengan list
angka2_list = [0,2,4,8,10] # ini dengan list
print(angka2_list)

for i in angka2_list:
    print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# 2. Dengan range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang -> {i}")
    
print("akhir dari program 2 \n")

angka2_range = range(1,10)

for i in angka2_range:
    #print(f"i sekarang -> {i}")
    print("saya keren")

print(f"akhir dari program 3 \n")

# 3. Dengan string
data_str = "saya"

for huruf in data_str:
    print(huruf)

print("akhir dari program 4 \n")