#Simule um sistema de cadastro de produtos.

lista_produtos = []

def cadastrar_produtos():
    add_produto = input("Digite o nome do produto: ")
    lista_produtos.append(add_produto.lower())
    print("O produto foi cadastrado com sucesso!")
    return lista_produtos

def listar_produtos():
    print("Lista de produtos: ")
    print(lista_produtos)

def buscar_produto():
    search_produto = input("Digite o nome do produto para busca: ")
    for produto in lista_produtos:
        if produto == search_produto.lower():
            print(f"Seu produto foi encontrado no estoque: {produto}")

while True:
    print("ESTOQUE DE PRODUTOS")
    print("[1] Cadastrar produto")
    print("[2] Listar produtos")
    print("[3] Buscar produto pelo nome")
    print("[4] Sair")

    user = input("Escolha uma das opções:")

    if user == "1":
        cadastrar_produtos()
    elif user == "2":
        listar_produtos()
    elif user == "3":
        buscar_produto()
    elif user == "4":
        print("Saindo...")
        break
    else:
        print("Opção invalida. Tente novamente!")