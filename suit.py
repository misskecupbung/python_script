a = input().split(" ")
Blangkon = str(input())
Semar = str(input())

if Blangkon == "[]" and Semar == "()":
    print("Blangkon")
elif Blangkon == "8<" and Semar == "[]":
    print("Blangkon")
elif Blangkon == "()" and Semar == "8<":
    print("Blangkon")
elif Semar == "[]" and Blangkon == "()":
    print("Semar")
elif Semar == "8<" and Blangkon == "[]":
    print("Semar")
elif Semar == "()" and Blangkon == "8<":
    print("Semar")
else:
    print("Seri")
