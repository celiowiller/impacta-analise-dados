'''
Para alimentar uma analise exploratoria/estatistica de dados sugere-se o seguinte cntexto de trabalho:

1. Carregamento e compreensão dos dados 
Leitura do CSV com nomes de colunas.
Identificação e exibição das colunas.


2. Analise Estatistica descritiva
Cálculo de média, mediana, desvio padrão, variância, mínimos e máximos.
Análise por espécie (ex.: média do comprimento da pétala para Setosa, Versicolor, Virginica).

3. Exploração da distribuição dos dados
Contagem de cada espécie.
Cálculo de quartis (Q1, Q2, Q3).


4. Filtragem condicional
Seleção de registros com comprimento da sépala maior que 5.0.


5. Relação entre as variaveis
Correlação entre comprimento e largura da pétala.
Matriz de correlação entre todas as variáveis numéricas.


6. Normalização e padronização dos dados
Aplicação de normalização min-max e padronização (z-score) para futuras análises.
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

'''
np.genformtxt(...): é uma função numpy usada para ler arquivos de texto como, por exemplo, .csv

'iris_com_colunas.csv': nome do arquivo de dados que estamos carregando

delimiter=',': indicando que os dados estão separados por virgula (este é o padrão dos arquivos .csv)

dtype=None: permite que o Numpy "deduza" automaticamente o tipo de dados de cada coluna(float, string, etc.)

enconding='utf-8': estamos tentando garantir que caracteres especiais possam ser lidos sem erro

names=True: significa que a primeira linha do arquivo contem os nomes das colunas e deve ser usada como cabeçalho

invalid_raise=False: faz com que as linhas que possam apresentar eventuais problemas ou dados ausentes sejam ignoradas ao inves de causar um erro de carregamento/leitura de dados
'''

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
 
# --------------------------------------------------------------------
# - AULA 7

# passo 10: vamos definir um loop para iterar/percorrer os valores atribuidos a variavel especies_unicas
for obs in especies_unicas:
    # agora, vamos criar uma var para dar a ela um valor
    especies_dados = dados[especies == obs] # aqui, estamos comparando os valores encontrados pela var iteradora em relação aos valores que foram atribuidos a var especies 


    # neste passo, vamos criar uma nova var que receberá como valor o calculo de uma media 
    media_petal_length = np.mean(especies_dados['petal_length'])
    print(f'Media do comprimento da pelata para {obs} : {media_petal_length :.2f}')

'''
este trecho de codigo, acima, está calculando a média do comprimento da pétala(pental_length); para cada conjunto de dados 
'''

# passo 11: QUARTIS
print()
print('----------- Quartis ----------------')
# definindo os quartis para o comprimento da sépala
q1 = np.percentile(sepal_length, 25)
q2 = np.percentile(sepal_length, 50)
q3 = np.percentile(sepal_length, 75)

# exibir os quartis
print(f'1º QUARTIL do comprimento da sépala: {q1}')
print(f'2º QUARTIL do comprimento da sépala: {q2}')
print(f'3º QUARTIL do comprimento da sépala: {q3}')

# passo 12: FILTRAGEM CONDICIONAL
print()
print('----------- Filtragem condicional ----------------')
# definir um "filtro" para que tenhamos uma seleção a partir de uma condição
# 1ª condição
filtro = dados[dados['sepal_length'] > 5.0]
print(f'Dados com o comprimento da sépala maior que 5.0: {filtro}')
print()
print('----------- Filtragem condicional - mais de uma condição ----------------')
print('-------------- operador logico AND/ E ---------------')
filtrosAnd = dados[
                    # 2ª condicão
                    (dados['sepal_width'] > 3.0) & # OPERADOR LÓGICO AND
                    # 3ª condicão
                    (dados['petal_length'] > 1.5) &
                    # 4ª condicão
                    (dados['petal_width'] <= 2.0) &
                    # 5ª condicão
                    (dados['species'] == 'Setosa')
                ]
print(f'Dados com outras condicionais: {filtrosAnd}')

print()
print('-------------- operador logico OR/ OU ---------------')
filtrosOr = dados[
                    # 2ª condicão
                    (dados['sepal_width'] > 3.0) | # OPERADOR LÓGICO OR
                    # 3ª condicão
                    (dados['petal_length'] > 1.5) |
                    # 4ª condicão
                    (dados['petal_width'] <= 2.0) |
                    # 5ª condicão
                    (dados['species'] == 'Setosa')
                ]
print(f'Dados com outras condicionais: {filtrosOr}')


# passo 13: Relação entre as variaveis
print()
print('----------- CORRELAÇÃO ----------------')
# definir uma var para recebe como valor a função qeu vai auxiliar na analise da correlação entre as vars
correlacao = np.corrcoef(petal_length, petal_width)[0, 1]
print(f'Correlação entre o comprimento e a largura da pétala: {correlacao: .2f}')

'''
np.corrcoef(petal_length, petal_width): função Numpy que calcula a correlação de Pearson entre duas vars: petal_length, petal_width

a correlação de Pearson mede a "força" e a direção de uma relação entre duas variaveis numéricas. O resultado da matriz de correlação 2x2 é esta 
     0     1
0 [[1.0, 0.96]
1  [0.96, 1.0]]

acima, a diagonal terá sempre o valor 1.0(este valor determina a correlação de uma com ela mesma)

mas, o valo mais importante para a nossa analise está fora da diagonal: 0.96 (este valor determina a correlação entre as variaveis analisadas)

interpretando a sadia -> 0.96: indica que há uma correlação muito forte entre as vars; ou seja, quanto maior o comprimento, mairo a largura e vice-versa! Porque o indice de correlação esta mais proximo de 1.0 - 0.96; e muito longe od valor 0.0.
'''
# passo 14: Grafico com SEABORN
print()
print('----------- GRAFICO ----------------')
# indicar o "estilo visual" do grafico

sns.set_theme(style = 'whitegrid') # indica que a grade do grafico será clara
plt.figure(figsize = (8, 5)) # 8" de largura x 5" de altura

# nosso gráfico será um grafico de dispersão
sns.scatterplot(x = petal_length, y = petal_width, color = 'blue', s = 60) 

# agora, o grafico de dispersão de valores entre as vars esta definido. Vamos estabelecer a linha de tendencia(regressão linear)
sns.regplot(x = petal_length, y = petal_width, color = 'red', scatter = False)
'''
scatter = False: impede que os pontos, da dispersão, sejam repetidos, pois já foram exibidos pela função scatterplot()
'''
# adicionar os titulos/labels(rotulos/nomenclaturas) no grafico
plt.title('Correlação entre o comprimento e largura da pétala ', fontsize = 14)
plt.ylabel('Largura da pétala', fontsize = 12)
plt.xlabel('Comprimeto da pétala', fontsize = 12)

# definir a exibição do valor da correlação diretamente no grafico
correlacao = np.corrcoef(petal_length, petal_width)[0, 1]

# adicionar um texto, ao grafico, com o valor da correlação
plt.text(min(petal_length), max(petal_width) * 0.9, f'Correlação: {correlacao: .2f}')
'''
plt.text(min(petal_length), max(petal_width) * 0.9: aqui, estamos ajustando a posição do texto para a exibição do indice do correlaçã dentro do grafico
'''
# ajustar o layout 
plt.tight_layout()
plt.show()