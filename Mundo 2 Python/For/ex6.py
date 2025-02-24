'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mosntre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date

atual = date.today().year # importamos a biblioteca time para sabermos o ano atual

totalMaior = 0 # variável que vai guardar a quantidade de pessoas maiores de idade teremos
totalMenor = 0 # variável que va guardar a quantidade de pessoas menores de idade teremos

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}° pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor +=1
print(f'Ao todo, temos {totalMaior} pessoas maiores de idade.')
print(f'Também tivemos {totalMenor} pessoas menores de idade.')




