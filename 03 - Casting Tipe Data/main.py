# kita belajar casting
# merubah dari satu tipe ke tipe lain
# tipe data = int, float, str, bool

## INTEGER
print("====INTEGER====")
data_int = 9
print("data =", data_int, ", tipe =", type(data_int))

data_float  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int) # akan false jika nilai int = 0
print("data =", data_float, ", tipe =", type(data_float))
print("data =", data_str, ", tipe =", type(data_str))
print("data =", data_bool, ", tipe =", type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 2
print("data =", data_float, ", tipe =", type(data_float))

data_int    = int(data_float) # akan dibulatkan kebawah
data_str    = str(data_float)
data_bool   = bool(data_float) # akan false jika nilai float = 0
print("data =", data_int, ", tipe =", type(data_int))
print("data =", data_str, ", tipe =", type(data_str))
print("data =", data_bool, ", tipe =", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = False
print("data =", data_bool, ", tipe =", type(data_bool))

data_int    = int(data_bool) # akan menjadi 0 jika nilai bool = False
data_str    = str(data_bool)
data_float  = float(data_bool) # akan menjadi 0 jika nilai bool = False
print("data =", data_int, ", tipe =", type(data_int))
print("data =", data_str, ", tipe =", type(data_str))
print("data =", data_float, ", tipe =", type(data_float))

## STRING
print("====STRING====")
data_str = "10"
print("data =", data_str, ", tipe =", type(data_str))

data_int    = int(data_str) # string harus angka
data_float  = float(data_str) # string harus angka
data_bool   = bool(data_str) # false jika nilai string kosong
print("data =", data_int, ", tipe =", type(data_int))
print("data =", data_float, ", tipe =", type(data_float))
print("data =", data_bool, ", tipe =", type(data_bool))

