# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

# Operasi Aritmatika
a = 5 # adalah assignment
print("nilai a =",a)
a += 1 # artinya adalah a = a + 1
print("nilai a+= 1, nilai a menjadi",a)
a -= 2 # artinya adalah a = a - 2
print("nilai a-= 2, nilai a menjadi",a)
a *= 5 # artinya adalah a = a * 5
print("nilai a*= 5, nilai a menjadi",a)
a /= 2 # artinya adalah a = a / 2
print("nilai a/= 2, nilai a menjadi",a)

b = 10 # adalah assignment
print("\nnilai b =",b)
b %= 3 # artinya adalah b = b % 3 (Modulus)
print("nilai b%= 3, nilai b menjadi",b)
b = 10 
print("nilai b =",b)
b //= 3 # artinya adalah b = b // 1 (Floor Division)
print("nilai b//= 1, nilai b menjadi",b)

a = 5 # adalah assignment
print("\nnilai a =",a)
a **= 3 # artinya adalah a = a ** 3 (Pangkat/Eksponen)
print("nilai a**= 3, nilai a menjadi",a)


# Operasi Bitwise
# OR
c = True
print("\nnilai c =",c)
c |= False 
print("nilai c|= False, nilai c menjadi",c)
c = False
print("nilai c =",c)
c |= False 
print("nilai c|= False, nilai c menjadi",c)
# AND
c = True
print("\nnilai c =",c)
c &= False 
print("nilai c&= False, nilai c menjadi",c)
c = True
print("nilai c =",c)
c &= True 
print("nilai c&= False, nilai c menjadi",c)
# XOR
c = True
print("\nnilai c =",c)
c ^= False 
print("nilai c^= False, nilai c menjadi",c)
c = False
print("nilai c =",c)
c ^= False 
print("nilai c^= False, nilai c menjadi",c)

# Geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2 
print("nilai d>>= 2, nilai d menjadi",d)
d <<= 1 
print("nilai d<<= 1, nilai d menjadi",d)