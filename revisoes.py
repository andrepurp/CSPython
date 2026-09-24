import re
import csv
from datetime import datetime

acessos = [
    ["192.168.1.10", "16/09/2026 08:30:15", "PC-01"],
    ["192.168.1.25", "16/09/2026 08:35:42", "PC-02"],
    ["10.0.0.15", "16/09/2026 08:41:03", "PC-03"],
    ["192.168.1.30", "16/09/2026 08:52:27", "PC-04"],
    ["172.16.0.20", "16/09/2026 09:05:11", "PC-05"],
    ["192.168.1.50", "16/09/2026 09:12:36", "PC-06"],
    ["10.0.0.25", "16/09/2026 09:20:18", "PC-07"],
    ["192.168.1.75", "16/09/2026 09:28:49", "PC-08"]
]

padrao = r"^(\d{1,3}\.){3}\d{1,3}$"
agora = datetime.now()
print(agora)

for acesso in acessos:
    ip = acesso[0]
    data = acesso[1]
    computador = acesso[2]

    if re.match(padrao, ip):
        estado = 'IP válido'
    else:
        estado = 'IP inválido'
    print(f"IP: {ip} - Data: {data} - Computador: {computador} - Estado: {estado}")

with open('acessos.csv', mode='w', newline='', encoding='utf-8') as ficheiro:
    escritor = csv.writer(ficheiro, delimiter=';')
    escritor.writerow(['IP', 'Data', 'Computador', 'Estado '])
    for acesso in acessos:
        escritor.writerow(acesso)

    ip = acesso[0]
    data = acesso[1]
    computador = acesso[2]

    if re.match(padrao, ip):
        estado = 'IP válido'
    else:
        estado = 'IP inválido'

    escritor.writerow([ip, data, computador, estado])

with open('acessos.csv', mode='r', encoding='utf-8') as ficheiro:
    leitor = csv.reader(ficheiro, delimiter=';')
    for linha in leitor:
        print(linha)