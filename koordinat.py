a = input().split(" ")
N = int(a[0])
x1 = int(a[1])
y1 = int(a[2])
x2 = int(a[3])
y2 = int(a[4])

for i in range (N):
    for j in range(N):
        if i==x1 and j==y1:
            print("o", end="")
        elif i==x2 and j==y2:
            print("x", end="")
        else:
            print(".", end="")
    print()
