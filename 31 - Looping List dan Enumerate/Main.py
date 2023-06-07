# Looping dari list

## Menggunakan for loop
print(f"For Loop")
kumpulan_angka = [2, 4, 3, 1, 5, 6]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Alex", "Agus", "Alexandra", "Diandra", "Usep"]

for nama in peserta:
    print(f"nama = {nama}")

## Menggunakan for loop dan range
print(f"\nFor Loop dan Range")
kumpulan_angka = [2, 4, 3, 1, 5, 6]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

## Menggunakan while loop
print(f"\nWhile Loop")
kumpulan_angka = [2, 4, 3, 1, 5, 6]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

## Menggunakan list comprehension
print(f"\nList Comprehension")
data = ["Asep", 5, 6, "Ujang"]

[print(f"data = {i}") for i in data]

angka = [2, 4, 3, 1, 5, 6]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

## Menggunakan Enumerate
print(f"\nEnumerate")
data_list = ["Asep", 5, 6, "Ujang"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")