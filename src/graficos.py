import matplotlib.pyplot as plt


def histograma(lista, nome_coluna):
    plt.figure(figsize=(8, 4))

    plt.hist(lista, bins=10)

    plt.title(f"Histograma - {nome_coluna}")
    plt.xlabel(nome_coluna)
    plt.ylabel("Frequência")

    return plt


def boxplot(lista, nome_coluna):
    plt.figure(figsize=(6, 4))

    plt.boxplot(lista)

    plt.title(f"Boxplot - {nome_coluna}")
    plt.ylabel(nome_coluna)

    return plt


def grafico_barras(lista, nome_coluna):
    plt.figure(figsize=(8, 4))

    valores = sorted(list(set(lista)))
    frequencias = []

    for valor in valores:
        frequencias.append(lista.count(valor))

    plt.bar(valores, frequencias)

    plt.title(f"Gráfico de Barras - {nome_coluna}")
    plt.xlabel(nome_coluna)
    plt.ylabel("Frequência")

    return plt