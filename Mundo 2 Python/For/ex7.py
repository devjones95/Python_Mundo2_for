'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A idade média do grupo.
- Qual o nome do homem mais velho.
- Quantas mulheres tem menos de 21 anos.'''

somaIdade = 0 # nossa variável que irá armazenar a soma das idades das pessoas
mediaIdade = 0 # variável que armazena o valor da média de idade
maiorIdadeHomem = 0 # variável que armazena a idade do homem mais velho
nomeMaisVelho = '' # variável que armazena o nome do homem mais velho
totalMulher20anos = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    somaIdade += idade
    if p == 1 and sexo in 'Mn': 
        maiorIdadeHomem = idade
        nomeMaisVelho = nome

    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome

    if sexo in 'Ff' and idade < 20:
        totalMulher20anos += 1

mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {idade} e se chama {nomeMaisVelho}.')
print(f'Ao todo, são {totalMulher20anos} mulheres com menos de 20 anos.')



