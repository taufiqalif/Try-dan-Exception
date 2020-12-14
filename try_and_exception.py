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
        print("yang anda masukan bukan angka\n")
    except ZeroDivisionError:
        print("yang anda masukan angka nol, pilih angka yg lain\n")

    # type of exception errors:
        # 1.IOError
        # 2.ImportError
        # 3.ValueError
        # 4.Devision by zero
        # 5.KeyboardInterupted
        # 6.EOFError

print("="*25)
print("hasil pembagian adalah: ", hasil)
print("="*25)
