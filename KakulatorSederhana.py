print("------Kakulator---")

while True:
    n1 = int(input("Masukan angka pertama : "))
    n2 = int(input("Masukan angka kedua : "))
    
    print("[1] Tambah")
    print("[2] Kurang")
    print("[3] Exit")
    
    pilihan = input("Tentukan Pilihanmu : ")
    pilihan = pilihan.lower()
    
    if pilihan in ("1", "tambah"):
        hasil = n1 + n2
    elif pilihan in ("2", "kurang"):
        hasil = n1 - n2
    elif pilhan in ("3", "exit"):
        break
    else:
        hasil = print("Maaf, mungkin anda salah input")
    
    print(hasil)
