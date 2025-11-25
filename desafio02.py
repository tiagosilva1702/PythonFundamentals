def eh_bissexto(ano: int) -> bool:
    """
    Retorna True se o ano for bissexto, caso contrário False.
    """
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


# Exemplos de uso:
anos = [1996, 2000, 1900, 2024, 2100]

for ano in anos:
    print(f"{ano}: {'Bissexto' if eh_bissexto(ano) else 'Não bissexto'}")