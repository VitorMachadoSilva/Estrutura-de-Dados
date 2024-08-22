# CONTAGEM REGRESSIVA USANDO (FOR RANGE)

from time import sleep


contagem_Regressiva = 10

for item in range (1, 11):
    print(f"Contagem: {contagem_Regressiva}")
    contagem_Regressiva = contagem_Regressiva - 1 
    sleep(1)
else:
    print("Feliz Ano Novo\n\n")

print("Contagem numero 2")
for n in range(10,-1, -1):
    if n == 0:
        print("Feliz ano novo")
    else:
        print(n)
    sleep(1)
    

