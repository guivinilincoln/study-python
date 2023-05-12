"""
Recebendo dados do usuário

"""
print("Qual seu nome? ")
nome = input()

idade = int(input("Qual sua ideade? "))

#print("Seja bem-vindo(a) " + nome + "" + idade)
print("Seja  bem-vindo(a) %s você tem %s anos" % (nome, idade))
print("Seja  bem-vindo(a) {0} você tem {1} anos".format(nome, idade))
print(f'Seja  bem-vindo(a) {nome} você tem {idade} anos')


print(f'Seja  bem-vindo(a) {nome} você nasceu em {2023 - int(idade)}') #cast