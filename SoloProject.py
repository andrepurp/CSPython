import re
import matplotlib.pyplot as plt
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

utilizadores = []
ips = []
mensagens = []
data = []

padrao = r"for\s+(\S+)\s+from\s+(\S+)"
padraodata = r"(\w{3}\s+\d{1,2}\s+\d{2}.\d{2}.\d{2})"
with open('auth.log', 'r', encoding='utf-8') as ficheiro:
    for linha in ficheiro:
        resultado = re.search(padrao, linha)
        resultadodata = re.search(padraodata, linha)
        utilizadores.append(resultado.group(1))
        ips.append(resultado.group(2))
        mensagens.append(linha.strip())
        data.append(resultadodata.group(1))
        print(f"Utilizador: {resultado.group(1)} \nIP: {resultado.group(2)} \nData: {resultadodata.group(0)}\nMensagem: {linha.strip()}  \n")