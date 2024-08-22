print("=====Calculadora de Tabuada(*)=====\n")

numero = int(input("Digite um número para a tabuada :"))
mult = 0
for n in range(1, 11):
    mult = numero * n
    print(f"{n} x {numero} = {mult}")