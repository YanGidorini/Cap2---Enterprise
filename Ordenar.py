# pontosEmpresa = {
#     "000webhost": 0,
#     "123RF": 0,
#     "500px": 0, 
#     "8fit": 0,
#     "8tracks": 0
# }
var = "yan"
var2 = "2022"
print(int(var))

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

''' 
como precisa ficar
organizado = {
    "123RF": ["senha", "tel", "nome", "email", "03/2020"] 25pts,
    "8fit": ["senha", "nome", "email", "07/2018"] 19.07pts,
    "500px": ["senha", "nome", "email", "06/2018"] 19.06pts,
    "000webhost": ["senha", "nome", "email", "03/2015"] 16pts,
    "8tracks": ["senha", "email", "06/2017"] 15pts,
}
'''