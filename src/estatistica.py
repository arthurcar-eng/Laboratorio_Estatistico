# ============================================================
# BIBLIOTECA ESTATÍSTICA PRÓPRIA
# Matemática e Estatística para Computação
# Laboratório Estatístico
# ============================================================


# ============================================================
# FUNÇÕES BÁSICAS
# ============================================================

def media(lista):
    """Calcula a média aritmética."""
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    soma = 0

    for numero in lista:
        soma += numero

    return soma / len(lista)


def minimo(lista):
    """Retorna o menor valor da lista."""
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    menor = lista[0]

    for numero in lista:
        if numero < menor:
            menor = numero

    return menor


def maximo(lista):
    """Retorna o maior valor da lista."""
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior


def amplitude(lista):
    """Calcula a amplitude total."""
    return maximo(lista) - minimo(lista)


# ============================================================
# MEDIANA E MODA
# ============================================================

def mediana(lista):
    """Calcula a mediana."""
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    dados = sorted(lista)

    tamanho = len(dados)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        return (dados[meio - 1] + dados[meio]) / 2

    return dados[meio]


def moda(lista):
    """Calcula a moda."""
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    contagem = {}

    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    maior_frequencia = max(contagem.values())

    for numero in contagem:
        if contagem[numero] == maior_frequencia:
            return numero


# ============================================================
# VARIÂNCIA E DESVIO PADRÃO
# ============================================================

def variancia(lista):
    """
    Variância amostral.
    Divide por n - 1.
    """
    if len(lista) < 2:
        raise ValueError(
            "São necessários pelo menos 2 valores."
        )

    m = media(lista)

    soma = 0

    for numero in lista:
        soma += (numero - m) ** 2

    return soma / (len(lista) - 1)


def desvio_padrao(lista):
    """Calcula o desvio padrão amostral."""
    return variancia(lista) ** 0.5


def variancia_populacional(lista):
    """Calcula a variância populacional."""
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    m = media(lista)

    soma = 0

    for numero in lista:
        soma += (numero - m) ** 2

    return soma / len(lista)


def desvio_padrao_populacional(lista):
    """Calcula o desvio padrão populacional."""
    return variancia_populacional(lista) ** 0.5


# ============================================================
# PERCENTIS E QUARTIS
# ============================================================

def percentil(lista, p):
    """
    Calcula um percentil usando interpolação linear.

    p deve estar entre 0 e 100.
    """
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    if p < 0 or p > 100:
        raise ValueError(
            "O percentil deve estar entre 0 e 100."
        )

    dados = sorted(lista)

    posicao = (len(dados) - 1) * (p / 100)

    inferior = int(posicao)
    superior = inferior + 1

    if superior >= len(dados):
        return dados[inferior]

    parte_decimal = posicao - inferior

    return (
        dados[inferior]
        + parte_decimal
        * (dados[superior] - dados[inferior])
    )


def primeiro_quartil(lista):
    """Calcula o primeiro quartil (Q1)."""
    return percentil(lista, 25)


def segundo_quartil(lista):
    """Calcula o segundo quartil (Q2/mediana)."""
    return percentil(lista, 50)


def terceiro_quartil(lista):
    """Calcula o terceiro quartil (Q3)."""
    return percentil(lista, 75)


def intervalo_interquartil(lista):
    """Calcula o IQR."""
    q1 = primeiro_quartil(lista)
    q3 = terceiro_quartil(lista)

    return q3 - q1


# ============================================================
# DETECÇÃO DE OUTLIERS
# ============================================================

def limites_outliers(lista):
    """
    Calcula os limites inferior e superior
    usando a regra de 1,5 × IQR.
    """
    q1 = primeiro_quartil(lista)
    q3 = terceiro_quartil(lista)

    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    return limite_inferior, limite_superior


def outliers(lista):
    """Retorna os valores considerados outliers."""
    limite_inferior, limite_superior = limites_outliers(lista)

    resultado = []

    for numero in lista:
        if (
            numero < limite_inferior
            or numero > limite_superior
        ):
            resultado.append(numero)

    return resultado


# ============================================================
# TABELA DE FREQUÊNCIAS
# ============================================================

def tabela_frequencia(lista, numero_classes=10):
    """
    Cria uma tabela de frequências para dados numéricos.

    Retorna:
    - Classe
    - Frequência
    - Frequência relativa (%)
    """

    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")

    if numero_classes < 1:
        raise ValueError(
            "O número de classes deve ser maior que zero."
        )

    minimo_valor = minimo(lista)
    maximo_valor = maximo(lista)

    amplitude_valor = (
        maximo_valor - minimo_valor
    )

    # Caso todos os valores sejam iguais
    if amplitude_valor == 0:
        return [
            {
                "Classe": str(minimo_valor),
                "Frequência": len(lista),
                "Frequência relativa (%)": 100.0
            }
        ]

    largura = (
        amplitude_valor / numero_classes
    )

    tabela = []

    for i in range(numero_classes):

        limite_inferior = (
            minimo_valor + i * largura
        )

        limite_superior = (
            minimo_valor + (i + 1) * largura
        )

        frequencia = 0

        for numero in lista:

            # Última classe inclui o limite superior
            if i == numero_classes - 1:

                if (
                    numero >= limite_inferior
                    and numero <= limite_superior
                ):
                    frequencia += 1

            else:

                if (
                    numero >= limite_inferior
                    and numero < limite_superior
                ):
                    frequencia += 1

        frequencia_relativa = (
            frequencia / len(lista)
        ) * 100

        tabela.append(
            {
                "Classe":
                    f"{limite_inferior:.2f} - "
                    f"{limite_superior:.2f}",

                "Frequência":
                    frequencia,

                "Frequência relativa (%)":
                    frequencia_relativa
            }
        )

    return tabela


# ============================================================
# COEFICIENTE DE VARIAÇÃO
# ============================================================

def coeficiente_variacao(lista):
    """
    Calcula o coeficiente de variação em porcentagem.
    """
    m = media(lista)

    if m == 0:
        return 0

    return (
        desvio_padrao(lista) / m
    ) * 100


# ============================================================
# COVARIÂNCIA
# ============================================================

def covariancia(lista_x, lista_y):
    """
    Calcula a covariância amostral.
    """
    if len(lista_x) != len(lista_y):
        raise ValueError(
            "As listas devem possuir o mesmo tamanho."
        )

    if len(lista_x) < 2:
        raise ValueError(
            "São necessários pelo menos 2 valores."
        )

    media_x = media(lista_x)
    media_y = media(lista_y)

    soma = 0

    for i in range(len(lista_x)):

        soma += (
            (lista_x[i] - media_x)
            *
            (lista_y[i] - media_y)
        )

    return soma / (len(lista_x) - 1)


# ============================================================
# CORRELAÇÃO DE PEARSON
# ============================================================

def correlacao_pearson(lista_x, lista_y):
    """
    Calcula o coeficiente de correlação de Pearson.
    """
    cov = covariancia(
        lista_x,
        lista_y
    )

    desvio_x = desvio_padrao(lista_x)
    desvio_y = desvio_padrao(lista_y)

    if desvio_x == 0 or desvio_y == 0:
        return 0

    return (
        cov
        /
        (desvio_x * desvio_y)
    )


# ============================================================
# DISTRIBUIÇÃO NORMAL
# ============================================================

def probabilidade_normal(
    x,
    media_valor,
    desvio
):
    """
    Calcula a função densidade da distribuição Normal.
    """
    import math

    if desvio <= 0:
        return 0

    z = (
        x - media_valor
    ) / desvio

    densidade = (
        1
        /
        (
            desvio
            *
            math.sqrt(2 * math.pi)
        )
    ) * math.exp(
        -(z ** 2) / 2
    )

    return densidade