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