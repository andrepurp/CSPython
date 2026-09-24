import re
import matplotlib.pyplot as plt
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

utilizadores = []
ips = []
mensagens = []
data = []
servidor = []

padraofinal = (
    r"(?P<data>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+"
    r"(?P<servidor>\w+)\s+"
    r"sshd\[\d+\]:\s+"
    r"(?P<estado>Accepted|Failed)\s+password\s+for\s+"
    r"(?P<utilizador>\S+)\s+from\s+"
    r"(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\s+port\s+"
    r"(?P<porta>\d+)\s+ssh2"
)

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        resultado = re.search(padraofinal, linha)

        if resultado:
            dados = resultado.groupdict()

            utilizadores.append(dados["utilizador"])
            ips.append(dados["ip"])
            mensagens.append(linha.strip())
            data.append(dados["data"])
            servidor.append(dados["servidor"])

            print(
                f"Utilizador: {dados['utilizador']}\n"
                f"IP: {dados['ip']}\n"
                f"Data: {dados['data']}\n"
                f"Servidor: {dados['servidor']}\n"
                f"Estado: {dados['estado']}\n"
                f"Porta: {dados['porta']}\n"
                f"Mensagem: {linha.strip()}\n"
            )