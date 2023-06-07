# operasi aritmatika 

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# operasi pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# operasi pembagian /
hasil = a / b
print(a,"/",b,"=",hasil)

# operasi eksponen **
hasil = a ** b
print(a,"**",b,"=",hasil)

# operasi modulus %
hasil = a % b
print(a,"%",b,"=",hasil)

# operasi floor division //
hasil = a // b
print(a,"//",b,"=",hasil)

# prioritas operasi, operational predence
'''
    1. ()
    2. exponen **
    3. perkalian, dkk * / % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x # operasi hitung akan dimulai dari tingkat tertinggi
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=",hasil)

hasil = x + y * z
print(x,"+",y,"*",z,"=",hasil)

hasil = (x + y) * z # kurung akan mengambil langkah paling pertama / op
print("(",x,"+",y,") *",z,"=",hasil)