def ganjil(bawah, atas):
    # Mengecek apakah bawah lebih besar atau lebih kecil dari atas
    if bawah < atas:
        # Perulangan dengan for range(start, stop)
        for i in range(bawah, atas+1):
            # Memeriksa apakah bilangan tersebut ganjil
            if i % 2 == 1:
                # Kalau ganjil akan diprint
                print(i)
    elif bawah > atas:
        # Perulangan dengan for range(start, stop, step negatif)
        for i in range(bawah, atas-1, -1):
            # Memeriksa apakah bilangan tersebut ganjil
            if i % 2 == 1:
                # Kalau ganjil akan diprint dari terbesar karena menggunakan step negatif
                print(i)
                
ganjil(10, 30)
ganjil(97, 82)