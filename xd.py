def minus_num(lista, num):
    newlist = []
    for x in range(len(lista)):
        newlist.append(lista[x] - num)
    return newlist

def average(lista):
    soma = 0
    for item in lista:
        soma += item
    media = soma / len(lista)
    return media


def std_deviation(lista):
    media = average(lista)
    subtr = minus_num(lista, media)
    quadrad = [x ** 2 for x in subtr]   
    media_quadrad = average(quadrad)
    desvio_padrao = media_quadrad ** 0.5   #como não pude importar bibliotecas, a forma de fazer a raiz quadrada foi essa
    
    return desvio_padrao


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(std_deviation(lista)) 
