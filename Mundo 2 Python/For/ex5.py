'''Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o'''

acumulador = 0 # precisamos dele pra armazenar os números pares e somar entre eles

for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        acumulador += num # se o número for par, nosso acumulador vai guardar e somar com o próximo número que também for par.
print(f'A soma dos 6 números escolhidos é de: {acumulador}.')


    


 