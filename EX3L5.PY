import math


def volume_cilindro(raio, altura):
    return math.pi * (raio ** 2) * altura


raio = float(input("Digite o raio do cilindro em metros: "))
altura = float(input("Digite a altura do cilindro em metros: "))

volume = volume_cilindro(raio, altura)

print(f"O volume do cilindro é: {volume:.2f} m³")
