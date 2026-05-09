'''
uma tupla, em python, é um conjunto de dados - semelhante a uma lista; com algumas diferenças:

     1 - para definirmos uma tupla, usamos os caracteres () - parenteses 

     2 - uma tupla, naturalmente, é um conjunto de dados IMUTAVEL!!!! ou seja, seus valores não se alteram em tempo de execução; a não ser que, manualmente, pratiquemos alguma alteração 

     *** no mais, tudo aquilo que foi observado e aplicado a uma lista, tambem se aplica auma tupla!
'''

# INDICE POSICIONAL
#           0      1       2          3          4
umaTupla = (1, 'palavra', 'c', 'YEGTKGHLKJGS', 256.8) # aqui, o que a define a tupla python é o uso dos caracteres ()

grandeTupla = (74, 'Sopranos', 'Python', 879, 'xalala', 532.7, 12, 50)

print()
print('================= OPERAÇÕES COM TUPLAS ===================')

# exibir as listas
print(umaTupla)
print(grandeTupla)



print(umaTupla[0])
print(umaTupla[1:3])
print(umaTupla[2:])
print(grandeTupla * 2)
print(umaTupla + grandeTupla)

# definir uma nova tupla
novoConjunto = ('filosofia', 'sociologia', 1993, 1996)

# tentativa de excluir um elemento de uma tupla
# del novoConjunto[1] - a operação de exclusão de um registro - numa tupla - não funciona porque a tupla é imutavel

# o que conseguimos fazer é: excluir a tupla inteira
del novoConjunto
# print(novoConjunto) -  na instrução de exibição da tupla temos um NameError - pois a tupla, no passo anterior, foi exlcuida; não exite tupla para exibir - com o nome novoConjunto




print()
print('================ USO DE FUNÇÕES NATIVAS')

# outraTupla = ('historia', 'geografia')
outraTupla = ('A', 'A') # neste caso, os valores dão identicos
# função len()
print(len(outraTupla)) # aqui, podemos obter o numero total de dados dentro da tupla

# função max()
print(max(outraTupla)) # aqui, podemos obter o "valor" maximo dentre todos os dados da tupla

# função min()
print(min(outraTupla)) # aqui, podemos obter o "valor" minimo dentre todos os dados da tupla

# vamos criar uma lista nova - chamada diferentona
tuplaDiferentona = ('%Bruno', '&lexandre', '-uilherme', '#du')

print(max(tuplaDiferentona)) # >
print(min(tuplaDiferentona)) # <

print()
print('================ OPERAÇÕES DE TRANSFORMAÇÃO - tuple(), list()')

minhaLista = [231, 56, 78.3, 'ola']

# transformar a lista, acima, numa tupla
print(tuple(minhaLista))

# transformar uma tupla numa lista
print(list(outraTupla))

