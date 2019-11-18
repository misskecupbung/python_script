#tanpa rekursif
def segitiga(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end= "")
        print()
segitiga(2)
--
#rekursif
def segitigaR(n):
    if n==1:
        print("*")
    else:
        segitigaR(n-1)
    for i in range(n):
        print("*", end="")
    print()
segitiga(2)
