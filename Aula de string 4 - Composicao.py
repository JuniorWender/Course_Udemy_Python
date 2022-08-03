# aula de string 4 - Composição de string

nome = "Jorge"
idade = 25
salario = 1000

# -------------------------------------------------------------------------------
# Sem Composição:

print("Sem Composição:")
print("Nome:",nome,"| Idade:",idade,"| Salario:R$",salario)

print("")

# -------------------------------------------------------------------------------
#Com Composição:

print("Com Composição:")
print("Nome: %s | Idade: %d | Salario:R$ %.0f" %(nome,idade,salario)) # Ao colocar .0f definimos a quantidade de casas decimais para 0
