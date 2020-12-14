# Try dan Exception


	type of exception errors:
        1.IOError
        2.ImportError
        3.ValueError
        4.Devision by zero
        5.KeyboardInterupted
        6.EOFError

## Blok try except

1.Setiap kode program yang memungkinkan terjadinya eksepsi, 
  makaperlu untuk di tempatkan di dalam blok try

2.Ketika ada kesalahan maka kode di blok except akan dieksekusi,

3.sebaliknya jika program tidak memiliki kesalahan maka blok except
  akan di abaikan.


	try:
	    # kode
	except TipeEksepsi:
            # Penanganan kesalahan


### Code

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
	
	print("hasil pembagian adalah: ", hasil)

Hasil

![01.png](/gambar/01.png)