def data_extenso(data):
        meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])
        
        resultado = str(dia) + " de "
        resultado = resultado + meses[mes]
        resultado = resultado + " de " + str(ano)
        return resultado

data = input("Digite uma data (DD/MM/AAAA): ")
print(data_extenso(data))
