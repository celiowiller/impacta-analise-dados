# importação das libs necessarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# passo 1: carregar os dados 
df = pd.read_excel('vendas.xlsx')
print('ler as primeiras do df')
print(df.head(5))
print('--------------------------')
print('Exibindo df')
print(df)
print()
# passo 2: resumo estatistico do dataset
print('Resumo estatistico')
print(df.describe())
print()
# passo 3: operação do fluxo - a partir do dataset
print('OPERAÇÃO 1 - QUANTIDADE DE PRODUTOS VENDIDOS POR REPRESENTANTE')
total_vendas_por_rep = df.groupby(['Rep'])[['Quantity']].sum()
print()
print('\nTotal de vendas de produto por representante\n')
print(total_vendas_por_rep)
print()

'''
total_vendas_por_rep: variavel que recebe como valor a totalização de vendas por representante

df.groupby(['Rep']): este trefho "agrupa" o Dataframe - df - com base na coluna 'Rep' - coluna dos representantes de venda; cada grupo, agora, contem todas as linhas de vendas feitas por um mesmo representante

[['Quantity']]: aqui, estamos praticando a seleção apenas da coluna "Quantity" do df para fazer as operações numéricas; [[ ]] ao usar os caracteres colchetes duplos estamos retornando - desta seleção -um "pequeno" Dataframe (inves de uma Series)

.sum(): para finalizar a operação, estamos aplicando - ao agrupamento - o uso da função sum() - aplicada sobre a coluna Quantity;então, dessa forma, estamos fazendo a soma total da quantidade de produtos vendidos para cada representante
'''

print('total de vendas realizado por cada um dos representantes * precisamos deste dado')
qtde_vendas_por_rep = df.groupby('Rep').size()
print()
print(qtde_vendas_por_rep)
print()

print('OPERAÇÃO 2 - MÉDIA DE VENDAS POR REPRESENTANTE')
media_vendas_por_rep = df.groupby(['Rep'])[['Quantity']].mean()
print()
print('\nMédia de vendas de produto por representante\n')
print(media_vendas_por_rep)
print()

'''
aqui, o valor obtido da média - .mean() - considera, para o resultado, o total de produtos vendidos pelo total de qtde de vendas realizado por cada um dos representantes

'''

# **** teste Alexandre
alexandre = df.groupby('Rep')['Quantity'].agg(
    Qtde_T_Vendas = 'count', # o size tambem mpode funcionar 
    Qtde_T_Produtos = 'sum',
    Media_P_Rep = 'mean'
)

print('Teste Alexandre - com participação do celio:')
print(alexandre)


print('----------------------------------------------------------------')
print()
print('OPERAÇÃO 3 - CRIAR UMA NOVA COLUNA NO DF')

# esta nova coluna vai armazenar o valor de totalização de vendas
df['Total_Sales'] = df['Quantity'] * df['Price']
print()
print('Dataframe com a coluna Total_Sales adicionada\n')
print(df[['Rep', 'Product', 'Quantity', 'Price', 'Total_Sales']].head())

print('----------------------------------------------------------------')
print()
print('OPERAÇÃO 4 - CRIAR UMA NOVA COLUNA NO DF - CLASSIFCAÇÃO DE VENDAS')

print('função para classificar vendas')
def classificar_vendas(preco):
    if preco >= 30000:
        return 'Alto'
    elif preco >= 10000:
        return 'Medio'
    else:
        return 'Baixo'

# criar a coluna de classificação
df['Classificacao_Vendas'] = df['Price'].apply(classificar_vendas)
print()
print('Dataframe com a colna Classificacao_Vendas\n')
print(df[['Price', 'Classificacao_Vendas']].head())
print()

print('----------------------------------------------------------------')
print()
print('OPERAÇÃO 5 - CRIAR UMA NOVA COLUNA NO DF - PARA DATAS')
print()

# verificar as colunas disponiveis no df
print(df.columns)
print()

# se não houver a ocorrencia da coluna Data(Date) será possivel 
# adiciona-la manualmente

if 'Date' not in df.columns and 'Data' not in df.columns:
    # criar uma coluna com datas a partir de um sequencia
    #df['Date'] = pd.to_datetime('2025-06-01')
    '''
    df['Date'] = pd.date_range(
        start = '2025-06-01',
        end = '2026-05-30',
        periods = len(df) # aqui, estamos dizendo que: os dados do df serão espalhados
        # por todo o intervalo de tempo
    )
    '''

    df['Date'] = pd.date_range(
        start = '2025-06-01',        
        periods = len(df), # aqui, estamos dizendo que: os dados do df serão espalhados
        # por todo o intervalo de tempo
        freq = 'ME' # Month End -> fim de mês
    )
    print('\nAdicionando coluna com datas fixas')

# converte a coluna 'Date' para o formato datetime
df['Date'] = pd.to_datetime(df['Date'])

# agrupar as vendas por trimestre
vendas_por_trimestre = df.resample('QE', on = 'Date')['Total_Sales'].sum()
# resample() -> função que reorganiza dados temporais, semelhante ao groupby()
# QE -> Quarter End (fim de trimestre)
print()
print(vendas_por_trimestre)

print('----------------------------------------------------------------')
print()
print('OPERAÇÃO 6 - GRAFICO DE TOTAL DE VENDAS POR REPRESENTANTE')
print()

plt.figure(figsize = (10, 6))
df.groupby('Rep')['Total_Sales'].sum().plot(kind = 'bar', color = 'lightgreen')
plt.title('Total de vendas por Representante')
plt.xlabel('Representantes')
plt.ylabel('Total em R$')

plt.xticks(rotation = 45) # rotaciona os labels em 45 graus
plt.grid(axis = 'y')
plt.tight_layout()
plt.show()




print('----------------------------------------------------------------')
print()
print('OPERAÇÃO 7 - TOTAL DE VENDAS DE PRODUTOS')
print()

plt.figure(figsize = (10, 6))
df.groupby('Product')['Quantity'].sum().plot(kind = 'bar', color = 'orange')
plt.title('Qtde Vendida de Produtos')
plt.xlabel('Produto')
plt.ylabel('Qtde')

plt.xticks(rotation = 45) # rotaciona os labels em 45 graus
plt.grid(axis = 'y')
plt.tight_layout()
plt.show()


print('----------------------------------------------------------------')
print()
print('OPERAÇÃO 8 - EVOLUÇÃO TRIMESTRAL DE VENDAS')
print()

# acessar a var vendas_por_trimestre e gerar o grafico
vendas_por_trimestre.plot(marker = 'o', linestyle = '-', color = 'purple')
plt.title('Evolução de vendas - trimestral')
plt.xlabel('Trimestre')
plt.ylabel('Total de vendas (R$)')

plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------- EXTRAS# 
#  calculo da variancia e desvio padrão dos preços
variancia_preco = df['Price'].var()
desvio_padrao_preco = df['Price'].std()
print('\nVariância dos preços: ', variancia_preco)
print('\nDevio padrão dos preços: ', desvio_padrao_preco)

print()
print('-----------------------------------------------------------------------')

#  analise da correlação 
correlacao = df[['Price', 'Quantity', 'Total_Sales']].corr()
print('Correlação entre Preço, Quantidade e Vendas totais')
print(correlacao)

print()
print('-----------------------------------------------------------------------')


# Boxplot dos Preços por Produto

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Product', y='Price', palette='Set2')
plt.title('Boxplot de Preços por Produto')
plt.xlabel('Produto')
plt.ylabel('Preço (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Heatmap de Correlação

plt.figure(figsize=(8,6))
sns.heatmap(df[['Price', 'Quantity', 'Total_Sales']].corr(), annot=True, cmap='Blues', fmt='.2f')
plt.title('Mapa de Correlação entre Preço, Quantidade e Vendas Totais')
plt.tight_layout()
plt.show()


# Classificação de Vendas (Alto, Médio, Baixo)

plt.figure(figsize=(6,5))
sns.countplot(data=df, x='Classificação_Vendas', palette='pastel', order=['Baixo', 'Medio', 'Alto'])
plt.title('Classificação das Vendas por Faixa de Preço')
plt.xlabel('Classificação')
plt.ylabel('Quantidade de Ocorrências')
plt.tight_layout()
plt.show()