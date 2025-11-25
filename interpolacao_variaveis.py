# interpolação de variaveis em strings

nome = "Alice"
idade = 30

# Usando f-strings (Python 3.6+)
mensagem_fstring = f"Meu nome é {nome} e eu tenho {idade} anos."
print(mensagem_fstring)

# Usando o método format()
mensagem_format = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem_format)

# Usando o operador %
mensagem_percent = "Meu nome é %s e eu tenho %d anos." % (nome, idade)
print(mensagem_percent)

# Usando concatenação
mensagem_concat = "Meu nome é " + nome + " e eu tenho " + str(idade) + " anos."
print(mensagem_concat)

