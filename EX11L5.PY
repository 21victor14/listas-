def numero(n): 
    unidades  = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas   = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    
    if n < 10:
        return unidades[n]
    
    if n < 20:
        return especiais[n - 10] 
    
    if n < 100:
        d = n // 10
        u = n % 10
        
        if u == 0:
            return dezenas[d]
        
        return dezenas[d] + " e " + unidades[u]

    if n < 1000:
        c = n // 100
        resto = n % 100

        centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", 
                    "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

        if n == 100:
            return "cem"

        if resto == 0:
            return centenas[c]

        return centenas[c] + " e " + numero(resto)

    if n < 1000000:
        milhar = n // 1000
        resto = n % 1000

        if milhar == 1:
            texto = "mil"
        else:
            texto = numero(milhar) + " mil"

        if resto > 0:
            texto += " " + numero(resto)

        return texto


def dinheiro(valor):
    reais = int(valor)
    centavos = int(round((valor - reais) * 100))
    
    if reais == 1:
        texto = "um real"
    else:
        texto = numero(reais) + " reais"

    if centavos == 1:
        texto += " e um centavo"
    elif centavos > 1:
        texto += " e " + numero(centavos) + " centavos"

    return texto


valor = float(input("Digite um valor: "))

resultado = dinheiro(valor)

print("Resultado:", resultado)