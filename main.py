for i in range(30):
    print("il trio informatico DOMINA")


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = b
        b += a
        a = temp
        print(b)


fibonacci(12)
