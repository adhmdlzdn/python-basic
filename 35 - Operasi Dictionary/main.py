# Operasi Dictionary

data_dict = {
    "cup":"ucup si cupu",
    "sep":"asep kena asep",
    "cok":"ucok si cocok"
}

# panjang dict
LENDICT = len(data_dict)
print(f"panjang data : {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah data {KEY} ada di data_dict : {CHECKKEY}")

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["dung"] = "dudung makadung"
print(data_dict)

data_dict.update({"cup":"ucup si cupu"})
print(data_dict)
data_dict.update({"mak":"maka mak"}) # Jika key ada pada dict, maka akan mengganti data yang lama dengan yang baru. Jika data tidak ada maka akan otomatis terbuat yang baru
print(data_dict)

# mendelete data pada dictionary
del data_dict["mak"]
print(data_dict)