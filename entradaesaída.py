# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:10:19 2024

@author: 202401000345
"""

print("Olá", "mundo", sep="-") # Saída: Olá-mundo
print("Olá", "Python", end="!\n") # Saída: Olá Python!


# Saída: 18/04/2023 (formato de data)
print("18", "04", "2023", sep="/")

# Saída: nome; sobrenome; email (útil em CSVs)
print("nome", "sobrenome", "email", sep="; ") 


print("Loading", end=" | ")

print("[OK]") # Saída: Loading [OK]

#nome = input("Digite seu nome: ")
#print("Olá", nome)

#itens = input("Digite itens separados por vírgula: ").split(',')

#print("Itens:", itens)


# Convertendo a entrada para inteiro
#idade = int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")


# Convertendo a entrada para float
#altura = float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros.")


#def trinta_por_cento():
   # print("Digite números para adicionar à lista (digite 'done' para terminar):")
   # numeros = []
    #while True:
     #   entrada = input()
      #  if entrada.lower() == 'done':
      #      break
      #  else:
       #     numeros.append(int(entrada))
  #  print("Números coletados:", numeros)
    
    
#trinta_por_cento()

def imprimir_informacoes(nome, idade, cidade):
   
    print("Nome:", nome, "Idade:", idade, "Cidade:", cidade, sep=" - ", end="!")


imprimir_informacoes("Ana", 28, "Rio de Janeiro")

#def calcular():
   
 #   num1 = float(input("Digite o primeiro número: "))
 #   num2 = float(input("Digite o segundo número: "))
    
   
 #   operacao = input("Digite a operação desejada (+, -, *, /): ")
    
  
  #  if operacao == '+':
  #      resultado = num1 + num2
  #      print(f"O resultado de {num1} + {num2} é {resultado}")
  # elif operacao == '-':
  #      resultado = num1 - num2
  #     print(f"O resultado de {num1} - {num2} é {resultado}")
   # elif operacao == '*':
    #    resultado = num1 * num2
  #      print(f"O resultado de {num1} * {num2} é {resultado}")
  #  elif operacao == '/':
       
  #       if num2 == 0:
  #          print("Erro: Divisão por zero não é permitida.")
  #      else:
  #          resultado = num1 / num2
  #          print(f"O resultado de {num1} / {num2} é {resultado}")
  #  else:
   #     print("Operação inválida. Por favor, escolha entre +, -, * ou /.")


#calcular()

#def lista_de_compras():
  
    #itens_input = input("Digite os itens da lista de compras, separados por vírgula: ")
    
    #itens = [item.strip() for item in itens_input.split(',')]
    
 
    #print("\nLista de Compras:")
    #for item in itens:
        #print(item)


#lista_de_compras()
    
#def converter_celsius_para_fahrenheit():
    
   # celsius = float(input("Digite a temperatura em graus Celsius: "))
    
   
    #fahrenheit = (celsius * 9/5) + 32
    
  
   # print(f"{celsius}°C é equivalente a {fahrenheit}°F.")


#converter_celsius_para_fahrenheit()    

def coletar_nomes():
    nomes = []  

    while True:  
        nome = input("Digite um nome ou 'sair' para encerrar: ")
        if nome.lower() == 'sair':  
            break  
        nomes.append(nome)  

   
    print("\nNomes Digitados:")
    for nome in nomes:
        print(nome)


coletar_nomes()

