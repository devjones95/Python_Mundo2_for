'''Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo 
de 1 até 500'''

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0: # se o número dentro do nosso contador for divisível por 3, ele será printado.
        soma = soma + c #ACUMULADOR: a soma recebe o valor dela, mais os números múltiplos de 3 dentro do nosso for, acumulando os valores sempre que o laço solicitar.
        contador = contador + 1 # CONTADOR: Vai contar sempre que encontrar algum elemento que for divisível por 3
print(f'A soma de todos os {contador} valores solicitados é de {soma}.')
