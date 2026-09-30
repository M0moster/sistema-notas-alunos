alunos = []
turma = {
    "aluno1": {
        "nome": "",
        "nota1": 0.0,
        "nota2": 0.0,
        "média": 0.0,
        "situação": ""
    },
    "aluno2": {
        "nome": "",
        "nota1": 0.0,
        "nota2": 0.0,
        "média": 0.0,
        "situação": ""
        },
    "aluno3": {
        "nome": "",
        "nota1": 0.0,
        "nota2": 0.0,
        "média": 0.0,
        "situação": ""
        }
}

def menu_inicial():
    menu = input("1 - Cadastrar Alunos. \n2 - Lançar Notas. \n3 - Calcular Média. \n4 - Mostrar Resultados. \n0 - Sair. \n")
    if menu == "1":
        cadastrar_aluno()
    elif menu == "2":
        lançar_notas()
    elif menu == "3":
        calcular_média()
    elif menu == "4":
        mostrar_resultados()
    elif menu == "0":
        print("Encerrando programa..." ) 
        exit()
    else: print ("Seleção inválida, por favor digite um numero correspondente. ")
    menu_inicial()

def cadastrar_aluno():
    for alunosCadastrados in turma:
        cadastro = input("Digite o nome dos alunos a serem cadastrados: ").lower()
        alunos.append(cadastro)
        turma[alunosCadastrados]["nome"] = cadastro
    print("Alunos cadastrados! ", alunos) 
    menu_inicial()

def lançar_notas():
    verificação_aluno = input("digite nome do aluno que você deseja lançar nota, ou ENTER para voltar para o menu: ").lower()
    if verificação_aluno in alunos:
        seleção_prova = (input("Aluno cadastrado! Digite 1 para lançar nota da primeira prova, ou digite 2 para lançar nota da segunda prova: "))
        if seleção_prova == "1":
            lançamento_notas = float(input("Prova 1 selecionada! Digite a nota a ser lançada: "))
            for alunosCadastrados2 in turma:
                if verificação_aluno == turma[alunosCadastrados2]["nome"]:
                    turma[alunosCadastrados2]["nota1"] = lançamento_notas
                    print (turma[alunosCadastrados2])
        elif seleção_prova == "2":
            lançamento_notas2 = float(input("Prova 2 selecionada! Digite a nota a ser lançada: "))
            for alunos_cadastrados2 in turma:
                if verificação_aluno == turma[alunos_cadastrados2]["nome"]:
                    turma[alunos_cadastrados2]["nota2"] = lançamento_notas2
                    print (turma[alunos_cadastrados2])
        elif seleção_prova != "1" or "2":
            print("Seleção inválida, por favor digite um numero correspondente.")
            lançar_notas()
    elif verificação_aluno == "":
        menu_inicial()
    else: print ("\naluno não existe. ")
    menu_inicial()

def calcular_média():
    verificação_aluno2 = input("digite nome do aluno que você deseja calcular a média: ").lower()
    if verificação_aluno2 in alunos:
        for alunos_cadastrados3 in turma:
            if verificação_aluno2 == turma[alunos_cadastrados3]["nome"]:
                turma[alunos_cadastrados3]["média"] = (turma[alunos_cadastrados3]["nota1"] + turma[alunos_cadastrados3]["nota2"]) / 2
                if turma[alunos_cadastrados3]["média"] >= 7:
                    turma[alunos_cadastrados3]["situação"] = "Aprovado"
                elif turma[alunos_cadastrados3]["média"] >= 5:
                    turma[alunos_cadastrados3]["situação"] = "Recuperação"
                elif turma[alunos_cadastrados3]["média"] < 5:
                    turma[alunos_cadastrados3]["situação"] = "Reprovado"
                print (turma[alunos_cadastrados3])

    else: print ("\naluno não existe. ")
    menu_inicial()

def mostrar_resultados():
    print("Mostrando informações dos alunos! ")
    for informações_alunos in turma:
        print (turma[informações_alunos])
        print("")
menu_inicial()

menu_inicial()