usuario=(input("Digite o nome de usuario: "))
senhaadm = "admin_12345"
senhaprofessor = "professor_12345"
senhaaluno = "aluno_12345"
match usuario:
    case "admin":
        senha = (input("Digite sua senha: "))
        if senha == senhaadm:
            print("Login Realizado com sucesso Admin, acesso total.")
        else:
            print("Senha incorreta")
    case "professor":
        senha = (input("Digite sua senha: "))
        if senha == senhaprofessor:
            print("Login Realizado com sucesso Professor, acessso ao ambiente acadêmico.")
        else:
            print("Senha Incorreta")
    case "aluno":
        senha = (input("Digite sua senha: "))
        if senha == senhaaluno:
            print("Login Realizado com sucesso Aluno, acesso ao ambiente de estudos.")
        else:
            print("Senha Incorreta")
