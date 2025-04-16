# # #atividade 2
# # # # largura = float(input("valor da largura: "))
# # # # Altura = float(input("valor da altura: "))

# # # # area = (largura * Altura) 

# # # # print(F"A area do retangulo é: {area}")


# # #atividade 1

# # # # Metros = float(input("seu valor em metros: "))

# # # # centimetros = Metros * 100

# # # # print(f'resultado deu : {centimetros}')

# # #atividade3

# # # peso = float(input("digite seu peso: "))
# # # altura = float(input("digite sua altura: "))

# # # imc = peso / (altura ** 2)

# # # print(f'o seu imc e de {imc: .2f}')

# # # atividade 4

# # idade = float(input('digite sua idade: '))

# # if idade >= 18 and idade < 50:
# #     print('voce e adulto ')

# # elif idade >= 10 and idade < 18 :
# #     print('voce e adolescente')

# # elif idade >= 50 :
# #     print('voce e idoso ')

# # else:
# #     print ('voce e criança ')

# nota = float(input('digite sua nota entre 0 - 100:'))

# if 80 <= nota <= 100:
#     print('A')
# elif 60 <= nota < 80:
#     print('B')
# elif 40 <= nota < 60:
#     print('C')
# elif 20 <= nota < 40:
#     print('D')
# elif 0 <= nota < 20:
#     print ('F') 

# for (i=0; i < 10; i+=1)

# numero = 1
# # soma = 0
# while numero <= 100:
#     if numero % 2 == 0:
#         soma += numero
#     numero += 1
#      print(soma)

# num = float(input('digite um numero :'))

# for i in range(1, 11):
#     print(f'{num*i}')

# palavra = input('Digite uma palavra: ')

# palindromo = palavra[::-1]

# if palavra == palindromo:
#     print('A palavra é um palindromo')
# else:
#     print('A palavra não é um palíndromo')
# nome = 'FelipeHardmann'
# senha = '123456789BA'

# tentativas = 0

# while tentativas < 3:
#     nome_usuar = input('Digite o nome do seu usuário: ')
#     senha_usuar = input('Digite a senha do seu usuário: ')

#     if nome_usuar == nome and senha_usuar == senha:
#         print('Bem-vindo ao meu sistema')
#         break
#     else:
#         print('Usuário ou senha inválidas repita')
#         tentativas += 1