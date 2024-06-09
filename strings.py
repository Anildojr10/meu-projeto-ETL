# nome = 'Curso de Python'
# aluno = 'Anildo'
# print(nome + ' com ' + aluno)

# frase = 'Vamos aprender Python hoje!!!'
# palavras = frase.split()
# print(palavras)
# for palavra in palavras:
#     print(palavra)


# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'Carbonato de sódio e Óxido de zinco'
# print('sódio' in produtos)
# print('magnédio' in produtos)

# item = 'hipoclorito'    
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)


# objeto_celeste = 'galáxia esPiral M31'
# print(objeto_celeste.upper())
# print(objeto_celeste.lower())
# print(objeto_celeste.capitalize())
# print(objeto_celeste.title())

# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')
# print(suplemento)
# print(n_suplemento)


# frase = '     ômega 3 é bom para a saúde!        '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20, "-"))
# print(fruta.center(20, "-"))

# p = 'Bóson Treinamentos'
# print(p.startswith('B'))
# print(p.endswith('b'))


# Docstrings
texto = """
Docstrings é uma espécie de documentação 
que podemos inserir dentro de um módulo, função
ou classe no Python entre outros locais
    Respeita deslocamento do texto e é multilinhas
"""
print(texto)
