"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples > 'oi'
- Estiver entre àspas duplas > "oi"
- Estiver entre àspas simples triplas > '''oi'''
"""
# Estiver entre àspas duplas triplas > """oi"""

n1 = 'Hello \nWorld !'
print(n1)
print(type(n1))

n2 = "Hello World !"
print(n2)
print(type(n2))

n3 = '''Hello World !'''
print(n3)
print(type(n3))

n4 = """Hello 
World !"""
print(n4)
print(type(n4))

print(n2.upper()) #letra maiuscula

print(n2.lower()) #letra minuscula

print(n2.split()) #transforma em lista

print(n2[0:5]) #Slice de string, pega poisção desejada

print(n2.split()[1]) #Slice de string, pega poisção desejada da lista gerado pelo split

print(n2[::-1]) #Invert String