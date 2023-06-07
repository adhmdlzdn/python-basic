# Looping dictionary
teman_temanku = {
    "sup":"usup surusup",
    "sep":"asep surasep",
    "sip":"asip surasip"
}

# Looping first try (yang keluar adalah keynya)

for teman in teman_temanku:
    print(teman)

# Operator untuk mengambil item / iterables
print("\n")

# Memanggil keys nya
keys = teman_temanku.keys()
print(keys)

for key in teman_temanku.keys():
    print(teman_temanku.get(key))

# Memanggil value nya
print("\n")

values = teman_temanku.values()
print(values)

for value in teman_temanku.values():
    print(value)

# Memanggil item nya
print("\n")

items = teman_temanku.items()
print(items)

for item in teman_temanku.items():
    print(item)

# Memanggil key serta value nya
print("\n")

for key,value in teman_temanku.items():
    print(f"key = {key}, value = {value}")