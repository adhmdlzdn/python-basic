# Copy dan Pop Dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"totong surotong",
    "dung":"adung adudung",
    "sep":"asep surasep",
    "cong":"ocong sibencong"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"]="ucup ga ganteng"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep: {dataAsep}\n")
print(f"friends: {friends}\n")

# popitem dictionary (key yang terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir: {dataTerakhir}\n")
print(f"friends: {friends}\n")