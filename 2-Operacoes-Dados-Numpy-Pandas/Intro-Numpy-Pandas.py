# agora, vamos começar a lidar com elementos de maior complexidade
# portanto, vamos iniciar os codigos importando os recursos de modulo para que tudo funcione adequadamente
import numpy as np # aqui, a lib numpy recebe um alias/"apelido", portanto, quando precisarmos referenciar a lib numpy basta escrever np

# criar uma lista com numeros
grupo = [[31, 85, 96], [4, 12, 1], [78, 986, 1000]]

'''
neste passo, vamos criar uma matriz usando o recurso numpy.

para este proposito, vamos definir uma nova variavel para receber como valor a função matrix
'''
umaMatriz = np.matrix(grupo) # a função matrix tem origem no numpy

# a tarefa que a função matrix() cumpre é: transformar um conjunto de dados numa matriz matematica
print('-------------------------------------------------------------------')

# agora, vamos exibir os resultados associados a nossa matriz recem-criada
print(type(umaMatriz)) # verificar o tipo da variavel
print('-------------------------------------------------------------------')

# verificar formato/dimensoes da matriz
print(np.shape(umaMatriz))
print('-------------------------------------------------------------------')

# uso da função mean() -> função que calcula a média de valores considerando o conjunto de dados
print(np.mean(umaMatriz))
print('-------------------------------------------------------------------')
print()

print('=================== ALGUMAS OPERAÇÕES COM MATRIZES ================')

# agora, serão criadas duas matrizes - ambas receberão valores distintos
matriz1 = np.array([['2', '4'], ['5', '-6']]) # esta é a função array, com origem no numpy, especificamente usada para criar arrays 

matriz2 = np.array([['9', '-4'], ['3', '5']])

# definir a operação de soma de matrizes
matrizResultante = matriz1 + matriz2

# exibir o resultado da operação
print('O resultado da operação é: ', matrizResultante)

print()
print('=================== OPERAÇÕES/ANALISES COM DADOS - NUMPY/PANDAS ================')

# importar o recurso pandas
import pandas as pd

# definir uma Series - uma Series nada mais é do que: uma matriz unidimensional, ou seja, de uma unica linha
umaSerie = pd.Series([1, 2, 3, np.nan, 6, 8, 'Ola'])

# acima, temos um valor chamada np.nan - este é o recurso que oferece a possibilidade de trabalhar com um elemento não-numérico(not-a-number): origem no numpy 
print(umaSerie)

print()
print('=================== criar alguns dataframes ================')
print()
print('=================== criar dataframe 1 ================')

# neste passo, será definida uma nova variavel para receber um conjunto de valores 
algumasDatas = pd.date_range('20260506', periods=6)
print(algumasDatas)

'''
para criar o conjunto de dados DateTimeIndex precisamos usar poucos recursos - são estes:

pd -> lib pandas
date_range() -> esta é a função para criar o intervalo/conjunto de valores baseados em datas

parametros 20260506, peridos -> os dois parametros estabelecem uma data inicial - 2026-05-06 - e o intervalo de valores que estamos estabelecendo para o periodo é dado pelo paramentro periods = 6 que gera o intervalor observado na saida; 

por padrão, o pandas estabelece para o intervalor de datas gerado, uma freq (frequency) diária -> freq = 'D'

então o resultado é este: 2026-05-06, 2026-05-07, 2026-05-08, 2026-05-09, 2026-05-10, 2026-05-11
'''

# agora, vamos definir um dataframe - que vamos conhecer e usar a sigla df
df1 = pd.DataFrame(np.random.randn(6, 4), index = algumasDatas, columns = list('ABCD'))

'''
O 1º argumento da função acima - DataFrame - é o recurso necessario para criar o dataframe com os dados gerados de forma randomica

dados que compõem o dataframe: este dados serão gerados, automaticamente, para preencher ao df a partir da instrução np.random.randn(); este valores são gerados seguindo as caracterisitcas definidas pelos valores 6, 4 -> significa que este dataframe será preenchido/"populado" por valores randomicos para a seguinte estrutura: 6 linhas e 4 colunas 

o 2º argumento - index = algumasDatas - define qual será o recurso de indice posicional principal do df - é o indice posicional das LINHAS 

o 3º argumento  - columns = list('ABCD') - define a quantidade de colunas que compõem o df
'''

print()
print('Este é nosso 1º dataframe')
print(df1)

print()
print('=================== criar dataframe 2 ================')

# gerar um novo dataframe; será gerado a partir de um dicionarios
# quando usamos dicionarios - baseados em pares key/value - o elemento key se tornará a coluna do df e o elemento value se tornará o valor que "popula" a linha(s) da coluna
df2 = pd.DataFrame({
    'A': 1., # valor constante repetido para todas as linhas da coluna A
    'B': pd.Timestamp('20260603'), # mesmo valor de data para todas as linhas da coluna B do df
    'C': pd.Series(1, index = list(range(4)), dtype = 'float64'), # Series com 4 elementos do tipo float que resulta no numero 1.0 -> indicado no argumento 1
    'D': np.array([3.0] * 4, dtype = 'int32'), # array com 4 valores inteiros - indicado pelo valor 3.0 mas devemos lembrar que o array foi definido com o dtype = 'int32'
    'E': pd.Categorical(['teste', 568, 'novo teste', 42]), # categorico com valores variados
    'F': 'esta é uma string' # mesma string vai "popular" todas as linhas da coluna F 
})
print('Este é o Dataframe 2')
print(df2)

# --------------------------------------------------------------------------------

print()
print('---------------------- observando - analise primaria -  os contextos dos DFs -------------------')
print()

# uso do comando/palavra reservada dtypes(data types) demonstra os tipos de dados que o compõem os DFs
print('composição dos data types do df1')
print(df1.dtypes)
print('composição dos data types do df2')
print(df2.dtypes)
print()

# neste passo, vamos fazer uma "leitura" resumida dos DFs; para este proposito será utilizado a função head(): por padrão, a função head() lê as primeiras 5 linhas de qualquer df
print('primeiras linhas do df1')
print(df1.head(2))
print('primeiras linhas do df2')
print(df2.head(2))
print()
# neste passo, vamos fazer uma "leitura" resumida dos DFs; para este proposito será utilizado a função tail(): por padrão, a função tail() lê as 5 ultimas linhas de qualquer df
print('ultimas linhas do df1')
print(df1.tail(3))
print('ultimas linhas do df2')
print(df2.tail(3))
print()
# neste passo, vamos fazer uma "leitura" de indice dos DFs; para este proposito será utilizado o comando index
print('indices do df1')
print(df1.index)
print('indices do df2')
print(df2.index)
print()
# neste passo, vamos fazer uma "leitura" das colunas DFs; para este proposito será utilizado o comando columns
print('colunas do df1')
print(df1.columns)
print('colunas do df2')
print(df2.columns)
print()
# neste passo, vamos fazer uma "leitura" de resumo/resumir, estatisticamente, DFs; para este proposito será utilizado a função describe()
print('resumo estatitico do df1')
print(df1.describe())
print('resumo estatistico do df2')
print(df2.describe())

'''
count: contagem da qtde de valores NÃO NULOS  do df (df1 = 6, df2 = 4)
mean: média aritmética do valores que compõem o df
min: é o menor valor - valor minimo - dentro de cada coluna do df

25%: 1º QUARTIL -> significa que 25% valores encontrados nos dados estão abaixo destes valores indicados em cada coluna 
50%: 2º QUARTIL -> significa que 50% valores encontrados nos dados, indicados em cada coluna do df, são considerados a MEDIANA de cada coluna
75%: 3º QUARTIL -> significa que 75% valores encontrados nos dados estão abaixo destes valores indicados em cada coluna; resumindo: portanto, a função describe diz que no 3º quartil 75% dos dados de uma determinada coluna são menores ou iguais ao indice indicado

max: é o maior valor - valor maximo - de cada coluna do df
'''

print()
print('---------------------- organizar dataframes -------------------')
print()

# observar a organização dos dfs  a partir de valores de uma coluna especifica
print('Ordenando o df1 por uma coluna especifica')
print(df1.sort_values(by = 'C', ascending = False))
print()
print('Ordenando o df2 por uma coluna especifica')
print(df2.sort_values(by = 'E', ascending = False))
print()

print('Ordenar o df1 de forma decrescente - pelo eixos das linhas ')
print(df1.sort_index(axis = 0, ascending = False))
'''
sort_index: função que ordena o df pelo indice "principal" - indic de linhas do df; também conhecido como o AXIS = 0; já o eixo das colunas é conhecido, tecnicamente como o AXIS = 1

ascending = False: significa que ordem será decrescente - ou seja, do maior par ao menor
'''
print('Ordenar o df2 de forma decrescente - pelo eixos das linhas ')
print(df2.sort_index(axis = 0, ascending = False))

# -------------------------------------------------------------------

print()
print('============ OPERAÇÕES COM SELECÕES E FATIAMENTO DE DFs ===========')
print()

print('Fatiando o df1')
print(df1['A'])
print()
print('Fatiando o df2')
print(df2['D'])
print()

# aplicar a seleção de um intervalo de valores a partir do df
print('Fatiando df1 - via intervalo')
print(df1[1:3]) # intervalo semi-aberto [.....[
print()
print('Fatiando df2 - via intervalo')
print(df2[2:4]) # intervalo semi-aberto [.....[


# fatiar via indice-linha
print('Fatiando df1 - via indice-linha')
print(df1['2026-05-07':'2026-05-10']) # intervalo semi-aberto [.....[????? NÃO E APLICA, AQUI, O CONCEITO DE INTERVALO SEMI-ABERTO
print()
print('Fatiando df2 - via intervalo')
print(df2[1:3]) # intervalo semi-aberto [.....[ - SIM, SE APLICA POIS AQUI TEMOS O PADRÃO-INDICE-POSICINAL PRINCIPAL

# -------------------------------------------------------------------

print()
print('============ OPERADORES .loc, .iloc, .at, .iat ===========')
print()

'''
os comandos -.loc, .iloc, .at, .iat- proporcionam processos de seleção precisa, a partir dos DFs. 

.loc: este operador funciona através de elementos nomeados(com nomes/valores) do df - (labels/nome)

.iloc: este operador funcioan aplicado ao indices posicionais do df

.at: este operador funciona através de elementos nomeados(com nomes) de indice posicional do df - (labels/nome)

.iat: este operador funcioan aplicado ao indices posicionais do df
'''

print()
print(df1)
print()
print(algumasDatas)
print()
print(df1.loc[algumasDatas[-1]]) # em Python, indice negativo significa que a contagem é feita de "trás para frente"
print()

# .loc: acessando as linhas pelo label/nome associado ao indice posicional
'''
acima, estão ocorrendo duas situações principais:
1. estamos "pegando" o ultimo elemento da algumasDatas -> a partir do comando: algumasDatas[-1]

2. estamos selecionando, então, este valor para localizar uma linha no Dataframe df1
'''

# praticar uma nova operação - a partir do indice nomeado  '2026-05-08' e trazer, com esta seleção, os valores de duas colunas especificas
print(df1.loc['20260508', ['A', 'B']]) 
print()

# uma nova seleção: selecionar o elemento de indice de linha algumasDatas[0] e extrair, desta linha, o valor da coluna 'C'
print(df1.loc[algumasDatas[0], 'C'])
print()

# agora, vamos fazer uso o operador .iloc: como sabemos, .iloc, opera EXCLUSIVAMENTE a partir dos indices posicionais dos DFs
print(df1.iloc[:4, :3]) # intervalo semi-aberto [....[ - SIM, SE APLICA EM AMBOS INTERVALOS - eixo das linhas :4; eixo das colunas :3

# acima, foram selecionados os seguintes dados: todas as ocorrencias até a linha de indice posicional 4 e todas as ocorrencias de dados até o indice posicional 3 - do eixo das colunas

# PREMISSA: a seleção será composta pelo seguinte intervalo: linhas de 1 a 5(sempre será, neste contexto, aplicado o intervalo semi-aberto) e queremos todas as colunas do df; qual a operação que atende a esta premissa? está indicada abaixo.
print(df1.iloc[1:5, :])
print()

#--------------------------------------------------------------------------
print('------------------- operadores .at / .iat -----------------------------')
print()

# PREMISSA: a seleção será composta pelo seguinte intervalo: todas as linhas; e queremos as colunas de 1 a 3
# qual o conjunto de instruções lógicas pode responder a este premissa(sempre é o praticado o conceito de intervalo semi-aberto); para esta premissa vamos fazer uso do operador .iat ******** PORÉM..... O OPERADOR .iat NÃO ACEITA INTERVALOS - SEU FUNCIONAMENTO SE DÁ PARA ACESSO A UM ÚNICO ELEMENTO DO DATAFRAME -> OU SEJA, ABAIXO  A INSTRUÇÃO, COM .iat, INDICA: 2º linha e 4ª coluna
print('operador .iat')
print(df1.iat[1, 3])
print()
# ENTÃO, PARA RESPONDER A ESTA PREMISSA VAMOS O OPERADOR .at.... TAMBÉM NÃO ACEITA INTERVALOS; ESTES OEPRADORES FUNCIONAM E SÃO USADOS, CONSEQUENTEMENTE, PAR AVALROES UNICOS. PARA INTERVALOS - EXTRAIDOS A PARTIR O DF - PRECISAMOS USAR OS OPERADORES .loc e .iloc
print('operador .at')
print(df1.at['20260506', 'A'])
print()

print('================== GRÁFICOS/MATPLOTLIB ======================')
'''
Matplolib é uma biblioteca do Python que cria gráficos 2D para visualização de dados.A visualização sempre ajuda na prática de qualquer analise de dados e, consequentemente, aumento da capacidade de informações
'''

# importar a  biblioteca matplotlib

import matplotlib.pyplot as plt

# para fazer uso dos graficos, vamos definir uma novo df
df3 = pd.Series(np.random.randn(1000), index = pd.date_range('20100101', periods = 1000))

# o df3, gerado acima, é um Time Series - series temporais -, signifca que: foi criada uma Series com indices posicionais de suas linhas de dados baseados em data 
print(df3)

'''
PREMISSA: fazer uso da função plot() para exibir um gráfico simples e tentar entender o comportamento dos vlaores da serie temporal estabelecida para o df3; antes de gerar o grafico, vamos praticar uma operaçõa de soma acumulada - ou seja, cada valor é soma dele mesmo com todos os anteriores - dos valores para enttender, ainda melhor, o comportamento dos numeros 
'''
# soma acumulada 
somaAcumulada = df3.cumsum()
print('resultado da soma acumulada', somaAcumulada)

#-------------------------------------------------------------
# para exibir o grafico vamos criar um novo df - df4 -  a partir dos novos recursos que acabamos de estabelecer: o df3 junto com o matplotlib
df4 = pd.DataFrame(np.random.randn(1000, 4), index = df3.index, columns = ['A', 'B', 'C', 'D'])
print(df4)
print()

# plotar um novo grafico a partir da nova serie temporal

oGrafico = df4.cumsum()
oGrafico.plot()
plt.show()

