def desenhar_moldura(linhas=1, colunas=1):
    
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    
    if linhas == 1:
        print("+" + "-" * colunas + "+")
        return

   
    print("+" + "-" * colunas + "+")

   
    for i in range(linhas - 2):
        print("|" + " " * colunas + "|")

    
    print("+" + "-" * colunas + "+")


linhas = int(input("Digite a quantidade de linhas (1 a 20): "))
colunas = int(input("Digite a quantidade de colunas (1 a 20): "))

desenhar_moldura(linhas, colunas)
