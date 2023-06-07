# latihan mengkonversi fahrenheit ke kelvin, dan kelvin ke fahrenheit

# kelvin
# konversi fahrenheit ke kelvin
# konversi dengan rumus : 
# (1F - 32) * 5/9 + 273.15
fahrenheit = float(input("masukan suhu dalam fahrenheit : "))
kelvin = ((fahrenheit-32)*5/9)+273.15
print("konversi suhu fahrenheit ke kelvin adalah",kelvin,"Kelvin")

# fahrenheit
# konversi kelvin ke fahrenheit
# konversi dengan rumus : 
# (1K - 273.15) * 9/5 + 32
kelvin = float(input("masukan suhu dalam kelvin : "))
fahrenheit = ((kelvin-273.15)*9/5)+32
print("konversi suhu kelvin ke fahrenheit adalah",fahrenheit,"Fahrenheit")

