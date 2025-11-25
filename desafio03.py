def conta_vogais(texto: str) -> int:
    # 1. Definir conjunto de vogais (maiúsculas e minúsculas)
    vogais = set("aeiouAEIOU")
    
    # 2. Inicializar contador
    contador = 0
    
    # 3. Iterar pelos caracteres da string
    for char in texto:
        # 4. Verificar se o caractere é uma vogal
        if char in vogais:
            contador += 1
    
    # 5. Retornar o contador
    return contador


# Exemplos de uso:
print(conta_vogais("Python"))        # Saída: 1 (apenas 'o')
print(conta_vogais("Copilot"))       # Saída: 3 ('o', 'i', 'o')
print(conta_vogais("Desafio"))       # Saída: 4 ('e', 'a', 'i', 'o')
print(conta_vogais("AEIOUaeiou"))    # Saída: 10 (todas vogais)