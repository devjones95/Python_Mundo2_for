'''Faça um programa que mostre a tabuada do número escolhido pelo usuário, utilizando um laço for'''

num = int(input('Digite um número inteiro: '))

for c in range(0, 11):
    print(f'{num} x {c} = {num*c}')
    
