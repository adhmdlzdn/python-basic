''' Type hints untuk fungsi '''

# Bentuk standar fungsi
# Studi kasus
'''
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("dadang")
fungsi(True)
'''

import string

# Penggunaan Type Hints
def pangkat_sepuluh(argument:int) -> int:
    hasil = 10**argument
    return hasil

hasil = pangkat_sepuluh(2)
print(hasil)

# Perbandingan
def display(argument:string):
    print(argument)

display("Dadang")