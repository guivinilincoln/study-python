"""
Estrutura de repetição

lista = [1,2,3,4,5,6]
nome = "Gui"

for numero in lista:
    print(numero)

for interacao, letra in enumerate(nome):
    print(nome[interacao])

for interacao, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome): #utilizado para descartar indice
    print(letra)

for letra in enumerate(nome): #traz tudo
    print(letra)

for letra in enumerate(nome): #traz somente as letras
    print(letra[1])

for n in range(10): # For padrão

     n += 1
    print(n)

for n in range(10): # For padrão
    n += 1
    print(n)
"""
"""
qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0
for n in range(1, qtd+1):
    valor = int(input(f'Informe o {n}/{qtd} valor:'))
    soma += valor
print(f'A soma é {soma}')
"""
"""

nome = 'Gui Lincoln'
for letra in nome:
    print(letra, end='')
"""