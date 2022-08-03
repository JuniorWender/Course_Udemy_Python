# Aula 11 - Trabalhando com entrada de dados e formatando as mesmas

nome = input("Digite O Seu Nome: ")
idade = int (input("Digite A Sua Idade: ")) # => Ao colocar esse int na frente você faz com que a entrada desse dado seja em int ao inves de str
salario = float (input("Digite O Seu Salario: ")) 


print("Nome: %s | Idade: %d | Salario:R$ %.0f" %(nome,idade,salario)) 