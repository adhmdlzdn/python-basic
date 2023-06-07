# Program list buku

list_buku = []

while True:
    print("\n\n")
    print(8*"=" , " Data buku " , 8*"=")
    judul = input("Masukan judul buku\t: ")
    penulis = input("Masukan nama penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n\n", 51*"=")
    print("| No.\t|        Judul        |       Penulis       |")
    for index, buku in enumerate(list_buku):
        print(f"| {index+1}.\t| {buku[0].center(20,' ')}| {buku[1].center(20,' ')}|")

    print(51*"=")
    response = input("Apakah ingin dilanjutkan? (y/n) ")
    if response == "n":
        break

print("Program Selesai!!")