# esta é uma linha de comentário no python; eeste é o "famoso" comentário de linha 
# estas linhas  - escritas com o caractere # - não são instruções lógicas. Portanto, serão ignoradas pelo interpretador python 

'''
Este, por exemplo, é um comentário de bloco de textos
Também será ignorado pelo interpretador
'''

'''
==========================================================================================
    ESTRUTURA DE DADOS COM PYTHON - PRIMEIROS PASSOS
==========================================================================================
'''

# vamos criar duas variaveis - chamadas de a e b
a = 1 # declaramos uma variavel com o nome - a - e atribuimos à ela o valor numérico 1; para este proposito - atribuição de um valor numérico para uma variavel - fizemos uso do operador = (igual); em lógico de prograqmação este operador/caractere é conhecido como operador de atribuição

b = 2 # declaramos uma variavel com o nome - b - e atribuimos à ela o valor numérico 2; para este proposito - atribuição de um valor numérico para uma variavel - fizemos uso do operador = (igual); em lógico de prograqmação este operador/caractere é conhecido como operador de atribuição

# vamos criar mais uma variavel - como o nome (c) - e iremos atribuir à ela, como valor, a soma das variaveis  a + b
c = a + b
#3 = 1 + 2

# agora, será necessario fazer uso de um recurso do python para que possamos exibir o valor da variavel (c)

print(c) # esta é uma função  - diretamente, nos dada, do python core; será utilizada para exibir o conteudo de qualquer "coisa" que queiramos mostrar - fazendo uso da linguagem python; a tarefa dessa função - print() - é simplesmente exbir qualquer conteudo 

# -------------------------------------------------------------------------------------

# abaixo, serão implementadas operações - fazendo uso dos operadores aritméticos python
print()
print('Resultado da operação de soma c = a + b = ', c) # aqui, estamos exibindo o mesmo valor da variavel (c) mas, ao mesmo tempo, tambem estamos exibindo um texto explicativo  - indicado entre aspas simples - ao lado do valor da variavel c; tecnicamente, esta modalidade é conhecida como: valor da variavel associada a um valor literal (valor literal é algo que não muda, seu valor, ao longo do processo de execução do código)
print()
print('Resultado da operação de subtração  a - b = ', a - b)

print()
print('Resultado da operação de multiplicação a * b = ', a * b)

print()
print('Resultado da operação de divisão a / b = ', a / b)

# -------------------------------------------------------------------------------------

print()
print('======================================================================')
print('INFERENCIA DE TIPO')
print()

# declarar 3 variaveis
numInt = 300
NumFloat = 456.89
NOME = 'Pandabox'


# alterando o valor da var numInt
numInt = 900
# alterando o valor da constante NOME
NOME = 'Guilherme'

# fazer uso da função print() para exibir os valores das vars
print('============ VALORES ATRIBUIDOS')
print(numInt)
print(NumFloat)
print(NOME)

print()
print('============ ESTES SÃO OS TIPOS DE DADOS DEFINIDOS/INFERIDOS PARA AS VARS - DATA TYPES')
# observar os data types atribuibos/inferidos a cada variavel
print()
print(type(numInt)) # função type() - com origem no python core - tem como objetivo exibir o data type de uma elemento lógico no python
print(type(NumFloat))
print(type(NOME))

print()
print('============ ATRIBUIÇÃO MULTIPLA DE VARIAVEIS ===================')
print()
# criar uma variavel e, com ela, praticar a atribuição multipla de valores
x = z = m = 'Bruno'
print(x)
print(z)
print(m)

print()
print('VARIAVEIS MULTIPLAS COM ATRIBUIÇÕES')
# criar variavesi multiplas e praticar atribuições multiplas
h, d, j, t = 89, 56.78, 'c', 'Edu'

# agora, vamos exibir as vars e seus respectivos valores
print(h, d, j, t)
print()
print(d, j, t, h)