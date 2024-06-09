# São imutáveis

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres # Concatenação
print(elementos)


# Operações não disponíveis em Tuplas
# .sort() classificação em loco
# .append() anexar novos itens
# .reverse() para reverter a tupla
# .pop()

# Todos os metodos que alterem o coneudo da tupla não estão disponíveis

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# Criar uma lista a partir de uma tupla
# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

# Criar uma tupla a partir de uma lista

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))


