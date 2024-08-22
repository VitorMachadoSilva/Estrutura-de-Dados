soma = 0

print("Escolha um número")
numero = int(input())

for n in range (1, 501):
    if n % numero == 0 :
        soma += n

print(soma)