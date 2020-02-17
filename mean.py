n = []
while True:
    i = input("Masukkan nilai: ")
    if i != 'x':
        n.append(int(i))
    else:
        sum = 0
        for x in n:
            sum += x
        print("Rata-rata nilai adalah: ", sum/len(n))
        exit()
