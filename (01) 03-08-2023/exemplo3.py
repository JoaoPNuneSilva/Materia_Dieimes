def calcular_media(numeros):
    total = sum(numeros)
    quantidade = len(numeros)
    media = total / quantidade
    return media
lista_numeros = [10, 20, 30, 40, 50]
media_calculada = calcular_media(lista_numeros)
print("A média dos números é:", media_calculada)