def BubbleSort(A):
    N = len(A)
    for i in range(N-1):
        for j in range(N-1):
            if(A[i]>A[j+1]):
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
Data = [30,10,15,6,10,8]
BubbleSort(Data)
print(Data)
