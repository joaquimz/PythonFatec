#Crie um programa que simule um sistema de login. Solicite um nome de usuário e senha e verifique se as credenciais estão corretas.



usuario=("admin")
senha=("12345")
login=(input("Digite seu nome de usuario: "))
senhausuario=(input("Digite sua senha: "))
if usuario==usuario and senha==senhausuario:
    print("login com sucesso")
else:
    print("login ou senha incorreto")
