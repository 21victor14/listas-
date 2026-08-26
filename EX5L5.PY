def lista_vazia(lista):
    return len(lista) == 0


def maior_valor(lista):
    if lista_vazia(lista):
        return -1

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior


def menor_valor(lista):
    if lista_vazia(lista):
        return -1

    menor = lista[0]

    for numero in lista:
        if numero < menor:
            menor = numero

    return menor


def valor_medio(lista):
    if lista_vazia(lista):
        return -1

    return sum(lista) / len(lista)



lista_vazia_teste = []
lista_com_elementos = [10, 25, 7, 42, 18]



print("LISTA VAZIA")
print("Está vazia?", lista_vazia(lista_vazia_teste))
print("Maior valor:", maior_valor(lista_vazia_teste))
print("Menor valor:", menor_valor(lista_vazia_teste))
print("Valor médio:", valor_medio(lista_vazia_teste))



print("\nLISTA COM ELEMENTOS")
print("Lista:", lista_com_elementos)
print("Está vazia?", lista_vazia(lista_com_elementos))
print("Maior valor:", maior_valor(lista_com_elementos))
print("Menor valor:", menor_valor(lista_com_elementos))
print("Valor médio:", valor_medio(lista_com_elementos))
