import re  # Importa o módulo utilizado para procurar padrões de texto.
import matplotlib.pyplot as plt  # Importa o módulo utilizado para criar gráficos.
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image  # Importa classes para criar o PDF, tabelas, parágrafos, espaçamentos, imagens e quebras de página.
from reportlab.lib import colors  # Importa cores para formatar a tabela.
from reportlab.lib.styles import getSampleStyleSheet  # Importa uma função que fornece estilos de texto predefinidos.

def pagina(pdf, documento):  # Define uma função para desenhar o cabeçalho e o rodapé de cada página.
    # Cabeçalho  # Indica o início da configuração do cabeçalho.
    pdf.setFont('Helvetica-Bold', 12)  # Define o tipo e o tamanho da letra do cabeçalho.
    pdf.drawCentredString(297, 800, 'RELATÓRIO DE SEGURANÇA')  # Escreve o título centrado na parte superior da página.
    
    # Rodapé  # Indica o início da configuração do rodapé.
    pdf.setFont('Helvetica', 9)  # Define o tipo e o tamanho da letra do rodapé.
    pdf.drawString(50, 30, 'Relatório de Segurança')  # Escreve o texto do rodapé no lado esquerdo.
    
    # Número de página  # Indica a configuração do número da página.
    pdf.drawRightString(545, 30, 'Página ' + str(documento.page))  # Escreve o número da página no lado direito.

def criar_grafico(utilizadores):
    contagem = {}
    for utilizador in utilizadores:  # Percorre todos os utilizadores encontrados.
        if utilizador in contagem:  # Verifica se o utilizador já está no dicionário de contagem.
            contagem[utilizador] += 1  # Incrementa a contagem do utilizador.
        else:
            contagem[utilizador] = 1  # Inicializa a contagem do utilizador.
    nomes = list(contagem.keys())  # Obtém a lista de nomes dos utilizadores.
    tentativas = list(contagem.values())  # Obtém a lista de contagens de tentativas por utilizador.
    plt.bar(nomes, tentativas)  # Cria um gráfico de barras com os nomes e as contagens.
    plt.title('Gráfico de acessos')
    plt.xlabel('Utilizadores')
    plt.ylabel('Número de tentativas')
    plt.xticks(rotation=45)  # Rotaciona os nomes dos utilizadores para melhor visualização.
    plt.savefig('grafico.png')  # Salva o gráfico como uma imagem PNG.
    plt.close()  # Fecha o gráfico para liberar memória.

utilizadores = []  # Cria uma lista vazia para guardar os nomes dos utilizadores.
ips = []  # Cria uma lista vazia para guardar os endereços IP.
mensagens = []  # Cria uma lista vazia para guardar as mensagens completas.

padrao = r'for\s+(\S+)\s+from\s+(\S+)'  # Define o padrão que procura um utilizador e um IP numa linha.

with open('auth.log', 'r', encoding='utf-8') as ficheiro:  # Abre o ficheiro auth1.log para leitura usando UTF-8.
    for linha in ficheiro:  # Percorre todas as linhas do ficheiro.
        resultado = re.search(padrao, linha)  # Procura o padrão definido na linha atual.
        if resultado:  # Verifica se foi encontrada uma correspondência.
            utilizador = resultado.group(1)  # Obtém o nome do utilizador encontrado.
            ip = resultado.group(2)  # Obtém o endereço IP encontrado.
            utilizadores.append(utilizador)  # Adiciona o utilizador à lista de utilizadores.
            ips.append(ip)  # Adiciona o IP à lista de endereços IP.
            mensagens.append(linha.strip())  # Adiciona a linha sem espaços desnecessários ou quebras de linha.

dados = []  # Cria uma lista vazia para guardar os dados da tabela.
dados.append(['Num', 'Utilizador', 'IP', 'Mensagem'])  # Adiciona os títulos das colunas da tabela.

estilos = getSampleStyleSheet()  # Obtém os estilos de texto predefinidos do ReportLab.
estilo = estilos['Normal']  # Seleciona o estilo normal para os textos.
estilo.alignment = 0  # Define o alinhamento do texto à esquerda.

for i in range(len(utilizadores)):  # Percorre os índices de todos os utilizadores encontrados.
    dados.append([i + 1, utilizadores[i], ips[i], Paragraph(mensagens[i], estilo)])  # Adiciona uma linha com o número, utilizador, IP e mensagem.

tabela = Table(dados, colWidths=[40, 100, 120, 200], repeatRows=1)  # Cria a tabela e define a largura das colunas; repete o cabeçalho em novas páginas.
tabela.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black)]))  # Adiciona uma grelha preta a todas as células da tabela.

pdf = SimpleDocTemplate('relatorio.pdf')  # Cria um documento PDF com o nome relatorio.pdf.
elementos = []  # Cria uma lista para guardar os elementos que serão colocados no PDF.
elementos.append(Paragraph('Relatório de acessos', estilo))  # Adiciona o título do relatório.
elementos.append(Spacer(1, 20))  # Adiciona um espaço vertical de 20 pontos depois do título.
elementos.append(tabela)  # Adiciona a tabela ao conteúdo do PDF.
elementos.append(PageBreak())
elementos.append(Paragraph('Análise de Gráficos', estilo))  # Adiciona o título do relatório.
elementos.append(Spacer(1, 20))  # Adiciona um espaço vertical de 20 pontos depois do título.
criar_grafico(utilizadores)  # Chama a função para criar o gráfico de acessos.
imagem=Image('grafico.png', width=400, height=300)  # Cria um objeto de imagem com o gráfico gerado.
elementos.append(imagem)  # Adiciona a imagem do gráfico ao conteúdo do PDF.

pdf.build(elementos, onFirstPage=pagina, onLaterPages=pagina)  # Gera o PDF e aplica a função pagina à primeira página e às seguintes.