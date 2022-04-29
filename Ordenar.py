from tkinter import E


# email = "jose@gmail.com"

# pontos:       6          5            4      3       2      diferença tempo (+recente = +pontos)
# prioridade: senha > ajuda de senha > tel > nomes > email > data (mais recente para o mais antigo)
empresas = {
    "000webhost": ["senha", "nome", "email", "03/2015"],
    "123RF": ["senha", "tel", "nome", "email", "03/2020"],
    "500px": ["senha", "nome", "email", "06/2018"],
    "8fit": ["senha", "nome", "email", "07/2018"],
    "8tracks": ["tel", "nome", "email", "06/2021"],
    "devsfiap": ["nome", "email", "08/2016"],
    "orocle": ["senha", "tel", "email", "05/2015"],
    "semnai": ["tel", "nome", "03/2019"],
}

pontosEmpresa = {}  # cria dict vazio
anoAtual = 2022

for empresa in empresas:
    # cria lista de pontos a partir da lista de empresas
    pontosEmpresa[empresa] = 0

    for i in range(len(empresas[empresa])):  # percorre a list de cada empresa
        if empresas[empresa][i] == "senha":
            pontosEmpresa[empresa] += 60
        
        if empresas[empresa][i] == "tel":
            pontosEmpresa[empresa] += 40

        if empresas[empresa][i] == "nome":
            pontosEmpresa[empresa] += 30

        if empresas[empresa][i] == "email":
            pontosEmpresa[empresa] += 20 
    else:
        diff = anoAtual - int(empresas[empresa][i][3:7])
        decimal = int(empresas[empresa][i][0:2]) / 100

        if diff == 1:
                pts = 10 + decimal
                pontosEmpresa[empresa] += pts
                round(pontosEmpresa[empresa], 2)
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 2:
                pts = 9 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff== 3:
                pts = 8 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 4:
                pts = 7 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 5:
                pts = 6 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 6:
                pts = 5 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 7:
                pts = 4 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 8:
                pts = 3 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 9:
                pts = 2 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
        elif diff == 10:
                pts = 1 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
else:

    print(pontosEmpresa) #vendo quantos pontos cada empresa tem
    ordenado = sorted(pontosEmpresa.values(), reverse=True)
    print(ordenado) #ordenando de forma decrescente

    print("A ordem da lista ordenada agora é: ")
    for pontos in ordenado:
        for empresa in pontosEmpresa:
            if pontos == pontosEmpresa[empresa]:
                print("------------------------------")
                print("Empresa: ", empresa, "\nObteve ", pontos , "pontos e teve os seguintes dados vazados: ")
                # percorre a list de cada empresa
                for i in range(len(empresas[empresa])):
                    match empresas[empresa][i]:
                        case "senha":
                            print("Senha.")
                        case "tel":
                            print("Telefone.")
                        case "nome":
                            print("Nome.")
                        case "email":
                            print("E-mail.")

# 2  10
# 3  9
# 4  8
# 5  7
# 6  6
# 7  5
# 8  4
# 9  3
# 10 2

# pontosEmpresa = {
#     "000webhost": 0,
#     "123RF": 0,
#     "500px": 0,
#     "8fit": 0,
#     "8tracks": 0
# }

''' 
como precisa ficar
organizado = {
    "123RF": ["senha", "tel", "nome", "email", "03/2020"] 24.03pts +,
    "8fit": ["senha", "nome", "email", "07/2018"] 18.07pts +,
    "500px": ["senha", "nome", "email", "06/2018"] 18.06pts +,
    "000webhost": ["senha", "nome", "email", "03/2015"] 15.03tps +,
    "8tracks": ["senha", "email", "06/2017"] 14.06pts +,
}
'''
