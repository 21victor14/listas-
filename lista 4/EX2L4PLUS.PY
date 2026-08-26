condutores = {
    "001": "Roberto Souza",
    "002": "João Graciano",
    "003": "Karine Silva",
    "004": "Pedro Luiz",
    "005": "Maria Catarina",
    "006": "Júlio Cardoso",
    "007": "Altivo Antônio",
    "008": "Jorge Gonçalves",
    "009": "Marcos Vinícius",
    "010": "Heleno Nunes",
    "011": "Mara Cristina",
    "012": "Otávio Rocha"
}

veiculos = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 5160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40s14",
    "008": "Iveco Tector 310E28"
}

registros = []

while True:

    print("\nALPHA ENTREGAS")
    print("1 - Registrar saída")
    print("2 - Registrar retorno")
    print("3 - Consultar caminhão")
    print("4 - Listar caminhões")
    print("5 - Listar condutores")
    print("6 - Listar retornados")
    print("7 - Verificar entregas")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        caminhao = input("Código do caminhão: ")
        condutor = input("Código do condutor: ")

        if caminhao in veiculos and condutor in condutores:

            aberto = False

            for registro in registros:
                if registro[0] == caminhao and registro[3] == "":
                    aberto = True

            if aberto:
                print("Este caminhão ainda está na rua!")

            else:
                data_saida = input("Digite a data e hora da saída: ")

                registro = [caminhao, condutor, data_saida, ""]
                registros.append(registro)

                print("Saída registrada!")

        else:
            print("Código inválido!")

    elif opcao == "2":

        caminhao = input("Código do caminhão: ")

        achou = False

        for registro in registros:

            if registro[0] == caminhao and registro[3] == "":

                data_retorno = input("Digite a data e hora do retorno: ")

                registro[3] = data_retorno

                achou = True

                print("Retorno registrado!")

        if achou == False:
            print("Caminhão não encontrado ou já retornou.")

    elif opcao == "3":

        caminhao = input("Código do caminhão: ")

        if caminhao in veiculos:

            achou = False

            for registro in registros:

                if registro[0] == caminhao:

                    achou = True

                    print("\nCaminhão:", veiculos[caminhao])
                    print("Condutor:", condutores[registro[1]])
                    print("Saída:", registro[2])

                    if registro[3] == "":
                        print("Ainda não retornou.")
                    else:
                        print("Retorno:", registro[3])

            if achou == False:
                print("Nenhum registro encontrado.")

        else:
            print("Caminhão não encontrado!")

    elif opcao == "4":

        print("\nCAMINHÕES")

        for codigo in veiculos:
            print(codigo, "-", veiculos[codigo])

    elif opcao == "5":

        print("\nCONDUTORES")

        for codigo in condutores:
            print(codigo, "-", condutores[codigo])

    elif opcao == "6":

        print("\nCAMINHÕES QUE RETORNARAM")

        achou = False

        for registro in registros:

            if registro[3] != "":

                achou = True

                print("Caminhão:", veiculos[registro[0]])
                print("Condutor:", condutores[registro[1]])
                print("Retorno:", registro[3])

        if achou == False:
            print("Nenhum caminhão retornou.")

    elif opcao == "7":

        if len(registros) == 0:

            print("Nenhuma entrega registrada.")

        else:

            tudo = True

            for registro in registros:

                if registro[3] == "":
                    tudo = False

            if tudo:
                print("Todas as entregas foram realizadas!")
            else:
                print("Ainda existem caminhões na rua.")

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")