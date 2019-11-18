#menampilkan menggunakan range
#range(n) = [0.......sampai n-1]
#contohnya range(5)= [0,.....4]
n = int(input())
hasil = 1
for i in range (1, n+1):
    hasil = hasil * i
print(hasil)
