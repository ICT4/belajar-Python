# Data type & variable in Python

nama = "Agung"
umur = 19
nilai = 9.50
keren = True
tipe_List = ["str", "int", "float", "list", "tuple", "range", "dict", "set"]
tipe_tuple = ("Apples", "Berries", "Chocolate", "Donut")
tipe_range = range(10)
tipe_dict = {"nama": "Agung", "Umur": 19}
tipe_set = {"berries", "banana", "cuanki"}

print("Nama saya adalah : " + nama + ", tipe datanya adalah", type(nama))
print("Umur saya sekarang : ", umur, " Tahun, tipe datanya adalah", type(umur))
print("Nilai semester saya adalah : ", nilai, ", tipe datanya adalah", type(nilai))
print("Saya adalah orang yang keren ? ", keren, " , tipe datanya adalah", type(keren))
print("Umur saya di tahun depan adalah : ", umur + 1, " Tahun\n")
print(tipe_List, "<- merupakan contoh dari tipe data", type(tipe_List))
print(tipe_tuple, "<- merupakan contoh dari tipe data", type(tipe_tuple))
print(tipe_range, "<- merupakan contoh dari tipe data", type(tipe_range))
print(tipe_dict, "<- merupakan contoh dari tipe data", type(tipe_dict))
print(tipe_set, "<- merupakan contoh dari tipe data", type(tipe_set))
