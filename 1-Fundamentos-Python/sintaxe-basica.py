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

# ===================================================================================
# AULA - 2
print()
print('=====================================================')
print('MANIPULAÇÃO DE STRINGS')

# vamos definir uma varivavel para receber como valor uma string/frase
umaFrase = 'Hoje é um dia excelente!'

# aqui, abaixo, serão exibidos os valores das manipulações

print()
print('-------- Manipulando a string----------------')
print(umaFrase)

print(umaFrase[0]) # aqui, o caractere [](colchete) assume uma nova funcionalidade: ele se torna o operador slice - "cortar/fatiar" - para "cortar/fatiar" a string num determinado "pedaço"

'''
    abaixo, na sequencia de caracteres, temos - de forma "implicita/oculta" - um sequencia numérica que indica, em ordem crescente, qual é a posição - dentro do conjunto de dados (string) - que cada "letra" ocupa


INDICE POSICIONAL            0  1  2  3 4 5 6 7  8 9 10  11  12 13 14  15 16 17  18 19  20  21 22 23  24
                             H  o  j  e   é   u  m   d   i   a     e   x   c  e  l   e   n   t    e   !

'''

print(umaFrase[2:13]) # neste, novamente, estamos executando um "fatiamento"! Só que, neste passo, estamos gerando um INTERVALO DE CARACTERES, ou seja, estamos criando um subconjunto ou uma substring - a partir do conjunto ou string anteriors. Esta é a operação que indica "extração" do seguinte subconjunto - [2:12]; isso significa que o "fatiamento" inicia no indice posicional 2 e vai até o indice posicional 12;

# [..........[ - intervalo semi-aberto: o intervalo semi-aberto determina que: no intervalor deve-se incluir o 1º elemento e excluir-se o ultimo elemento da composição do intervalo - a partir da seguinte operação -> [2:12] (-1) = [2:11]

print(umaFrase[:8]) # novamente, temos um novo "fatiamento" gerando um novo intervalo!
# [..........[ - intervalo semi-aberto: o intervalo semi-aberto determina que: no intervalor deve-se incluir o 1º elemento e excluir-se o ultimo elemento da composição do intervalo - a partir da seguinte operação -> [:8] (-1) = [:7]

print(umaFrase[3:]) # novamente, temos um novo "fatiamento" gerando um novo intervalo! O intervalo começa no indice posicional 3 e vai até o ultimo indice posicional que compõe o intervalo. Portanto, o conceito de intervalo semi-aberto não se aplica!

print(umaFrase[1], umaFrase[10], umaFrase[20]) # toda a vez que precisamos acessar indice posicionais distintos, ao mesmo tempo, dentro de uma string, fazemos o seguinte: acessamos a string - separada por virgula - repetidas vezes e indicamos o valor do indice posicional

print(umaFrase * 3) # aqui, nesta operação, estamos "dizendo" qu queremos que o valor da variavel 'umaFrase' seja REPETIDA/MULTIPLICADA tres vezes

print(umaFrase + ' Muito bom ! Que todos os dias sejam assim.') # aqui, nesta operação, estamos dizendo que queremos associar/ligar/concatenar/juntar o valor da variavel 'umaFrase' ao novo texto/frase que indicamos depois do operador(+) plus/mais


print('Alexandre exemplo 1:  ' + umaFrase[1], umaFrase[10]) # uma virgula NÃO CONCATENA ELEMENTOS! UMA VIRGULA, NO PYTHON, SEPARA/SEGREGA ARGUMENTOS!

print('Alexandre exemplo 2:  ' + umaFrase[1] + umaFrase[10])
print()

print('===========================================================================')
print('ALTERAR UMA STRING')

# vamos definir uma nova frase

novaFrase = 'Amanhã, também, será excelente!'
print('Alterando a string: ', 'Depois de amanhã,', novaFrase[7:])

# vamos definir uma nova variavel com um novo valor
nome  = 'Guilherme'
print('O nome do meu amigo é %s, ele tem %d anos de idade.' % (nome, 21))

# aqui, acima, estamos usando o operador % (aqui, no "papel" de operador de FORMATAÇÃO DE SAIDA DE STRING) -> %s %d significa que: pela ordem posicional o caratere %s espera  uma string - anda deiferente disso - e o operador de formatação %d espera um valor numérico - nada diferente disso!

print('==============================================================')
 # definir uma nova variavel para observar o uso de uma formatação de saida extremamente comum. Provavelmente, usaremos com maior frequencia 

novoNome = 'Bruno'
idade = 37
print(f'O nome do meu amigo é {novoNome} e ele tem {idade} anos de idade!')

# (f''): f-string: formato que "junta/concatena/liga/interpola ("mistura ao mesmo tempo") elementos literais de string com valores de variaveis"