# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import random
#from random import randint, choice

#randomseed(3)

#numero = randint(1,10)
#fruto = choice(['maçã', 'banana', 'laranja'])

from random import randint

def adivinhe_o_numero():
    numero_aleatorio = randint(1, 100)
    tentativas = 0
    acertou = False
    print("Adivinhe o número entre 1 e 100")
 
    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        
        if palpite < numero_aleatorio:
            print("Muito baixo!")
        elif palpite > numero_aleatorio:
            print("Muito alto!")
        else:
            print(f"Você adivinhou em {tentativas} tentativas.")
            acertou = True

#adivinhe_o_numero()

import random

def lancar_dado():
    resultado = random.randint(1, 6)  
    return resultado

resultado_lancamento = lancar_dado()
print("O resultado do lançamento do dado é:", resultado_lancamento)