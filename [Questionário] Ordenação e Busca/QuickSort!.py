def quickSort(alist):
    if len(alist) <=1:
        return alist
    esquerda, pivo, direita = reordena(alist)
    esquerda = quickSort(esquerda)
    direita = quickSort(direita)
    esquerda.append(pivo)
    esquerda.extend(direita)
    return esquerda

def reordena(alist):
    pivo = alist[0]
    # Cria uma lista com os elementos menores ou iguais ao pivô
    esquerda = [x for x in alist[1:] if x <= pivo]
    # Cria uma lista com os elementos maiores que o piv
    direita = [x for x in alist[1:] if x > pivo]
    return esquerda, pivo, direita
