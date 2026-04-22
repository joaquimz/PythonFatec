# O usuário digita o preço e a quantidade de produtos até digitar “sair”. O Sistema mostra a quantidade de produtos e o valor final da compra.

preco_total = 0
produtos_total = 0

print("--- BEM-VINDO A CAIXA REGISTRADORA ---")
while True:
    print("---DIGITE (SAIR) QUANDO FINALIZAR---")
    preco = (input("Digite o preço do produto: ")).lower()

    if preco == "sair":
        print("Saindo...")
        break

    quantidade = int(input("Quantidade: "))

    preco_total += float(preco) * quantidade
    produtos_total += quantidade

    print("---CAIXA REGISTRADORA---")
    print(f"PREÇO = R$ {preco_total}")
    print(f"QUANTIDADE PRODUTOS = {produtos_total}")
    print("-"*30)
