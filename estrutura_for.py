texto = input("Digite um texto: ")
VAOGAIS = "aeiouAEIOU"

# Loop para percorrer cada letra do texto
for letras in texto:
    if letras in VAOGAIS:
        print(letras, end=' ' )
    else:
        continue    