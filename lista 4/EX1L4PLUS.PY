professores = {
    "001": "Prof Thiago Paes",
    "002": "Prof Schalata",
    "003": "Prof Ignácio",
    "004": "Prof Ryan",
    "005": "Prof André",
    "006": "Prof Fabiana",
    "007": "Prof Alberto",
    "008": "Prof Juliano",
    "009": "Prof Thiago Waltrik",
    "010": "Prof João Eduardo"
}

acessos = {
    "Lab102": ["003", "001", "004", "005", "006"],
    "Lab103": ["007"],
    "Lab104": ["004", "008", "002", "005"],
    "Lab105": ["003", "007", "009", "001"],
    "Lab106": ["002", "003", "009", "001"],
    "Lab107": ["005", "002", "009", "001", "010"]
}

while True:

    print("\nMENU")
    print("1 - Adicionar professor")
    print("2 - Alterar professor")
    print("3 - Excluir professor")
    print("4 - Listar professores")
    print("5 - Adicionar acesso")
    print("6 - Alterar acesso")
    print("7 - Excluir acesso")
    print("8 - Listar acessos")
    print("9 - Testar acesso")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        codigo = input("Digite o código do professor: ")

        if codigo in professores:
            print("Esse código já existe")

        else:
            nome = input("Digite o nome do professor: ")

            professores[codigo] = nome

            print("Professor cadastrado")

    elif opcao == "2":

        codigo = input("Digite o código do professor: ")

        if codigo in professores:

            nome = input("Digite o novo nome: ")

            professores[codigo] = nome

            print("Professor alterado")

        else:
            print("Professor não encontrado")

    elif opcao == "3":

        codigo = input("Digite o código do professor: ")

        if codigo in professores:

            del professores[codigo]

            for laboratorio in acessos:

                lista = acessos[laboratorio]

                if codigo in lista:
                    lista.remove(codigo)

            print("Professor excluído")

        else:
            print("Professor não encontrado")

    elif opcao == "4":

        print("\nLista de professores")

        for codigo in professores:

            nome = professores[codigo]

            print(codigo, nome)

    elif opcao == "5":

        codigo = input("Digite o código do professor: ")
        laboratorio = input("Digite o laboratório: ")

        if codigo not in professores:

            print("Professor não cadastrado")

        else:

            if laboratorio not in acessos:

                print("Laboratório não existe")

            else:

                lista = acessos[laboratorio]

                if codigo in lista:

                    print("Acesso já existe")

                else:

                    lista.append(codigo)

                    print("Acesso cadastrado")

    elif opcao == "6":

        codigo = input("Código do professor: ")

        antigo = input("Laboratório atual: ")

        novo = input("Novo laboratório: ")

        if codigo not in professores:

            print("Professor não cadastrado")

        elif antigo not in acessos:

            print("Laboratório atual não existe")

        elif codigo not in acessos[antigo]:

            print("Professor não possui acesso")

        elif novo not in acessos:

            print("Novo laboratório não existe")

        elif codigo in acessos[novo]:

            print("Professor já possui acesso ao novo laboratório")

        else:

            acessos[antigo].remove(codigo)
            acessos[novo].append(codigo)

            print("Acesso alterado")

    elif opcao == "7":

        codigo = input("Código do professor: ")

        laboratorio = input("Laboratório: ")

        if laboratorio in acessos:

            lista = acessos[laboratorio]

            if codigo in lista:

                lista.remove(codigo)

                print("Acesso removido")

            else:

                print("Acesso não encontrado")

        else:

            print("Laboratório não existe")

    elif opcao == "8":

        for laboratorio in acessos:

            print("\n", laboratorio)

            lista = acessos[laboratorio]

            for codigo in lista:

                nome = professores[codigo]

                print(codigo, nome)

    elif opcao == "9":

        laboratorio = input("Digite o laboratório: ")

        codigo = input("Digite o código do professor: ")

        if laboratorio in acessos:

            lista = acessos[laboratorio]

            if codigo in lista:

                print("Acesso permitido")

            else:

                print("Acesso negado")

        else:

            print("Laboratório não existe")

    elif opcao == "0":

        print("Programa encerrado")

        break

    else:

        print("Opção inválida")