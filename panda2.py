import pandas as pd

df = pd.read_csv('alunos.txt', sep=';')

with open('alunos.txt', 'r', encoding='utf-8') as ficheiro:
    for linha in ficheiro:
        print(linha.strip())
