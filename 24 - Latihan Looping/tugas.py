# Tugas membuat bentuk ketupat

x = 11
y = int(x//2)
count = 1
spasi = int(x/2)

for i in range(x):
    if i <= y:
        print("*"*count)
        count += 1
        spasi -= 1
    else:
        print("*"*y)
        y -= 1

