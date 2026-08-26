import random

def embaralhar(texto):
    caracteres = list(texto)

    random.shuffle(caracteres)

    for i in range(len(caracteres)):
        if random.choice([True, False]):
            caracteres[i] = caracteres[i].upper()
        else:
            caracteres[i] = caracteres[i].lower()

    return ''.join(caracteres)


palavra = input("Digite uma palavra: ")

print("Resultado:", embaralhar(palavra))