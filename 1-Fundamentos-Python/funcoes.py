'''
 uma função - em Python - é definida a partir do uso da palavra reservada def
 
 def -> nome da função -> ():
    alguma(s) instrução(ões) que compõe(m) a função
    ou seja, as "tarefas" que a função irá cumprir

    return -> expressão de retorno/resposta da função 
'''

# abaixo, a definição da função exibir() com um parametro: um parametro nada mais do que 
# uma variavel *** esta variavel/parametro será "enxergada/existirá" somente para função 
def exibir(umTexto): # umTexto -> é o parametro da nossa função; em algum momento este parametro receberá algum valor 

    print(umTexto) # essa é a "tarefa" que a função cumprirá quando for executada!
    return # o comando return encerra a função 


# acima, a função exibir() foi definida; agora, precisamos chamar esta função à sua execução
# fazemos isso criando um caller - objeto chamador - da função
exibir('Essa é a 1ª chamada da função!')
# temos, necessariamente, na chamada da função, ofereer um valor para o parametro

exibir('Essa é a 2ª chamada de função!')

exibir(79875645321) # essa é a 3ª chamada de função 

# --------------------------------------------------------------------

print()
print('-------------- função com uso de keyword/palavra-chave -------------')

# definir uma nova função
def dados(nome, idade):
    # 1ª tarefa: função print() para exibir o valor do parametro nome
    print('O nome é: ', nome)

    # 2ª tarefa: função print para exibir o valor do parametro idade
    print('A idade é: ', idade, ' anos')

    # encerrar a função
    return

print('Segue, abaixo, a chamada da função')

dados(idade = 38, nome = 'Saul Goodman')

# --------------------------------------------------------------------------

print()
print('=========== função Lambda =================')

'''
uma função lambda - em python - nada mais é do que uma função anônima! como uma função lambda não possui nome, precisamos associa-la à algo que poss ser referenciado par aque a função seja chamada a sua execução: é por isso que usamos uma variavel - PARA CRIAR UMA EXPRESSÃO DE FUNÇÃO -> significa que a função anônima é atribuida, como valor, de uma variavel
'''

# uma expressão de função inicia-se com a definição de uma variavel e atribui-se a esta variavel a função lambda; definida com o comando lambda
soma = lambda param1, param2 : param1 + param2

# soma: variavel que recebe como valor a função anônima
# lambda: palavra reservada que define uma função lambda
# param1, param2: parametros definidos, por nós, para a função lambda
# param1 + param2: equação de soma dos argumentos que serão dados aos parametros da função lambda -> significa que esta é a tarefa que a função lambda cumpre 

# agora, vmaos executar esta função
print('O valor da soma da função é: ', soma(1000, 9000))

print('O valor, aqui, da soma da função lambda é: ', soma(5, -5))




# -----------------------------------
def exibir(umTexto): # umTexto -> é o parametro da nossa função; em algum momento este parametro receberá algum valor 

    print(umTexto) # essa é a "tarefa" que a função cumprirá quando for executada!

    # posso criar uma soma

    # posso criar uma subtração


    # posso criar uma multiplicação

    # posso criar uma divisão

    # e, ainda, posso criar qualquer outra equação mais complexa 
    return # o comando return encerra a função

soma = lambda param1, param2 : param1 + param2


              