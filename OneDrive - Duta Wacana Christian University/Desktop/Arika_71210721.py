x = True
while x:
    print ("Masukan pilihan\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\nQ.Keluar")
    operasi = (input("Masukan pilihan:"))

    if operasi == "1":
        bil1 = int(input('Masukan bilangan 1:'))
        bil2 = int(input('Masukan bilangan 2:'))
        hasil = bil1 + bil2
        print ('Hasil dari ', bil1, "+", bil2, ' = ',hasil)
    elif operasi == "2":
        bil1 = int(input('Masukan bilangan 1:'))
        bil2 = int(input('Masukan bilangan 2:'))
        hasil = bil1 - bil2 
        print ('Hasil dari ', bil1, "-", bil2, ' = ',hasil)
    elif operasi == "3":
        bil1 = int(input('Masukan bilangan 1:'))
        bil2 = int(input('Masukan bilangan 2:'))
        hasil= bil1 * bil2
        print ('Hasil dari ', bil1, "*", bil2, ' = ',hasil)
    elif operasi == "4":
        bil1 = int(input('Masukan bilangan 1:'))
        bil2 = int(input('Masukan bilangan 2:'))
        hasil = bil1 / bil2
        print ('Hasil dari ', bil1, "/", bil2, ' = ',hasil)
    elif operasi == "Q":
        x = False