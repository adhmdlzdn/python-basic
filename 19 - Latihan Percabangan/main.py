# Latihan percabangan

# Kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=")

angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukan angka 2 = "))

# Percabangannya
if operator == "+": # Penjumlahan
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil:.2f}")
elif operator == "-": # Pengurangan
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil:.2f}")
elif operator == "x" or operator == "*": # Perkalian
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil:.2f}")
elif operator == "/": # Pembagian
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil:.2f}")
else:
    print("Masukan angka yang bener dong ah")

print("Akhir dari program")