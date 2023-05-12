"""

Estruturas Lógicas: and(e), or (ou), not(não), is(é)

"""
ativo = True
logado = False

if ativo is True:
    print("Usuario ativo no sistema")

if ativo and logado:
    print("Usuario ativo no sistema e logado no sistema")
elif not ativo and not logado:
    print("Usuario não ativo no sistema e não logado no sistema")
elif ativo and not logado:
    print("Usuario é ativo no sistema e não esta logado no sistema")
elif ativo or logado:
    print("Usuario esta ativo ou logado no sistema")

