#copiar cris
# for i in range(1, 10, 1):
#     print(i)
#copiar cris
# for i in range(10, -1, -1):
#     print(i)
#copiar cris
# for i in range(10):
#     print(i)
#copiar cris
# numero_procurado = 7
# for i in range (1, 11):
#     if 1 == numero_procurado:
#         print(f"numero {numero_procurado}encontrado!")
#         break
#     print(i)
# copia cris
# for i in range(1, 11):
#     if i% 2 !=0:
#         continue
#     print(i)

#lista - é uma variavel que guarda mais um valor ao mesmo tempo

# lista = [1,1.9,"cris",True,[1,2,3,4,5,6,7],"Zé Carlos","Luana","Márcio","Camila"]

#como acessar um valor de uma lista:
# print (lista [4][4])

# lista = ("cristian","jogos","limpar","fogo","feijão","arroz")
# print(lista[3])

# Aula 1 de Python:

#inicio, final e passo
# for i in range(1,10,1):
#     print(i)

#inicio,final
# for i in range(1,11):
#     print(i)

# for i in range(10,-1,-1):
#     print(i)


# for i in range(10):
#     print(i)



# for i in range(1,11):
#     if i%2!=0:
#         continue
#     print(i)







#listas - é uma variável que guarda mais de um valor ao mesmo tempo

# lista = [1,1.9,"nath",True,[1,2,3,4,5,6,7],"Zé Carlos","Luana","Márcio","Camila"]

#como acessar um valor de uma lista:
# print(lista[4][4])


#como mostrar a lista toda:
# print(lista)

#como adicionar um elemento ao final da lista:
# lista1 = [1,2,3,4,5,6,7]
# lista1.append("Nath")
# print(lista1)

#como inserir um elemento em qualquer posição escolhida pelo usuario:
# lista1.insert(7,8)
# print(lista1)


#como remover um valor da lista:
#obs: o remove tira apenas a primeira existencia do elemento
# lista1 = [1,2,3,4,5,6,4,7]
# lista1.remove(4)
# print(lista1)

#como remover um elemento da lista (de novo):
# lista1 = [1,2,3,4,5,6,4,7]
# lista1.pop()
# print(lista1)


#como percorrer listas:
# lista_nomes = ["Zé Carlos", "Camila","Luana","Márcio","Nath"]

# for x in lista_nomes:
#     print(x)

#crie uma lista com nomes e mostre apenas os nomes que começam com a letra A
#.upper() - deixa a letgra maiuscula
# lista_nomes = ["ana","Luísa","anabelle","Bruna","Milena"]
# for nome in lista_nomes:
#     if nome[0].upper()=="A":
#         print(nome)

#como saber o tamanho da lista?
# lista_nomes = ["ana","Luísa","anabelle","Bruna","Milena"]
# print(len(lista_nomes))


# lista1 = [1,2,3,4,5,6,7,8,9,10]
# soma = 0
# for numero in lista1:
#     soma += numero
# media = soma / len(lista1)
# print(f"A media final é: {media:.2f}")

#escreva uma função que receba uma lista de numeros como entrada de retorne uma lista contendo a soma de cada par de elemento consecutivos da lista original 