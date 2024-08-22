from time import sleep




soma = 0
print("=====================")
numero = int(input("Escolha um número: "))
inicial = int(input("Escolha um início: "))
final = int(input("Escolha um final: "))
print("=====================")

sleep(2)
print(" ")

for n in range (inicial, final):
    if n % numero == 0 :
        soma += n

print(f"A soma total do multiplos de {numero} do {inicial} até {final} é de {soma}")