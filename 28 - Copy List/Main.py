## Teknik menduplikat list

a = ["Ucup", "Otong", "Dadang"]
print(f"a = {a}")

b = a # Pass by reference
print(f"b = {b}")

# Kita akan merubah member dari a
# Ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# Address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# Menduplikat list dengan copy
print("Membuat list c dengan a.copy()")
c = a.copy() # Full duplikat / data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 1")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")