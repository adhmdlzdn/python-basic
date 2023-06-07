# Latihan perulangan membuat segitiga

sisi = 10

# 1 - Menggunakan For
print("=====Awal For=====")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("=====Akhir For=====\n")

# 2 - Menggunakan While
print("=====Awal While=====")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("=====Akhir While=====\n")

# 3 - Panggil ganjil saja
print("=====Awal While=====")
count = 1
while True:
    if (count%2):
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika genap
        count += 1
        continue
    
    # akan break jika count melibihi sisi
    if count > sisi:
        break

print("=====Akhir While=====\n")

# 4 - Membuat segitiga sama kaki dengan ganjil saja
print("=====Awal While=====")
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # Print jika ganjil
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break jika melebihi sisi
    if count > sisi:
        break
    
print("=====Akhir While=====\n")