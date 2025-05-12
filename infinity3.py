numero_secreto = 7

tentativa = 0
limite_tentativas = 3

while tentativa < limite_tentativas:
    palpite = int(input("advinhe o número (entre 1 e 10): "))
    tentativa += 1


    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto.")
        break

else:
        print("Errou!tente novamente.")