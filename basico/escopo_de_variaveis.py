"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis são reconhecidas, em todo o o programa.

2 - Local;
    -  São reconhecidas apenas no bloco onde foram declaradas.
"""

n1 = 42 #global
print (n1)


if n1 > 10:
    novo = n1 + 10 #local
    print(novo)

def teste_local():
    novo = 20 #local
    return novo + n1

print(teste_local())
