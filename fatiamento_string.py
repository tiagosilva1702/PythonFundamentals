# fatiamento de string
curso = "pYthon"
print(curso[0])      # 'p': primeiro caractere
print(curso[1])      # 'Y': segundo caractere   
print(curso[-1])     # 'n': último caractere
print(curso[0:2])    # 'pY': do índice 0 ao 2 (exclusivo)
print(curso[2:])     # 'thon': do índice 2 até o final  
print(curso[:2])     # 'pY': do início até o índice 2 (exclusivo)
print(curso[1:4])    # 'Yth': do índice 1 ao 4 (exclusivo)
print(curso[::2])    # 'Pto': do início ao fim, pulando de 2 em 2
print(curso[::-1])   # 'nohtYp': string invertida
print(curso[1::2])   # 'Yhn': do índice 1 ao fim, pulando de 2 em 2
print(curso[-4::-1]) # 'Yp': do índice -4 ao início, invertido
print(curso[-1::-1]) # 'nohtYp': do índice -1
print(curso[-1:-4:-1]) # 'noh': do índice -1 ao -4 (exclusivo), invertido
print(curso[-4:-1])  # 'tho': do índice -4 ao -1 (exclusivo)
print(curso[:])      # 'pYthon': toda a string


