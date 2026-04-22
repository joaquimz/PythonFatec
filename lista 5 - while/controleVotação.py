# Faça um programa que permita cadastrar votos para 3 candidatos. Exibe contagem ao final quando for digitado "fim".

votos_flavio = 0
votos_lula = 0
votos_zema = 0

while True:
    print("1 - Candidato: Flavio")
    print("2 - Candidato: Lula")
    print("3 - Candidato: Zema")
    print("4 - Sair / Mostrar Quantidade de votos.")

    opcao = input("Escolha seu candidato: ")

    if opcao == "4":
        print("RESULTADO DA VOTAÇÃO:")
        print(f"Flavio: {votos_flavio}")
        print(f"Lula:   {votos_lula}")
        print(f"Zema:   {votos_zema}")
        print("Saindo do programa...")
        break
    elif opcao == "1":
        votos_flavio += 1
        print(f"Voto para Flavio registrado! Agora são {votos_flavio} votos para Flavio ")

    elif opcao == "2":
        votos_lula += 1
        print(f"Voto para Lula registrado! Agora são {votos_lula} votos para Lula ")

    elif opcao == "3":
        votos_zema += 1
        print(f"Voto para Zema registrado! Agora são {votos_zema} votos para Zema ")

    else:
     print("Opção invalida. Tente novamente...")

