'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10, até 0,
com uma pausa de 1 segundo entre eles.
'''
from time import sleep
for contador in range(10,-1, -1): # passo negativo para contar de de trás pra frente
    print(contador)
    sleep(1)
print('BOOM PÁAA BOOOOM KABOOOM - (Fogos estourando)')


    

