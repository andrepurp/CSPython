import datetime
import re
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------------------------------------------------
# a) e b) Abertura do ficheiro, leitura linha a linha e extração por Regex
# -----------------------------------------------------------------------------
log_pattern = re.compile(
    r'([A-Z][a-z]{2}\s+\d+\s+\d{2}:\d{2}:\d{2}).*?\b(Accepted|Failed)\b.*?\bfor\s+(?:invalid user\s+)?(\S+)\s+from\s+(\d{1,3}(?:\.\d{1,3}){3})'
)

registos = []
ano_atual = datetime.datetime.now().year

with open('auth.log', 'r', encoding='utf-8') as ficheiro:
  for linha in ficheiro:
    match = log_pattern.search(linha)
    if match:
      data_str, estado, utilizador, ip = match.groups()

      # -------------------------------------------------------------------------
      # c) Conversão da data e hora para objeto datetime
      # -------------------------------------------------------------------------
      data_str_clean = ' '.join(data_str.split())
      data_dt = datetime.datetime.strptime(
          data_str_clean, '%b %d %H:%M:%S'
      ).replace(year=ano_atual)

      registos.append({
          'Data': data_dt,
          'Utilizador': utilizador,
          'IP': ip,
          'Estado': estado,
      })

# -----------------------------------------------------------------------------
# d) Criação do DataFrame
# -----------------------------------------------------------------------------
df = pd.DataFrame(registos, columns=['Data', 'Utilizador', 'IP', 'Estado'])

# -----------------------------------------------------------------------------
# e) Apresentar o DataFrame no ecrã
# -----------------------------------------------------------------------------
print('=== e) DataFrame de Registos ===')
print(df)
print('\n' + '=' * 60 + '\n')

# -----------------------------------------------------------------------------
# f) Total de acessos registados
# -----------------------------------------------------------------------------
total_acessos = len(df)
print(f'f) Número total de acessos registados: {total_acessos}\n')

# -----------------------------------------------------------------------------
# g) Acessos Accepted vs Failed
# -----------------------------------------------------------------------------
contagem_estado = df['Estado'].value_counts()
accepted_count = contagem_estado.get('Accepted', 0)
failed_count = contagem_estado.get('Failed', 0)

print(
    f'g) Resultado dos Acessos:\n   - Accepted: {accepted_count}\n   - Failed:'
    f' {failed_count}\n'
)

# -----------------------------------------------------------------------------
# h) Acessos totais por utilizador
# -----------------------------------------------------------------------------
print('h) Acessos por utilizador:')
for user, qtd in df['Utilizador'].value_counts().items():
  print(f'   {user} -> {qtd} acessos')
print()

# -----------------------------------------------------------------------------
# i) Tentativas Failed por utilizador
# -----------------------------------------------------------------------------
df_failed = df[df['Estado'] == 'Failed']
failed_por_user = df_failed['Utilizador'].value_counts()

print('i) Tentativas Failed por utilizador:')
for user, qtd in failed_por_user.items():
  print(f'   {user} -> {qtd} acessos falhados')
print()

# -----------------------------------------------------------------------------
# l) Utilizador com mais tentativas falhadas
# -----------------------------------------------------------------------------
top_user_failed = failed_por_user.idxmax()
max_failed_attempts = failed_por_user.max()
print(
    f'l) Utilizador com mais falhas: {top_user_failed} ({max_failed_attempts}'
    ' tentativas)\n'
)

# -----------------------------------------------------------------------------
# m) Endereço IP mais frequente
# -----------------------------------------------------------------------------
top_ip = df['IP'].mode()[0]
top_ip_count = (df['IP'] == top_ip).sum()
print(f'm) IP mais frequente: {top_ip} ({top_ip_count} registos)\n')

# -----------------------------------------------------------------------------
# n) Apenas registos de acessos Failed
# -----------------------------------------------------------------------------
print('n) Registos de acessos Failed:')
print(df_failed)
print('\n' + '=' * 60 + '\n')

# -----------------------------------------------------------------------------
# o) Acessos realizados depois das 09:00
# -----------------------------------------------------------------------------
df_apos_09 = df[df['Data'].dt.time > datetime.time(9, 0, 0)]
print('o) Registos de acessos realizados depois das 09:00:')
if df_apos_09.empty:
  print('   Nenhum acesso registado após as 09:00 neste ficheiro.')
else:
  print(df_apos_09)
print('\n' + '=' * 60 + '\n')

# -----------------------------------------------------------------------------
# j) Gráfico 1: Acessos Accepted vs Failed
# -----------------------------------------------------------------------------
plt.figure(figsize=(7, 4))
plt.bar(
    contagem_estado.index,
    contagem_estado.values,
    color=['#d62728', '#2ca02c'],
    edgecolor='black',
)
plt.title('Acessos Registados: Accepted vs Failed')
plt.xlabel('Estado da Autenticação')
plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# k) Gráfico 2: Tentativas Failed por Utilizador
# -----------------------------------------------------------------------------
plt.figure(figsize=(8, 4))
plt.bar(
    failed_por_user.index,
    failed_por_user.values,
    color='#ff7f0e',
    edgecolor='black',
)
plt.title('Tentativas de Acesso Falhadas (Failed) por Utilizador')
plt.xlabel('Utilizador')
plt.ylabel('Tentativas Falhadas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()