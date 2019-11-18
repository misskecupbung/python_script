masukkan = input().split(" ")
x = int(masukkan[0])
y = int(masukkan[1])

sekarang = x + y
if sekarang == 3:
    sekarang = 21
elif sekarang == 8:
    sekarang = 30
elif sekarang == 17:
    sekarang = 13
elif sekarang == 28:
    sekarang = 84
elif sekarang == 52:
    sekarang = 29
elif sekarang == 57:
    sekarang = 40
elif sekarang == 58:
    sekarang = 77
elif sekarang == 62:
    sekarang = 22
elif sekarang == 75:
    sekarang = 86
elif sekarang == 80:
    sekarang = 100
elif sekarang == 90:
    sekarang = 91
elif sekarang == 95:
    sekarang = 51
elif sekarang == 97:
    sekarang = 79

if sekarang >= 100:
    sekarang = "MENANG"

print(sekarang)
