# importação das libs necessarias
import pandas as pd
import numpy as np

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