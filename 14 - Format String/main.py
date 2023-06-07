# Format string

# Contoh generic
# String
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# Boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# Angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# Bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# Bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

# Bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# Menampilkan landing zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# Menampilkan tanda + dan -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# Memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.1%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp{harga*jumlah:,}"
print(format_string)

# Format angka lain (binary, octal, hexadecimal)
angka = 10
format_bin = f"binary = {bin(angka)}"
format_oct = f"octal = {oct(angka)}"
format_hex = f"hexa = {hex(angka)}"
print(format_bin)
print(format_oct)
print(format_hex)