# import modul_kalkulator
from modul_kalkulator import *

print("program kalkulator")
print("Masukan angka yang akan di hitung")

a = int(input("masukan A: ",))
b = int(input("masukan B: ",))

print("Hasil A + B : ", tambah(a,b))
print("Hasil A * B : ", kali(a,b))

hit = kalkulator (a,b)
print("Class -> Hasil A + B : ", hit.tambah())
print("Class -> Hasil A * B : ", hit.kali())
print("Class -> Hasil A / B : ", hit.bagi())
print("Class -> Hasil A - B : ", hit.kurang())
