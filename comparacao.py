#operadores de comparação
a = 10 
b = 20
print(a == b)  #igualdade
print(a != b)  #diferente   
print(a > b)   #maior
print(a < b)   #menor   
print(a >= b)  #maior ou igual
print(a <= b)  #menor ou igual
#operadores lógicos
x = True
y = False
print(x and y)  #e
print(x or y)   #ou
print(not x)    #não

#combinação de operadores
idade = 25
altura = 1.75
print(idade > 18 and altura >= 1.70)  #verifica se é maior de idade e tem altura mínima
print(idade < 18 or altura < 1.70)   #verifica se é menor de idade ou não tem altura mínima
print(not (idade < 18))                #verifica se não é menor de idade
