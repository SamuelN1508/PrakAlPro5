def perkalian(a, b):
    x = 0
    # Perulangan ini menggunakan for range
    for a in range (1, a + 1):
        # Untuk setiap rentang dari 1 sampai a, x akan ditambah b
        x += b
    return x
        
print(perkalian(15,10))
print(perkalian(100,10))