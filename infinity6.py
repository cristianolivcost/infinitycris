produtos = {}

for i in range(5):
    nome = input(F'Digite o nome do {i+1} produto:')
    preco = float(input(f"Digite o preço do produto '{nome}': R$ "))
    produtos[nome] = preco


valor_total = sum(produtos.values())

print("\nResumo da compra:")
for nome, preco in produtos.items():
    print(f"- {nome}: R$ {preco:.2f}")
print(f"\nValor total da compra: R$ {valor_total:.2f}")

