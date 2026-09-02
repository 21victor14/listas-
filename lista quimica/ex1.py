massa_inicial = float(input("Digite a massa inicial em gramas: "))
meias_vidas = int(input("Digite o número de meias-vidas: "))

massa_final = massa_inicial * (1 / 2) ** meias_vidas

print("Massa final:", massa_final, "g")