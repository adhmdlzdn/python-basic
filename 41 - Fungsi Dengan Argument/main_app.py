# Fungsi dengan argument (input)

# Template
# def fungsi(argumen):
#     badan fungsi

def hello_world(nama):
    print(f"Selamat datang dunia, {nama}")

hello_world("dudung")
hello_world("makdung")

# program tambah
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(5, 7)
tambah(9999, 1)

# absen nama
def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota = ["yayan", "yuyun", "yeyen"]

say_hi(anggota)