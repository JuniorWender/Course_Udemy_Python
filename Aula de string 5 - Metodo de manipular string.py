# aula de string 4 - Metodos de manipulação de string

from turtle import clear


nome = input("Digite O Seu Nome: ")

print(nome.capitalize()) # Ao utilizar capitalize ele transforma o PRIMEIRO caractere para maiusculo

print(nome.center(30)) # Centraliza o nosso texto ele irá adicionar 30 espaços em branco para <- e ->

print(nome.count("e")) # Conta quantos de um, caractere aparece durante aquela palavra

print(nome.endswith("ge")) # Retorna true or false se a nossa string terminar com oq foi determinado
