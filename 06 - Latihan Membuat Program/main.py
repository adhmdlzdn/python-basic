# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPRATURE\n")

# celcius
celcius = float(input("masukan suhu dalam celcius: "))
print("suhu adalah",celcius,"Celcius")

# reamur
# (4/5) * celcius
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"Reamur")

# fahrenheit
# ((9/5) * celcius) + 32
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenhiet")

# kelvin
# celcius + 273
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin,"Kelvin")