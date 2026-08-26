def soma_lista(lista):
    soma = 0

    for numero in lista:
        soma += numero

    return soma


lista = []

for i in range(4):
    numero = float(input(f"Digite o {i + 1}º número: "))
    lista.append(numero)

resultado = soma_lista(lista)

print(f"A soma dos números é: {resultado}")
