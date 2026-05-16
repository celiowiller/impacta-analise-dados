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