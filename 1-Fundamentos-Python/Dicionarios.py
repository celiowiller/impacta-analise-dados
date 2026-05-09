'''
    um dicionario - em python  - também é um conjunto de dados da mesma forma que uma tupla e uma lista!
    Mas com algumas diferenças:

    1 - para definirmos um dicionario é necessario usar os caracteres {} chaves

    2 - um dicionario é composto pares de dados organizados em: chave/key    :    valor/value 

    3 -  o conceito de indice posicional  NÃO EXISTE para um dicionario; então, um valor(VALUE) é selecionado pela chave(KEY) a qual ele, valor, está associado! 

    *** no mais, tudo aquilo que foi observado para uma lista/tupla/string  também se aplica oa dicionario
'''

# definir um dicionario
d = { # aqui, inicialmente, temos um dicionaroio vazio

    # chave : valor
    # key   : value
    'Nome'  : 'Florinda',
    'idade' : 37,
    'Curso' : 'Clipper',
    40      : 'florinda@mail.com'
}

# exibir o dicionario
print('Este é meu novo conjunto de dados - um dicionario : ', d)

print()
print('=============== OPERAÇÕES COM DICIONARIOS =================')

# selecionando um valor do dicionario
print('Imprimir o nome que consta no registro: ', d['Nome']) # o valor que queremos exibir é acessado pela chave(key) do dicionario

print('Imprimir a idade que consta no registro: ', d['idade']) # o valor que queremos exibir é acessado pela chave(key) do dicionario

print('Imprimir todos os dados do dicionario: ', d['Nome'], d['idade'], d['Curso'], d[40]) # o valor que queremos exibir é acessado pela chave(key) do dicionario

# aqui, vamos acessar um valor que, no dicionario, ainda não existe
# print(d['endereco'])

# ===============================================================

print()
print('FUNçÃO GET()')

print('Imprimir a idade que consta no registro - usando get(): ', d.get('idade')) # fazer uso da função da get() para selecionar um valor- a partir da chave/key

# ===============================================================

print()
print('INSERIR UM NOVO VALOR NO DICIONARIO')

# criar uma nova chave/key com um novo valor que deve ser adicionado ao dicionario
d['Sobrenome'] =  'Lalala'
print(d)

# ===============================================================

print()
print('NOVO DICIONARIO / NOVAS OPERAÇÕES')

# compor o novo dicionario a partir do recurso fromkeys() - é uma função nativa do python
disciplinas = {}.fromkeys(['Historia', 'Matematica', 'Geografia'], 0) # usando a função fromkeys() não é possivel criar um dicionario com valores disitintos para cada chave
print(disciplinas)
print()

print('Valores exibidos pelo loop for')
# criar um loop FOR para iterar sobre valores do dicionario
for x in disciplinas.items():
    print(x) # esta instrução PERTENCE a instrução acima; ou seja, faz parte da instrução for
'''
**** a variavel x é conhecida cmo variavel iteradora/auxiliar que irá RASTREAR/ITERAR sobre todos so valores que compõem o conjunto de dados/dicionario disciplinas 

    1º: esta é uma estrutura de repetição do python - for... in que irá exibir todos os valores que forem encontrados no dicionario disciplinas 

    2º: a função items() auxilia na recuperação/rastreamento de todos os valores que compõem o dicionario disciplinas - por isso esta associado a ele.

    3º: o uso da função  print(x) diz que: serão exibidos todos os valores que a variavel iteradora/rastreadora x encontrar dentro do dicionario disciplinas; até que não seja encontrado nenhum outro valor a mais.
'''

# ===============================================================

print()
print('NOVO DICIONARIO / "automaticos"')

# definir um novo dicionario
outroDicionario = {
#  chave :     valor 
#  key   :     value
    y    :      y*y  # temos, aqui, os pares chave/valor -> minha chave é y e o valor associado a ela é y^2
#   0    :      0*0 = 0
#   1    :      1*1 = 1
#   2    :      2*2 = 4
#   3    :      3*3 = 9

    for y in range(8) # instrução para gerar o intervalo de valores que compõem o dicionario 
    # 0, 1, 2, 3, 4, 5, 6, 7

    # **** a variavel y é conhecida como variavel iteradora/auxiliar que irá RASTREAR/ITERAR sobre todos os valores que compõem o conjunto de dados/dicionario outroDicionario - MAAAAAAAAAAAAAAAAAS, nosso novo dicionario, inicialemnte, não possui valor nenhum pors não definimos, de forma direta, nenhum valor pra ele. 
    # No entanto, que "popula/compõe" nosso dicionario com os valores adequado é o loop for com o uso da função range().
    # a função range() é nativa do python - sua funcionalidade é, exatamente, estabelcer um intervalo de valores numericos para algum elemento lógico - neste caso, o dicionario; podemos observar que a função possui um argumento -  o numero 8 - que indica a quantidade de elementos que devem ser criados dentro do dicionario; portanto o intervalo de valores estabelecido inicia em 0 (zero) e finaliza em 7 (sete) => total de 8 valores 
}

# exibir o dicionario criado
print(outroDicionario)