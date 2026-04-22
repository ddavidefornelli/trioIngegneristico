for i in range(1):
    print("il trio informatico DOMINA")
    print("Ciao Ciao ciao ciao ciao david")
    print("Gruppo magmo merda!!!")
    print("Nicola di trani ha perso il focus!")
    print("che divertimento!")

num1 = input("Inserisci il primo numero: ")
num2 = input("Inserisci il secondo numero: ")

somma = float(num1) + float(num2)

print(f"La somma di {num1} e {num2} è: {somma}")


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = b
        b += a
        a = temp
        print(b)


fibonacci(4)
