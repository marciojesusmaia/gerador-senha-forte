# GERADOR DE SENHAS FORTES
# c = contador
# t = tamanho

from random import choice
from os import system


lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&','*','=','?']
c = 1
senha = []

system('clear')
print('*'*45)
print('*','Bem vindo ao gerador de senha segura'.center(41),'*')
print('*'*45)
print()
t = int(input('Qual o tamnho da senha segura que deseja gerar? '))


while c <= t:
    senha.append(choice(lista))
    c +=1

senha2 = ''.join(senha)


print()
print(f'Sua senha segura é: {senha2}, contendo {c-1} caracteres','\n','\n')


