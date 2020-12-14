# Taufiq Alif
# Belajar program python

print("="*25)
print("masukan angka")
print("="*25)

while True:
    try:
        penyebut = int(input("masukan penyebut: "))
        pembilang = int(input("masukan pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print("="*25)
        print("yang anda masukan bukan angka\n")
        print("="*25)
    except ZeroDivisionError:
        print("="*25)
        print("yang anda masukan angka nol, pilih angka yg lain\n")
        print("="*25)

print("="*25)
print("hasil pembagian adalah: ", hasil)
print("="*25)
