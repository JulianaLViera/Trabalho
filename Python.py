Python segue a mesma convenção usada na matemática, a ordem de avaliação dos operadores, do de maior precedência para o de menor precedência, por isso antes mesmo de executar qualquer operação é importante saber a ordem de precedência da sua operação matemática, para que o seu código não apresente um resultado diferente.

 

Sendo a ordem:

 

·        Parêntesis

·        Expoentes

·        Multiplicação e divisão (Da esquerda para a direita)

·        Somas e subtrações (Da esquerda para a direita)

Operador NOT em Python
O operador not em Python é o mais simples.
Ele ele pega a expressão e reverte ela.

Se era uma condição TRUE, ela vira FALSE.
Se algo era FALSE, ela vira TRUE.
Basta colocar not antes
banda = input('Qual melhor banda do mundo? ')

if not banda=='rush':
    print('Herege!')
else:
    print('Correto, é o Rush!')

https://www.dio.me/articles/qual-e-a-ordem-de-precedencia-em-python
https://www.pythonprogressivo.net/2018/02/Operadores-logicos-AND-OR-NOT.html
