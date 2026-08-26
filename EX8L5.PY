def converter_hora(hora_24):
    hora, minuto = hora_24.split(":")

    hora = int(hora)
    minuto = int(minuto)

    if hora == 0:
        hora_convertida = 12
        periodo = "A"
    elif hora < 12:
        hora_convertida = hora
        periodo = "A"
    elif hora == 12:
        hora_convertida = 12
        periodo = "P"
    else:
        hora_convertida = hora - 12
        periodo = "P"

    return hora_convertida, minuto, periodo


def imprimir_hora(hora, minuto, periodo):
    print(f"{hora}:{minuto:02d} {periodo}.M.")


while True:
    entrada = input("Digite a hora no formato HH:MM: ")

    hora, minuto, periodo = converter_hora(entrada)

    imprimir_hora(hora, minuto, periodo)

    continuar = input("Deseja fazer outra conversão? (s/n): ")

    if continuar.lower() != "s":
        break
