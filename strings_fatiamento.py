curso = "pYthon"

print(curso.upper())  # PYTHON: todas as letras maiúsculas
print(curso.lower())  # python: todas as letras minúsculas
print(curso.title())  # Python: primeira letra maiúscula de cada palavra
print(curso.capitalize())  # Python: primeira letra maiúscula da string

curso = "   pYthon  "
print(curso.strip())  # Python: remove espaços em branco dos dois lados
print(curso.rstrip())  # "   pYthon" : remove espaços em branco da direita
print(curso.lstrip())  # "pYthon  " : remove espaços em branco da esquerda

curso = "Python"
print(curso.replace("thon", "3"))  # Py3: substitui parte da string
print(curso.replace("P", "p"))  # python: substitui parte da string
print(curso.replace("Py", "Jav"))  # Javthon: substitui parte da string

curso = "Python"
print(curso.find("th"))  # 2: índice onde começa a substring "th"
print(curso.find("z"))  # -1: substring "z" não encontrada  

curso = "Python"
print(curso.center(10, "#"))  # ##Python##: centraliza a string com preenchimento
print(curso.ljust(10, "-"))  # Python----: alinha à esquerda com preenchimento
print(curso.rjust(10, "*"))  # ****Python: alinha à direita
print(curso.zfill(10))  # 0000Python: preenche com zeros à esquerda

curso = "Python é uma linguagem de programação. Python é muito popular."
print(curso.count("Python"))  # 2: conta ocorrências de "Python"
print(curso.join(["Aprenda ", "a", "programar "]))  # Aprenda a programar: junta lista em string
print(curso.split("."))  # ['Python é uma linguagem de programação', ' Python é muito popular', '']: divide a string em lista
print(curso.startswith("Python"))  # True: verifica se começa com "Python"
print(curso.endswith("popular."))  # True: verifica se termina com "popular."


