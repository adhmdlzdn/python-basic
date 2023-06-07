# fungsi dengan kembalian (return)

# template fungsi dengan kembalian
# def fungsi(argumen):
#     badan fungsi
#     return output

# fungsi kuadrat
def kuadrat(input_angka):
    # Fungsi kuadrat
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(2)
print(y)

print(kuadrat(5))

z = 10 + kuadrat(6)
print(z)

#  fungsi tambah
def fungsi_tambah(angka1, angka2):
    # fungsi return dengan multi input
    return angka1 + angka2

a = fungsi_tambah(8, 3)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

k, l, m, n = operasi_matematika(4, 2)

print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil bagi = {n}")