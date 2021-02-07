def soma_lista(lista):
    if lista == []:
        return False
    elif lista != [] and len(lista) > 0:
        indice = len(lista) - 1
    if indice >= 0:
        return lista[indice] + soma_lista(lista[:indice])