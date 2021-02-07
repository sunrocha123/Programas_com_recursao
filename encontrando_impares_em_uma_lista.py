numeros_coletados = []

def encontra_impares(lista):
    if lista == []:
        return numeros_coletados
    if lista != [] and (len(lista) - 1) >= 0:
        indice = len(lista) - 1
        if lista[indice] % 2 != 0:
            numeros_coletados.extend([lista[indice]])
        return encontra_impares(lista[:indice])