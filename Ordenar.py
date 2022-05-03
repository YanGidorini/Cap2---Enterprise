'''
ALUNOS
-------------------------
| CHRISTOPHER (RM95083) |
| EVELLY      (RM96090) |
| VICTOR      (RM96141) |
| YAN         (RM96190) |
-------------------------
'''

# pontos:       60          50         40     30      20      diferença tempo (+recente = +pontos)
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
    "newideas": ["senha","email", "05/2013"],
    "animaljam": ["tel", "nome", "06/2017"],
    "animoto": ["email", "tel", "nome", "senha", "03/2018"],
    "bigbasket": ["senha", "email", "nome", "tel", "02/2021"],
    "epik": ["email", "senha", "05/2013"],
    "gett": ["senha", "email", "tel", "08/2017"],
    "houzz": ["email", "09/2013"],
    "pixlr": ["tel", "06/2009"],
    "quidd": ["nome","email", "tel", "senha", "06/2021"],
    "younoww": ["email", "tel", "03/2014"],
    "zynga": ["tel", "05/2019"],
    "yatra":["nome", "email", "06/2009"],
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
        elif diff == 3:
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
    ordenado = sorted(pontosEmpresa.values(), reverse=True) #pegando os pontos e organizando eles de forma decrescente
    resultado = {} #dicionário vazio onde será armazenado a empresa e seus pontos, de forma já ordenada
    
    #Guardando em um dict o nome da empresa e seu nome de forma ordenada
    for pontos in ordenado:
        for item in pontosEmpresa:
            if pontos == pontosEmpresa[item]:
                resultado[item] = pontos
    
    #Mostrando no console a lista ordenada
    print("LISTA ORDENADA")
    print("---------------------------------------------------")
    for item in resultado:
        for empresa in empresas:
            if item == empresa:
                print(f"{item}: {empresas[empresa]}")