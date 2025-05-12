incio=int(input("Digite o numero inicial do intervalo: "))
fim=int(input("Digite o numero final do intervalo: "))

somaa_pares = 0
tem_par = False

for numero in range(incio, fim + 1):
    if numero % 2 == 0:
        somaa_pares += numero
        tem_par = True

else:
    if tem_par:
        print(f"A soma dos números pares no intervalo de {incio} a {fim} é: {somaa_pares}")
    else:
        print(f"Não há números pares no intervalo de {incio} a {fim}.")