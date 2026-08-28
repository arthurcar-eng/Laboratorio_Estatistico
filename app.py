import streamlit as st
import pandas as pd
import numpy as np
import random
import math
import matplotlib.pyplot as plt

import src.estatistica as est


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Laboratório Estatístico",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# TÍTULO
# ============================================================

st.title("📊 Laboratório Estatístico")

st.write(
    "Aplicação desenvolvida para explorar um conjunto de dados "
    "real por meio de estatística descritiva, probabilidade, "
    "simulação, distribuições teóricas, correlação e regressão."
)

st.divider()


# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

try:

    dados = pd.read_csv("dados/online_shoppers.csv")

except FileNotFoundError:

    st.error(
        "❌ O arquivo dados/online_shoppers.csv não foi encontrado."
    )

    st.stop()


st.subheader("📋 Banco de Dados")

st.write(
    f"O conjunto de dados possui **{len(dados)} registros** "
    f"e **{len(dados.columns)} variáveis**."
)

st.dataframe(
    dados,
    use_container_width=True
)

st.divider()


# ============================================================
# VARIÁVEIS NUMÉRICAS
# ============================================================

colunas_numericas = list(
    dados.select_dtypes(include="number").columns
)

st.subheader("📊 Análise Estatística")

coluna = st.selectbox(
    "Escolha uma variável numérica:",
    colunas_numericas,
    key="variavel_principal"
)

lista = dados[coluna].dropna().tolist()


# ============================================================
# ESTATÍSTICAS DESCRITIVAS
# ============================================================

media_calculada = est.media(lista)
mediana_calculada = est.mediana(lista)
moda_calculada = est.moda(lista)
variancia_calculada = est.variancia(lista)
desvio_calculado = est.desvio_padrao(lista)
minimo_calculado = est.minimo(lista)
maximo_calculado = est.maximo(lista)
amplitude_calculada = est.amplitude(lista)

st.subheader("📐 Estatísticas Descritivas")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Média",
        f"{media_calculada:.2f}"
    )

with col2:
    st.metric(
        "Mediana",
        f"{mediana_calculada:.2f}"
    )

with col3:
    st.metric(
        "Moda",
        f"{moda_calculada:.2f}"
    )

with col4:
    st.metric(
        "Desvio padrão",
        f"{desvio_calculado:.2f}"
    )


col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(
        "Variância",
        f"{variancia_calculada:.2f}"
    )

with col6:
    st.metric(
        "Mínimo",
        f"{minimo_calculado:.2f}"
    )

with col7:
    st.metric(
        "Máximo",
        f"{maximo_calculado:.2f}"
    )

with col8:
    st.metric(
        "Amplitude",
        f"{amplitude_calculada:.2f}"
    )


# ============================================================
# COEFICIENTE DE VARIAÇÃO
# ============================================================

cv = est.coeficiente_variacao(lista)

st.write(
    f"**Coeficiente de variação:** {cv:.2f}%"
)

st.divider()


# ============================================================
# TABELA DE FREQUÊNCIAS
# ============================================================

st.subheader("📋 Tabela de Frequências")

numero_classes = st.slider(
    "Número de classes:",
    min_value=5,
    max_value=20,
    value=10,
    key="slider_frequencia"
)

frequencias = est.tabela_frequencia(
    lista,
    numero_classes
)

tabela_df = pd.DataFrame(frequencias)

st.dataframe(
    tabela_df,
    use_container_width=True
)

st.divider()


# ============================================================
# QUARTIS E OUTLIERS
# ============================================================

st.subheader("📊 Quartis e Detecção de Outliers")

q1 = est.primeiro_quartil(lista)
q2 = est.segundo_quartil(lista)
q3 = est.terceiro_quartil(lista)

iqr = est.intervalo_interquartil(lista)

outliers_lista = est.outliers(lista)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Q1",
        f"{q1:.4f}"
    )

with col2:
    st.metric(
        "Mediana (Q2)",
        f"{q2:.4f}"
    )

with col3:
    st.metric(
        "Q3",
        f"{q3:.4f}"
    )

with col4:
    st.metric(
        "IQR",
        f"{iqr:.4f}"
    )


limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

st.write("### Limites para detecção de outliers")

st.write(
    f"**Limite inferior:** {limite_inferior:.4f}"
)

st.write(
    f"**Limite superior:** {limite_superior:.4f}"
)

st.write(
    f"**Quantidade de outliers encontrados:** "
    f"{len(outliers_lista)}"
)

if len(outliers_lista) > 0:

    st.warning(
        f"Foram encontrados {len(outliers_lista)} outliers "
        "nessa variável."
    )

    st.write("### Valores considerados outliers")

    st.dataframe(
        pd.DataFrame(
            {coluna: outliers_lista}
        ),
        use_container_width=True
    )

else:

    st.success(
        "Nenhum outlier foi encontrado pela regra do IQR."
    )


# ============================================================
# INTERPRETAÇÃO AUTOMÁTICA
# ============================================================

st.subheader("🔎 Interpretação Automática")

st.write(
    f"**1º Quartil (Q1):** {q1:.4f}"
)

st.write(
    f"**Mediana (Q2):** {q2:.4f}"
)

st.write(
    f"**3º Quartil (Q3):** {q3:.4f}"
)

st.write(
    f"**Intervalo Interquartil (IQR):** {iqr:.4f}"
)

st.write(
    f"**Quantidade de outliers:** {len(outliers_lista)}"
)


if media_calculada > mediana_calculada:

    st.info(
        "📈 A média é maior que a mediana. "
        "Isso pode indicar uma assimetria à direita (positiva)."
    )

elif media_calculada < mediana_calculada:

    st.info(
        "📉 A média é menor que a mediana. "
        "Isso pode indicar uma assimetria à esquerda (negativa)."
    )

else:

    st.info(
        "⚖️ A média e a mediana são aproximadamente iguais."
    )


st.divider()


# ============================================================
# VISUALIZAÇÃO
# ============================================================

st.subheader("📈 Visualização dos Dados")


# Histograma

st.write("### Histograma")

fig_hist, ax_hist = plt.subplots(figsize=(9, 5))

ax_hist.hist(
    lista,
    bins=numero_classes
)

ax_hist.set_title(
    f"Histograma - {coluna}"
)

ax_hist.set_xlabel(coluna)
ax_hist.set_ylabel("Frequência")

st.pyplot(fig_hist)


# Boxplot

st.write("### Boxplot")

fig_box, ax_box = plt.subplots(figsize=(9, 4))

ax_box.boxplot(lista)

ax_box.set_title(
    f"Boxplot - {coluna}"
)

ax_box.set_ylabel(coluna)

st.pyplot(fig_box)


# ============================================================
# GRÁFICO DE CATEGÓRICA
# ============================================================

st.write("### Gráfico de Variável Categórica")

colunas_categoricas = list(
    dados.select_dtypes(
        include=["object", "bool"]
    ).columns
)

if len(colunas_categoricas) > 0:

    categoria = st.selectbox(
        "Escolha uma variável categórica:",
        colunas_categoricas,
        key="categoria_grafico"
    )

    contagem = dados[categoria].value_counts().head(15)

    fig_cat, ax_cat = plt.subplots(figsize=(10, 5))

    ax_cat.bar(
        contagem.index.astype(str),
        contagem.values
    )

    ax_cat.set_title(
        f"Frequência - {categoria}"
    )

    ax_cat.set_xlabel(categoria)
    ax_cat.set_ylabel("Quantidade")

    plt.xticks(rotation=45)

    st.pyplot(fig_cat)


st.divider()


# ============================================================
# DISTRIBUIÇÃO NORMAL
# ============================================================

st.subheader("📈 Distribuição Normal")

media_dados = est.media(lista)
desvio_dados = est.desvio_padrao(lista)

st.write(
    f"**Média estimada:** {media_dados:.4f}"
)

st.write(
    f"**Desvio padrão estimado:** {desvio_dados:.4f}"
)

valor = st.number_input(
    "Digite um valor:",
    value=float(media_dados),
    key="valor_normal"
)

densidade = est.probabilidade_normal(
    valor,
    media_dados,
    desvio_dados
)

st.write(
    f"**Densidade normal:** {densidade:.6f}"
)


fig_normal, ax_normal = plt.subplots(figsize=(9, 5))

if desvio_dados > 0:

    x_normal = np.linspace(
        min(lista),
        max(lista),
        300
    )

    y_normal = []

    for x_valor in x_normal:

        y_valor = est.probabilidade_normal(
            x_valor,
            media_dados,
            desvio_dados
        )

        y_normal.append(y_valor)

    ax_normal.hist(
        lista,
        bins=numero_classes,
        density=True,
        alpha=0.5
    )

    ax_normal.plot(
        x_normal,
        y_normal,
        linewidth=2
    )

    ax_normal.set_title(
        "Histograma + Distribuição Normal"
    )

    ax_normal.set_xlabel(coluna)
    ax_normal.set_ylabel("Densidade")

    st.pyplot(fig_normal)


st.divider()


# ============================================================
# DISTRIBUIÇÃO EXPONENCIAL
# ============================================================

st.subheader("📉 Distribuição Exponencial")

if media_dados > 0:

    lambda_exp = 1 / media_dados

    st.write(
        f"**λ estimado:** {lambda_exp:.6f}"
    )

    x_exp = np.linspace(
        0,
        max(lista),
        300
    )

    y_exp = []

    for valor_exp in x_exp:

        y = (
            lambda_exp
            * math.exp(
                -lambda_exp * valor_exp
            )
        )

        y_exp.append(y)

    fig_exp, ax_exp = plt.subplots(
        figsize=(9, 5)
    )

    ax_exp.hist(
        lista,
        bins=numero_classes,
        density=True,
        alpha=0.5
    )

    ax_exp.plot(
        x_exp,
        y_exp,
        linewidth=2
    )

    ax_exp.set_title(
        "Histograma + Distribuição Exponencial"
    )

    ax_exp.set_xlabel(coluna)
    ax_exp.set_ylabel("Densidade")

    st.pyplot(fig_exp)

else:

    st.warning(
        "A distribuição exponencial não pode ser "
        "calculada porque a média não é positiva."
    )


st.divider()


# ============================================================
# LEI DOS GRANDES NÚMEROS
# ============================================================

st.subheader("🎲 Lei dos Grandes Números")

st.write(
    "Este experimento simula lançamentos de uma moeda. "
    "Conforme o número de lançamentos aumenta, a frequência "
    "relativa de caras tende a se aproximar de 50%."
)

lancamentos = st.slider(
    "Número de lançamentos:",
    min_value=100,
    max_value=10000,
    value=1000,
    step=100,
    key="slider_lancamentos"
)

if st.button(
    "▶ Executar Lei dos Grandes Números",
    key="botao_lgg"
):

    caras = 0
    frequencias_caras = []

    for i in range(1, lancamentos + 1):

        resultado = random.randint(0, 1)

        if resultado == 1:
            caras += 1

        frequencia = caras / i

        frequencias_caras.append(
            frequencia
        )

    fig_lgg, ax_lgg = plt.subplots(
        figsize=(9, 5)
    )

    ax_lgg.plot(
        range(1, lancamentos + 1),
        frequencias_caras
    )

    ax_lgg.axhline(
        0.5,
        linestyle="--"
    )

    ax_lgg.set_title(
        "Lei dos Grandes Números"
    )

    ax_lgg.set_xlabel(
        "Número de lançamentos"
    )

    ax_lgg.set_ylabel(
        "Frequência relativa de caras"
    )

    st.pyplot(fig_lgg)

    st.write(
        f"**Frequência final de caras:** "
        f"{frequencias_caras[-1]:.4f}"
    )


st.divider()


# ============================================================
# TEOREMA CENTRAL DO LIMITE
# ============================================================

st.subheader("📊 Teorema Central do Limite")

st.write(
    "São retiradas várias amostras do conjunto de dados. "
    "Para cada amostra calculamos a média. "
    "A distribuição das médias tende a apresentar "
    "um comportamento aproximadamente normal."
)

tamanho_amostra = st.slider(
    "Tamanho de cada amostra:",
    min_value=2,
    max_value=100,
    value=30,
    key="slider_tcl_tamanho"
)

repeticoes = st.slider(
    "Número de repetições:",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100,
    key="slider_tcl_repeticoes"
)

if st.button(
    "▶ Executar TCL",
    key="botao_tcl"
):

    medias_amostrais = []

    for i in range(repeticoes):

        amostra = random.choices(
            lista,
            k=tamanho_amostra
        )

        media_amostra = est.media(
            amostra
        )

        medias_amostrais.append(
            media_amostra
        )

    fig_tcl, ax_tcl = plt.subplots(
        figsize=(9, 5)
    )

    ax_tcl.hist(
        medias_amostrais,
        bins=30
    )

    ax_tcl.set_title(
        "Teorema Central do Limite"
    )

    ax_tcl.set_xlabel(
        "Médias amostrais"
    )

    ax_tcl.set_ylabel(
        "Frequência"
    )

    st.pyplot(fig_tcl)

    st.write(
        f"**Média das médias amostrais:** "
        f"{est.media(medias_amostrais):.4f}"
    )


st.divider()


# ============================================================
# CORRELAÇÃO
# ============================================================

st.subheader("🔗 Correlação entre Variáveis")

coluna_corr_x = st.selectbox(
    "Variável X:",
    colunas_numericas,
    key="correlacao_x"
)

coluna_corr_y = st.selectbox(
    "Variável Y:",
    colunas_numericas,
    key="correlacao_y"
)

if coluna_corr_x != coluna_corr_y:

    x_corr = dados[
        coluna_corr_x
    ].dropna().tolist()

    y_corr = dados[
        coluna_corr_y
    ].dropna().tolist()

    tamanho = min(
        len(x_corr),
        len(y_corr)
    )

    x_corr = x_corr[:tamanho]
    y_corr = y_corr[:tamanho]

    correlacao = est.correlacao_pearson(
        x_corr,
        y_corr
    )

    cov = est.covariancia(
        x_corr,
        y_corr
    )

    st.write(
        f"**Covariância:** {cov:.4f}"
    )

    st.write(
        f"**Correlação de Pearson:** "
        f"{correlacao:.4f}"
    )

    if abs(correlacao) >= 0.7:

        st.info(
            "A relação linear entre as variáveis é forte."
        )

    elif abs(correlacao) >= 0.3:

        st.info(
            "A relação linear entre as variáveis é moderada."
        )

    else:

        st.info(
            "A relação linear entre as variáveis é fraca."
        )

else:

    st.warning(
        "Escolha duas variáveis diferentes."
    )


st.divider()


# ============================================================
# REGRESSÃO LINEAR
# ============================================================

st.subheader("📉 Regressão Linear")

st.write(
    "A regressão linear utiliza o método dos mínimos quadrados "
    "para encontrar a reta que melhor representa a relação "
    "entre duas variáveis."
)

coluna_x = st.selectbox(
    "Escolha a variável X:",
    colunas_numericas,
    index=0,
    key="regressao_x"
)

coluna_y = st.selectbox(
    "Escolha a variável Y:",
    colunas_numericas,
    index=1,
    key="regressao_y"
)

if coluna_x == coluna_y:

    st.warning(
        "⚠️ Escolha duas variáveis diferentes."
    )

else:

    x = dados[coluna_x].dropna().tolist()
    y = dados[coluna_y].dropna().tolist()

    tamanho = min(
        len(x),
        len(y)
    )

    x = x[:tamanho]
    y = y[:tamanho]

    media_x = est.media(x)
    media_y = est.media(y)

    numerador = 0
    denominador = 0

    for i in range(tamanho):

        numerador += (
            (x[i] - media_x)
            *
            (y[i] - media_y)
        )

        denominador += (
            (x[i] - media_x) ** 2
        )

    if denominador == 0:

        st.error(
            "Não é possível calcular a regressão "
            "porque X não possui variação."
        )

    else:

        a = numerador / denominador

        b = (
            media_y
            -
            a * media_x
        )

        # Correlação e R²

        correlacao_reg = est.correlacao_pearson(
            x,
            y
        )

        r2 = correlacao_reg ** 2

        st.write(
            f"**Coeficiente angular (a):** {a:.6f}"
        )

        st.write(
            f"**Coeficiente linear (b):** {b:.6f}"
        )

        st.write(
            f"**Coeficiente de correlação:** "
            f"{correlacao_reg:.6f}"
        )

        st.write(
            f"**R²:** {r2:.6f}"
        )

        st.success(
            f"### Equação da reta\n\n"
            f"**Y = {a:.6f}X + {b:.6f}**"
        )

        # ====================================================
        # GRÁFICO DA REGRESSÃO
        # ====================================================

        valores_x = sorted(x)

        valores_y = []

        for valor_x in valores_x:

            valor_y = (
                a * valor_x
                + b
            )

            valores_y.append(
                valor_y
            )

        fig_reg, ax_reg = plt.subplots(
            figsize=(9, 5)
        )

        ax_reg.scatter(
            x,
            y,
            alpha=0.5
        )

        ax_reg.plot(
            valores_x,
            valores_y,
            linewidth=2
        )

        ax_reg.set_xlabel(
            coluna_x
        )

        ax_reg.set_ylabel(
            coluna_y
        )

        ax_reg.set_title(
            f"Regressão Linear: "
            f"{coluna_x} × {coluna_y}"
        )

        st.pyplot(fig_reg)

        # ====================================================
        # PREDIÇÃO
        # ====================================================

        st.write("### 🔮 Predição Interativa")

        valor_x_predicao = st.number_input(
            "Digite um valor de X:",
            value=float(media_x),
            key="valor_predicao"
        )

        previsao = (
            a * valor_x_predicao
            + b
        )

        st.metric(
            "Valor previsto de Y",
            f"{previsao:.4f}"
        )

        st.warning(
            "⚠️ Correlação e regressão não significam "
            "necessariamente causalidade."
        )


st.divider()


# ============================================================
# VALIDAÇÃO COM NUMPY
# ============================================================
st.subheader("✅ Validação da Regressão com NumPy")

st.write(
    "Os coeficientes calculados manualmente são "
    "comparados com os resultados obtidos pelo NumPy."
)

if coluna_x != coluna_y:

    # Cálculo pelo NumPy
    x_numpy = np.array(x)
    y_numpy = np.array(y)

    media_x_numpy = np.mean(x_numpy)
    media_y_numpy = np.mean(y_numpy)

    numerador_numpy = np.sum(
        (x_numpy - media_x_numpy)
        *
        (y_numpy - media_y_numpy)
    )

    denominador_numpy = np.sum(
        (x_numpy - media_x_numpy) ** 2
    )

    if denominador_numpy != 0:

        a_numpy = (
            numerador_numpy
            /
            denominador_numpy
        )

        b_numpy = (
            media_y_numpy
            -
            a_numpy * media_x_numpy
        )

        correlacao_numpy = np.corrcoef(
            x_numpy,
            y_numpy
        )[0, 1]

        r2_numpy = correlacao_numpy ** 2

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                "**Coeficiente angular (a)**"
            )

            st.write(
                f"Nosso cálculo: **{a:.6f}**"
            )

            st.write(
                f"NumPy: **{a_numpy:.6f}**"
            )

        with col2:

            st.write(
                "**Coeficiente linear (b)**"
            )

            st.write(
                f"Nosso cálculo: **{b:.6f}**"
            )

            st.write(
                f"NumPy: **{b_numpy:.6f}**"
            )

        st.write(
            "**Correlação de Pearson**"
        )

        st.write(
            f"Nosso cálculo: **{correlacao_reg:.6f}**"
        )

        st.write(
            f"NumPy: **{correlacao_numpy:.6f}**"
        )

        st.write(
            "**R²**"
        )

        st.write(
            f"Nosso cálculo: **{r2:.6f}**"
        )

        st.write(
            f"NumPy: **{r2_numpy:.6f}**"
        )

        diferenca_a = abs(
            a - a_numpy
        )

        diferenca_b = abs(
            b - b_numpy
        )

        diferenca_correlacao = abs(
            correlacao_reg
            -
            correlacao_numpy
        )

        diferenca_r2 = abs(
            r2
            -
            r2_numpy
        )

        if (
            diferenca_a < 0.0001
            and
            diferenca_b < 0.0001
            and
            diferenca_correlacao < 0.0001
            and
            diferenca_r2 < 0.0001
        ):

            st.success(
                "✅ A regressão linear foi "
                "validada com sucesso pelo NumPy!"
            )

        else:

            st.error(
                "❌ Existem diferenças entre "
                "os cálculos."
            )
st.subheader("✅ Validação dos Resultados")

st.write(
    "Os resultados da nossa biblioteca estatística "
    "são comparados com o NumPy."
)

media_numpy = np.mean(lista)

mediana_numpy = np.median(lista)

variancia_numpy = np.var(
    lista,
    ddof=1
)

desvio_numpy = np.std(
    lista,
    ddof=1
)

col1, col2 = st.columns(2)

with col1:

    st.write(
        f"**Média**  \n"
        f"Nossa: {media_calculada:.4f}  \n"
        f"NumPy: {media_numpy:.4f}"
    )

    st.write(
        f"**Mediana**  \n"
        f"Nossa: {mediana_calculada:.4f}  \n"
        f"NumPy: {mediana_numpy:.4f}"
    )


with col2:

    st.write(
        f"**Variância**  \n"
        f"Nossa: {variancia_calculada:.4f}  \n"
        f"NumPy: {variancia_numpy:.4f}"
    )

    st.write(
        f"**Desvio padrão**  \n"
        f"Nossa: {desvio_calculado:.4f}  \n"
        f"NumPy: {desvio_numpy:.4f}"
    )


if (
    abs(
        media_calculada
        -
        media_numpy
    ) < 0.0001

    and

    abs(
        mediana_calculada
        -
        mediana_numpy
    ) < 0.0001

    and

    abs(
        variancia_calculada
        -
        variancia_numpy
    ) < 0.0001

    and

    abs(
        desvio_calculado
        -
        desvio_numpy
    ) < 0.0001
):

    st.success(
        "✅ Todos os resultados foram "
        "validados com sucesso!"
    )

else:

    st.error(
        "❌ Existem diferenças entre os cálculos."
    )


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.caption(
    "Laboratório Estatístico — "
    "Matemática e Estatística para Computação"
)