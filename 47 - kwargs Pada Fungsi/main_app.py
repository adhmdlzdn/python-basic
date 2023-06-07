''' **kwargs '''

def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi("ucup", 180, 70)

def fungsi(**kwargs):
    ''' fungsi kwargs '''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi(nama="ucup", tinggi=180, berat=70)

# Studi kasus
def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kurang":
        for angka in args:
            output -= angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Operasi tidak ada")

    return output

hasil = math(1, 2, 3, 4, option="tambah")
print(f"Hasilnya adalah {hasil}")

hasil = math(1, 2, 3, 4, option="kurang")
print(f"Hasilnya adalah {hasil}")

hasil = math(1, 2, 3, 4, option="kali")
print(f"Hasilnya adalah {hasil}")