"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se vc criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores

Já em Python:
    - Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplemente ir adicionando elementos;
    -Qualquer tipo de dado: As listas não possuem tipo de dado fixo; Ou seja, podemos colocar tipo de dado;

As listas em Python são representadas por colchetes:  []

lista1 = [1, 99, 5, 55, 1]

lista2 = ['G', 'U', 'I']

lista3 = []

lista4 = list(range(11))

lista5 = list('Guilherme')

#checar valor contido na lista
n1 = 8
if n1 in lista4:
    print('Encontrei o 8')
else:
    print('Não encontrei')

#checar valor contido na lista string
if 'G' in lista5:
    print('Encontrei o G')
else:
    print('Não encontrei o G')

#Ordenando lista
lista1.sort()
print(lista1) # Numero
lista5.sort()
print(lista5) # Letra

#Conta ocorrências de valor iguais
print(lista1.count(1))
print(lista5.count('e'))

#adicionando elemento em lista: append so permite adiconar um elemento por vez
print(lista1)
lista1.append(42)
print(lista1)

#adicionando elementos em lista com extend: Permite adicionar todos elementos como valor adiconal á lista principal
lista1.extend([123, 44, 76])
print(lista1)

# Inserir elemtento na lista em posição desejada
# Sem substituir o valor inicial.
lista1.insert(2, 'Novo valor')
print(lista1)

#Juntando duas listas
lista6 = lista1 + lista2
print(lista6)

#Invertando a lista
lista1.reverse()
print(lista1)
print(lista1[::-1])

#Copiar uma lista
list6 = lista2.copy()
print(list6)

#Conta quantidade de itens na lista
print(len(lista4))

#Podemos remover facilmente o último elemtento de uma lista
#OBS: O pop não somente remove o ultimo elemento como tbm o retorna
print(lista2)
lista2.pop()
print(lista2)

#removendo item por indice
lista2.pop(1)
print(lista2)

#limpando lista
lista5.clear()
print(lista5)
"""

lista1 = [1, 99, 5, 55, 1]

lista2 = ['G', 'U', 'I', 'L', 'I']

lista3 = []

lista4 = list(range(11))

lista5 = list('Guilherme')

