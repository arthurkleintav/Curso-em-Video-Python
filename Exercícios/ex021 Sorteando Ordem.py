from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Seguundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem selecionada para apresentar o trabalho será: ')
print(lista)