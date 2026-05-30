'''
Para alimentar uma analise exploratoria/estatistica de dados sugere-se o seguinte cntexto de trabalho:

1. Carregamento e compreensão dos dados 

2. Analise Estatistica descritiva

3. Exploração da distribuição dos dados

4. Filtragem condicional

5. Relação entre as variaveis

6. Normalização e padronização dos dados
'''

# para esta analise exploratoria vamos usar alguns recursos importantes:
# numpy, matplotlib.pyplot, seaborn
import numpy as np # lib numerica python
import matplotlib.pyplot as plt # lib de graficos 2 python
import seaborn as sns # fazer uso do seaborn para "melhorar" os gráficos e a organização de informações para visualização

'''
BLOCO I - 1. Carregamento e compreensão dos dados 
'''
# passo 1: carregar os dados - para este proposito vamos definir uma variavel para receber como valor no nosso dataset
dados = np.genfromtxt('iris_com_colunas.csv', delimiter=',', dtype=None, encoding='utf-8', names=True, invalid_raise=False)
print()
print(dados)
print()

# -------------------------------------------------------------------------

# passo 2: exibir os nomes das colunas
print('Colunas: ', dados.dtype.names)
print()

# passo 3: exibir um determinado intervalo a partir do dataset
print('Intervalo gerado: ')
print(dados[:5])
print()

# -----------------------------------------------------------------
'''
BLOCO II - 2. Analise Estatistica descritiva
'''
# passo 4: implementar algumas operações estatisticas e para este proposito vamos criar algumas variaveis - as 5 variaveis recebem , respectivamente, como valor cada uma das colunas do dataset
sepal_length  =  dados['sepal_length']
sepal_width = dados['sepal_width']
petal_length = dados['petal_length']
petal_width = dados['petal_width']
species = dados['species']

# passo 5: implementação da analise descritiva/estatistica
print('----------- Analise descritiva/Estatistica ----------------')

media_sepal_length = np.mean(sepal_length)
media_sepal_width = np.mean(sepal_width)
media_petal_length = np.mean(petal_length)
media_petal_width = np.mean(petal_width)

# exibir os valores das vars
print(f'Média do comprimento da sépala: {media_sepal_length:.2f}')
print(f'Média da largura da sépala: {media_sepal_width:.2f}')

print(f'Média do comprimento da pétala: {media_petal_length:.2f}')
print(f'Média da largura da pétala: {media_petal_width:.2f}')
print()

# passo 6: filtrar os dados por especie - precisamos acessar a coluna respectiva; na sequencia, vamos aplicar um tratamento/limpeza nos dados encontrados
especies = np.char.strip(dados['species'].astype(str), ' " ')
'''
np.char: significa que estamos acessando um caractere em especifico

strip: função que remove espaços, aspas duplas e outros quaisquer caracteres "indesejados" do inicio e fim de cada string

dados['species']: aqui, selecionamos a coluna respectiva para aplicar a limpeza de dados

astype(str): é uma função de asserção/conversão -> converte valores da coluna para o tipo string - caso estejam em outro formato
'''
print('Coluna spiecies tratada')
print(especies)
print()

# ---------------------------------------------------------------------

# passo 7: definir uma variavel para acessar a coluna species e selecionar uma especie especifica
setosa =  dados[especies == 'Setosa'] 
print('\nDados da especie Iris-Setosa: \n ', setosa)
print()
# passo 8: definir uma var para atribuir como valor o calculo da media somentes da especie setosa
media_setosa_sepal_length = np.mean(setosa['sepal_length'])
media_setosa_sepal_width = np.mean(setosa['sepal_width'])

# exibir o resultado do calculo
print(f'Media do comprimento da sépala da Setosa: {media_setosa_sepal_length:.2f}')
print(f'Media do largura da sépala da Setosa: {media_setosa_sepal_width:.2f}')
print()


# --------------------------------------------------------------------
# passo 9: observação do uso da função np.unique() para operar com valores unicos
especies_unicas = np.unique(especies)
print('Valor da var especies_unicas: ', especies_unicas)
