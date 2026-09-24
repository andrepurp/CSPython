import pandas as pd

print("Pandas version:", pd.__version__)

dados = {"Nome": ["Ana", "Carlos", "Sandra", "João", "Maria", "Pedro", "Sofia", "Ricardo", "Inês", "Miguel", "Rita", "Bruno", "Carla", "Tiago", "Beatriz"],
    "Idade": [20, 22, 21, 19, 23, 24, 20, 25, 22, 21, 19, 23, 24, 20, 22],
    "Curso": ["CTESP", "TESP", "CTESP", "EFA", "CTESP", "TESP", "CTESP", "EFA", "TESP", "CTESP", "EFA", "TESP", "CTESP", "EFA", "TESP"]}

df = pd.DataFrame(dados)

print(df.iloc[0:5])

print(len(df))

