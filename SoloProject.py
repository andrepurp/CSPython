import re
import matplotlib.pyplot as plt
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

utilizadores = []
ips = []
mensagens = []

padrao = 

with open('auth.log', 'r', encoding='utf-8') as ficheiro:
    for linha in ficheiro:
        print(linha.strip())