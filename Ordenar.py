email = "jose@gmail.com"

# pontos:       6          5            4      3       2      diferença tempo (+recente = +pontos)
# prioridade: senha > ajuda de senha > tel > nomes > email > data (mais recente para o mais antigo)
empresas = {
    "000webhost": ["senha", "nome", "email", "03/2015"],
    "123RF": ["senha", "tel", "nome", "email", "03/2020"],
    "500px": ["senha", "nome", "email", "06/2018"], 
    "8fit": ["senha", "nome", "email", "07/2018"],
    "8tracks": ["senha", "email", "06/2017"]
}

pontosEmpresa = {} # cria dict vazio
anoAtual = 2022
    
for empresa in empresas:
    pontosEmpresa[empresa] = 0 # cria lista de pontos a partir da lista de empresas
    
    for i in range(len(empresas[empresa])): # percorre a list de cada empresa
        match empresas[empresa][i]:
            case "senha":
                pontosEmpresa[empresa] += 6
            case "tel":
                pontosEmpresa[empresa] += 4
            case "nome":
                pontosEmpresa[empresa] += 3
            case "email":
                pontosEmpresa[empresa] += 2
    else:
        diff = anoAtual - int(empresas[empresa][i][3:7])
        decimal = int(empresas[empresa][i][0:2]) / 100
        
        match diff:
            case 1:
                pts = 10 + decimal
                pontosEmpresa[empresa] += pts
                round(pontosEmpresa[empresa], 2)
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 2:
                pts = 9 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 3:
                pts = 8 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 4:
                pts = 7 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 5:
                pts = 6 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 6:
                pts = 5 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 7:
                pts = 4 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 8:
                pts = 3 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 9:
                pts = 2 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)
            case 10:
                pts = 1 + decimal
                pontosEmpresa[empresa] += pts
                pontosEmpresa[empresa] = round(pontosEmpresa[empresa], 2)           
else:
    print(pontosEmpresa)

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