# Operasi komparasi
# Setiap hasil dari operasi komparasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari (>)
print("======== lebih besar dari (>)")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# Lebih kecil dari (<)
print("======== lebih kecil dari (<)")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih kecil dari (<)
print("======== lebih kecil dari (<)")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih besar sama dengan (>=)
print("======== lebih besar sama dengan (>=)")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Lebih kecil sama dengan (<=)
print("======== lebih kecil sama dengan (<=)")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama dengan (==)
print("======== sama dengan (==)")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# Tidak sama dengan (!=)
print("======== tidak sama dengan (!=)")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

# 'is not' sebagai komparasi object identity
print("======== object identity (is)")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x =",x,", id =",hex(id(x)))
print("nilai y =",y,", id =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x =",x,", id =",hex(id(x)))
print("nilai y =",y,", id =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

# 'is not' sebagai komparasi object identity
print("======== object identity (is not)")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x =",x,", id =",hex(id(x)))
print("nilai y =",y,", id =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x =",x,", id =",hex(id(x)))
print("nilai y =",y,", id =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)