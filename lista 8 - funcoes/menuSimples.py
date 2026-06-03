#Crie uma função exibe_menu() que imprima um menu simples na tela.

def exibe_menu():
    while True:
      print("MENU SIMPLES")
      print("1 - ENTRAR")
      print("2 - CADASTRAR-SE")
      print("3 - SAIR")
      user = input("Escolha uma das opçoes acima: ")
      if user == "1":
          print("Voce escolheu: ENTRAR")
      elif user == "2":
          print("Voce escolheu: CADASTRAR-SE")
      elif user == "3":
          print("Voce escolheu: SAIR")
          break
      else:
          print("Opção inválida! Tente novamente.")

exibe_menu()





