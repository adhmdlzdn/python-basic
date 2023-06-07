# Continue, pass

# 1. Pass -> berfungsi sebagai dummy, tidak akan dieksekusi
#angka = 0

#while angka < 5:
#    angka += 1

#    if angka == 3:
#        pass # ini tidak akan dieksekusi

#print(angka)

# 2. Continue
angka = 0

print(f"angka sekarang -> {angka}") # aksi 1

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice!")
        continue # akan membuat loop meloncat ke awal lagi

    print("whassup!") # aksi 2

print("Finish!")