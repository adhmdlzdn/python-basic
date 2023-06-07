# Deep Copy Nested List
data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# Mengambil data dari nested list
data = data_2D[1][0]
print(f"data = {data}")

# Address dari semua list
data_2D = [data_0, data_1, 10]

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print("address dari number ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# Kita gunakan deepcopy
from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli {hex(id(data_2D))}")
print(f"address deeep {hex(id(data_2D_deepcopy))}")

print("address dari number ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")