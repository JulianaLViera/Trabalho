def soma(a,b):
    return a + b

def quadrado(a):
    return a**2

def hipotenusa(cat1, cat2):
    return soma(quadrado(cat1), quadrado(cat2)) ** (1/2)

def simples(cor):
    if cor == 'azul':
        return "escolheu bem"
def medio(cor):
    if cor == 'azul':
        return 'escolheu certo'
    else:
        return 'tente outra cor'
    
def completo(cor):
    if cor == 'azul':
        return 'escolheu certo'
    elif cor == 'marrom':
        return 'não tem salvação'
    else:
        return 'tente outra cor'
    
numeros = [1,2,3,4,5]

contador = 0
while contador < 10:
    print(contador, end=' ')
    contador += 1
    
for i in range(10):
    print(i, end= ' ')
    
for item in [1,45,78,'a',[3 ,5]]:
    print(item)

for letra in 'minha string':
    print(letra)

for i in range(10):
    print((i + 1) * "*")
    print()