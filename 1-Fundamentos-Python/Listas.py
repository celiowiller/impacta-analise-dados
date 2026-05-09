# PYTHON LISTS - Listas com Python
'''
Uma lista, em python, determina que podemos ter um conjunto de dados composto por qualquer tipo de valor - ou seja, data types diferentes podem compor uma mesma lista! A estrutura de uma lista segue a mesma premissa do conjunto de dados da string - ou seja, cada valor que compõe o conjunto de dados (lista) ocupa um indice posicional reservado na memoria
'''

# definir uma lista - para este proposito, criaremos  uma variavel e, à ela, atribuiremos uma valor que seja descrito da seguinte forma: dentro de []COLCHETES. Agora, ao usarmos o caractere [] - aqui, ele assume o papel de uma lista python - podemos criar o conjunto de dados LIST

# INDICE POSICIONAL
#           0      1       2          3          4
umaLista = [1, 'palavra', 'c', 'YEGTKGHLKJGS', 256.8] # aqui, o que a define a lista python é o suo dos caracteres []

listona = [74, 'Sopranos', ['Python', 879, ['xalala', 532.7, 12], 50]]

# exibir as listas
print(umaLista)
print(listona)

# ---------------------------------------------------------------------------------------------------

print()
print('==================== OPERAÇÕES COM LISTAS =====================')

print(umaLista[2])


# OBSERVANDO A LISTONA
# INDICE POSICIONAL
#           0      1                      2
#                              0       1             2             3
#                                               0       1     2
listona = [74, 'Sopranos', ['Python', 879, ['xalala', 532.7, 12], 50]]

print()
print('==== aqui, vamos manipular listona')
print(listona[1])
print(listona[2])
#print(listona[2[1]])  # queremos acessar o valor 879
print(listona[2][1]) # queremos acessar o valor 879
print(listona[2][2][2]) # agora, queremo o numero 12 

print()
print('================== ALTERAR UMA LISTA')
# definir uma nova lista
#              0                 1             2    3
lista1 = ['matematica', 'lingua portuguesa', 1992, 2005]
print('Valor indicado no indice posicional 2 da lista1: ', lista1[2]) # aqui, a saida será 1992

# tentativa de substituir este valor selecionado
lista1[2] = 'Ola lista'
print('Valor de indice 2 da lista1, agora, alterado: ', lista1[2]) # aqui, a saida será 2026

print()
print('================== EXCLUIR UM ELEMENTO DE LISTA')

# agora, vamos excluir um elemento de lista
del lista1[2]


#neste passo, vamos exibir a lista com a exclusão do elemento
print('Lista exibida com o valor excluido: ', lista1)
print('algum valor assume o indice posicional 2 ou ele deixa de existir? ', lista1[2])

print()
print('================== OUTRAS MANIPULAÇÕES')

# definir uma nova lista
#              0         1     2           3              4        5 
lingProg = ['Python', 'Java', 'C#', 'Visual Basic', 'javascript', 'C']
#              5         4     3           3              1        0     -1

# exibir os resultados das operações
print(lingProg[2])  # saida: C#
print(lingProg[1:]) # saida: 'Java', 'C#', 'Visual Basic', 'javascript', 'C'
print('teste', lingProg[-1:4:-1]) # saida invertida

print(lingProg[::-1])  # saida invertida

'''
print(lingProg[-1::-1]) -> lê-se dessa forma:

print('teste', lingProg[-1:4:-1])  lê-se dessa forma:
print('teste', lingProg[5:4:-1]) ---> aqui, o python pratica o intervalo semi-aberto[....[ inclui-se o 1º item e exclui-se o ultimo intem do intervalo - a partir da operação (-1)

                            lingProg[start:stop:step]
'''

print()
print('================ USO DE FUNÇÕES NATIVAS')

# função len()
print(len(lingProg)) # aqui, podemos obter o numero total de dados dentro da lista

# função max()
print(max(lingProg)) # aqui, podemos obter o "valor" maximo dentre todos os dados da lista

# função min()
print(min(lingProg)) # aqui, podemos obter o "valor" minimo dentre todos os dados da lista

# vamos criar uma lista nova - chamada diferentona
listaDiferentona = ['%Bruno', '&lexandre', '-uilherme', '#du']

print(max(listaDiferentona)) # >
print(min(listaDiferentona)) # <
