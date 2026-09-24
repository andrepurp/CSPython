from SchoolProjects.logsfile import logs


def imprimir_logs():
    for log in logs:
        print(log)

def imprimir_total_registos():
    total_registos = len(logs)
    print(f"Total de registos: {total_registos}")

def estado_login():
    sucesso = 0
    falha = 0
    for log in logs:
        if "LOGIN_OK" in log:
            sucesso += 1
        else:
            falha += 1
    print(f"Existem {sucesso} registos de login bem-sucedidos.")
    print(f"Existem {falha} registos de login falhados.")

def login_falhado():
    for log in logs:
        if "LOGIN_FAIL" in log:
            print(log)

utilizadores = []

def imprimir_utilizadores():
    for log in logs:
        dados = log.split()
        utilizador = dados[1]
        if utilizador not in utilizadores:
            utilizadores.append(utilizador)
        print(utilizador)

ipsunicos = []

def imprimir_ips():
    for log in logs:
        dados = log.split()
        ips = dados[2]
        if ips not in ipsunicos:
            ipsunicos.append(ips)
        print(ips)

contagem = {}

def contar_utilizadores_xvezes():
    for log in logs:
        dados = log.split()
        utilizador = dados[1]
        if utilizador in contagem:
            contagem[utilizador] += 1
        else:   
            contagem[utilizador] = 1  
    for utilizador, vezes in contagem.items():
        print(f"{utilizador}: {vezes} vezes")

contagemips = {}

def ips_xvezes():
    for log in logs:
        dados = log.split()
        ips = dados[2]
        if ips in contagemips:
            contagemips[ips] += 1
        else:
            contagemips[ips] = 1
    for ips, vezes in contagemips.items():
        print(f"{ips}: {vezes} vezes")
    

imprimir_logs()
imprimir_total_registos()
estado_login()
login_falhado()
imprimir_utilizadores()
imprimir_ips()
contar_utilizadores_xvezes()
ips_xvezes()