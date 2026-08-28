import pytest

from src.estatistica import (
    media,
    mediana,
    moda,
    minimo,
    maximo,
    amplitude,
    variancia,
    desvio_padrao,
    primeiro_quartil,
    segundo_quartil,
    terceiro_quartil,
    intervalo_interquartil,
    limites_outliers,
    outliers,
    tabela_frequencia,
    covariancia,
    correlacao_pearson,
    variancia_populacional,
    desvio_padrao_populacional,
    coeficiente_variacao,
)


# ============================================================
# ESTATÍSTICA DESCRITIVA
# ============================================================

def test_media():
    assert media([1, 2, 3, 4, 5]) == 3


def test_mediana():
    assert mediana([1, 2, 3, 4, 5]) == 3
    assert mediana([1, 2, 3, 4]) == 2.5


def test_moda():
    assert moda([1, 2, 2, 3, 4]) == 2


def test_minimo():
    assert minimo([5, 2, 8, 1, 4]) == 1


def test_maximo():
    assert maximo([5, 2, 8, 1, 4]) == 8


def test_amplitude():
    assert amplitude([1, 2, 3, 4, 5]) == 4


def test_variancia():
    assert variancia([1, 2, 3, 4, 5]) == pytest.approx(2.5)


def test_desvio_padrao():
    assert desvio_padrao([1, 2, 3, 4, 5]) == pytest.approx(2.5 ** 0.5)


# ============================================================
# QUARTIS
# ============================================================

def test_quartis():
    lista = [1, 2, 3, 4, 5]

    assert primeiro_quartil(lista) == 2
    assert segundo_quartil(lista) == 3
    assert terceiro_quartil(lista) == 4


def test_iqr():
    lista = [1, 2, 3, 4, 5]

    assert intervalo_interquartil(lista) == 2


# ============================================================
# OUTLIERS
# ============================================================

def test_limites_outliers():
    lista = [1, 2, 3, 4, 5]

    inferior, superior = limites_outliers(lista)

    assert inferior == -1
    assert superior == 7


def test_outliers():
    lista = [1, 2, 3, 4, 5, 100]

    resultado = outliers(lista)

    assert 100 in resultado


# ============================================================
# TABELA DE FREQUÊNCIAS
# ============================================================

def test_tabela_frequencia():
    lista = [1, 2, 3, 4, 5]

    tabela = tabela_frequencia(lista, 3)

    assert len(tabela) == 3

    total = sum(
        linha["Frequência"]
        for linha in tabela
    )

    assert total == 5


# ============================================================
# COVARIÂNCIA E CORRELAÇÃO
# ============================================================

def test_covariancia():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    assert covariancia(x, y) == pytest.approx(5.0)


def test_correlacao_pearson():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    assert correlacao_pearson(x, y) == pytest.approx(1.0)


# ============================================================
# VARIÂNCIA POPULACIONAL
# ============================================================

def test_variancia_populacional():
    lista = [1, 2, 3, 4, 5]

    assert variancia_populacional(lista) == pytest.approx(2.0)


def test_desvio_padrao_populacional():
    lista = [1, 2, 3, 4, 5]

    assert desvio_padrao_populacional(lista) == pytest.approx(2 ** 0.5)


# ============================================================
# COEFICIENTE DE VARIAÇÃO
# ============================================================

def test_coeficiente_variacao():
    lista = [1, 2, 3, 4, 5]

    resultado = coeficiente_variacao(lista)

    assert resultado == pytest.approx(52.7046276695)
# ============================================================
# VALIDAÇÃO COM BIBLIOTECAS DE REFERÊNCIA
# ============================================================

import numpy as np
from scipy import stats

TOLERANCIA = 1e-6


def test_media_vs_numpy():
    dados = [1, 2, 3, 4, 5, 10]

    assert media(dados) == pytest.approx(
        np.mean(dados),
        abs=TOLERANCIA
    )


def test_mediana_vs_numpy():
    dados = [1, 2, 3, 4, 5, 10]

    assert mediana(dados) == pytest.approx(
        np.median(dados),
        abs=TOLERANCIA
    )


def test_moda_vs_scipy():
    dados = [1, 2, 2, 3, 4, 5]

    resultado_scipy = stats.mode(
        dados,
        keepdims=False
    ).mode

    assert moda(dados) == pytest.approx(
        resultado_scipy,
        abs=TOLERANCIA
    )


def test_minimo_vs_numpy():
    dados = [5, 2, 8, 1, 4]

    assert minimo(dados) == pytest.approx(
        np.min(dados),
        abs=TOLERANCIA
    )


def test_maximo_vs_numpy():
    dados = [5, 2, 8, 1, 4]

    assert maximo(dados) == pytest.approx(
        np.max(dados),
        abs=TOLERANCIA
    )


def test_amplitude_vs_numpy():
    dados = [5, 2, 8, 1, 4]

    assert amplitude(dados) == pytest.approx(
        np.ptp(dados),
        abs=TOLERANCIA
    )


def test_variancia_amostral_vs_numpy():
    dados = [1, 2, 3, 4, 5, 10]

    assert variancia(dados) == pytest.approx(
        np.var(dados, ddof=1),
        abs=TOLERANCIA
    )


def test_desvio_padrao_amostral_vs_numpy():
    dados = [1, 2, 3, 4, 5, 10]

    assert desvio_padrao(dados) == pytest.approx(
        np.std(dados, ddof=1),
        abs=TOLERANCIA
    )


def test_variancia_populacional_vs_numpy():
    dados = [1, 2, 3, 4, 5, 10]

    assert variancia_populacional(dados) == pytest.approx(
        np.var(dados, ddof=0),
        abs=TOLERANCIA
    )


def test_desvio_padrao_populacional_vs_numpy():
    dados = [1, 2, 3, 4, 5, 10]

    assert desvio_padrao_populacional(dados) == pytest.approx(
        np.std(dados, ddof=0),
        abs=TOLERANCIA
    )


def test_quartis_vs_numpy():
    dados = [1, 2, 3, 4, 5, 6, 7]

    assert primeiro_quartil(dados) == pytest.approx(
        np.percentile(dados, 25),
        abs=TOLERANCIA
    )

    assert segundo_quartil(dados) == pytest.approx(
        np.percentile(dados, 50),
        abs=TOLERANCIA
    )

    assert terceiro_quartil(dados) == pytest.approx(
        np.percentile(dados, 75),
        abs=TOLERANCIA
    )


def test_iqr_vs_numpy():
    dados = [1, 2, 3, 4, 5, 6, 7]

    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)

    assert intervalo_interquartil(dados) == pytest.approx(
        q3 - q1,
        abs=TOLERANCIA
    )


def test_covariancia_vs_numpy():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 8, 10]

    resultado_numpy = np.cov(
        x,
        y,
        ddof=1
    )[0, 1]

    assert covariancia(x, y) == pytest.approx(
        resultado_numpy,
        abs=TOLERANCIA
    )


def test_correlacao_pearson_vs_numpy():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 8, 10]

    resultado_numpy = np.corrcoef(
        x,
        y
    )[0, 1]

    assert correlacao_pearson(x, y) == pytest.approx(
        resultado_numpy,
        abs=TOLERANCIA
    )


def test_coeficiente_variacao_vs_numpy():
    dados = [1, 2, 3, 4, 5, 10]

    resultado_numpy = (
        np.std(dados, ddof=1)
        / np.mean(dados)
    ) * 100

    assert coeficiente_variacao(dados) == pytest.approx(
        resultado_numpy,
        abs=TOLERANCIA
    )