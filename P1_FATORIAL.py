# Fatorial de um número

'''
Crie um programa que recebe um número e imprime seu fatorial.

Metodo 5Q's:
1. Quais são os dados de entrada necessário?
Número.
2. O que devo fazer com estes dados?
Calcular o fatorial do número que for passado para o meu programa e exibir na tela.
3. Quais são as restrições deste problema?
Números inteiros;
Números positivos.
4. Qual é o resultado esperado?
Que o calculo sejá feito e exibido na tela.
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0:
print "digite apenas números positivos"
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print fatorial
'''

num = int(input("Digite um número: "))
if num > 0:
   fatorial = 1
   for item in range(1,num + 1):
    fatorial = fatorial * item
print(fatorial)