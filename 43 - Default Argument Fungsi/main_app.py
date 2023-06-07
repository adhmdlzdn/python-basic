# Default Argument Fungsi

# def fungsi(argumen):
# def fungsi(argumen = nilai defaultnya):

# contoh 1
def say_hello(nama = "ganteng"):
    # fungsi dengan default argumen
    print(f"Hello {nama}")

say_hello("Dadang")
say_hello()

# contoh 2
def sapa(nama, pesan = "Apa kabar?"):
    # fungsi dengan satu input biasa dan satu default argumen
    print(f"hai {nama}, {pesan}")

sapa("Otong", "halo")
sapa("Dudung")

# contoh 3
def hitung_pangkat(angka, pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat = 3, angka = 5)
print(hasil)

# contoh 4
def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input4 = 7))