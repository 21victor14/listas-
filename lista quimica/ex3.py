concentracao_inicial = float(input("Digite a concentração inicial em g/L: "))
concentracao_final = float(input("Digite a concentração final em g/L: "))
volume_final = float(input("Digite o volume final em mL: "))

volume_inicial = (concentracao_final * volume_final) / concentracao_inicial

print("Volume da solução inicial:", volume_inicial, "mL")
