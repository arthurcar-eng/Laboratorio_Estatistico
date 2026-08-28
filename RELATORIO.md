# 📊 Relatório — Laboratório Estatístico

## Matemática e Estatística para Computação

### Identificação

**Integrante:** Arthur Cardoso Assunção  
**Matrícula:** RA: 72650172

---

# 1. Introdução

Este projeto apresenta o desenvolvimento de um Laboratório Estatístico
Interativo utilizando Python e Streamlit.

O objetivo é aplicar conceitos de Matemática e Estatística para Computação
em um conjunto de dados real, implementando manualmente as principais
funções estatísticas e posteriormente validando seus resultados com
bibliotecas consolidadas.

A aplicação permite realizar estatística descritiva, análise de outliers,
visualizações, simulações, análise de distribuições teóricas, correlação e
regressão linear.

---

# 2. Dataset

Foi utilizado o conjunto de dados:

**Online Shoppers Purchasing Intention Dataset**

Fonte: **UCI Machine Learning Repository**

Link original:

https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

O arquivo utilizado pela aplicação possui **12.330 registros e 18 variáveis**.

Cada registro representa uma sessão de navegação de um usuário em um site
de comércio eletrônico.

O conjunto contém informações relacionadas ao comportamento de navegação,
incluindo quantidade e duração de páginas visitadas, taxa de rejeição,
taxa de saída e informações relacionadas à realização de compras.

## 2.1 Justificativa da escolha

O dataset foi escolhido por possuir quantidade suficiente de registros e
diversidade de variáveis numéricas e categóricas.

Além disso, o contexto de comércio eletrônico permite aplicar diferentes
técnicas estatísticas e investigar relações entre o comportamento de
navegação dos usuários e as características das sessões.

---

# 3. Núcleo Estatístico Próprio

O núcleo matemático foi separado da interface e implementado no arquivo:

`src/estatistica.py`

As principais medidas estatísticas foram programadas manualmente, evitando
o uso de funções estatísticas prontas para gerar os resultados principais
apresentados pela aplicação.

NumPy e outras bibliotecas são utilizadas principalmente para validação.

---

# 4. Fórmulas Utilizadas

## 4.1 Média aritmética

A média é definida por:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

onde $x_i$ representa cada observação e $n$ representa o número de
observações.

---

## 4.2 Mediana

A mediana representa o valor central dos dados após sua ordenação.

Para quantidade ímpar de observações, utiliza-se o elemento central.

Para quantidade par, utiliza-se a média dos dois elementos centrais.

---

## 4.3 Moda

A moda corresponde ao valor que apresenta a maior frequência no conjunto
de dados.

---

## 4.4 Amplitude

A amplitude é calculada por:

$$
A = x_{max} - x_{min}
$$

---

## 4.5 Variância populacional

$$
\sigma^2 =
\frac{1}{n}
\sum_{i=1}^{n}(x_i-\mu)^2
$$

---

## 4.6 Variância amostral

$$
s^2 =
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

---

## 4.7 Desvio padrão

O desvio padrão corresponde à raiz quadrada da variância:

$$
s = \sqrt{s^2}
$$

Para a população:

$$
\sigma = \sqrt{\sigma^2}
$$

---

## 4.8 Quartis e percentis

Os quartis dividem os dados ordenados em quatro partes.

- Q1 corresponde ao percentil 25;
- Q2 corresponde ao percentil 50 e representa a mediana;
- Q3 corresponde ao percentil 75.

---

## 4.9 Intervalo Interquartil

$$
IQR = Q_3-Q_1
$$

A regra utilizada para identificação de outliers considera:

$$
L_{inferior}=Q_1-1.5(IQR)
$$

$$
L_{superior}=Q_3+1.5(IQR)
$$

Valores abaixo do limite inferior ou acima do limite superior são
classificados como possíveis outliers.

---

## 4.10 Coeficiente de variação

$$
CV =
\frac{s}{\bar{x}}
\times 100
$$

O coeficiente de variação expressa a dispersão relativa dos dados em
relação à média.

---

## 4.11 Covariância amostral

$$
Cov(X,Y)=
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
n-1
}
$$

---

## 4.12 Correlação de Pearson

$$
r =
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}
\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}
}
$$

O coeficiente varia entre -1 e 1.

Valores próximos de 1 indicam forte relação linear positiva, valores
próximos de -1 indicam forte relação linear negativa e valores próximos
de zero indicam relação linear fraca.

---

# 5. Módulo 0 — Dados Reais

O arquivo `online_shoppers.csv` é carregado utilizando Pandas.

A aplicação informa automaticamente a quantidade de registros e variáveis
e apresenta os dados em uma tabela interativa.

O conjunto utilizado possui 12.330 registros e 18 variáveis.

---

# 6. Módulo 1 — Biblioteca Estatística

A biblioteca própria implementa funções para:

- média;
- mediana;
- moda;
- mínimo;
- máximo;
- amplitude;
- variância amostral;
- variância populacional;
- desvio padrão amostral;
- desvio padrão populacional;
- quartis;
- percentis;
- intervalo interquartil;
- coeficiente de variação;
- covariância;
- correlação de Pearson;
- tabela de frequências;
- identificação de outliers.

---

# 7. Módulo 2 — Estatística Descritiva Interativa

O usuário seleciona uma variável numérica diretamente na interface.

A aplicação apresenta medidas de tendência central e dispersão calculadas
pela biblioteca estatística própria.

Também são apresentados:

- tabela de frequências com número de classes ajustável;
- quartis;
- intervalo interquartil;
- limites para outliers;
- quantidade e valores dos outliers;
- histograma;
- boxplot.

Para variáveis categóricas, a aplicação disponibiliza um gráfico de barras.

A interpretação automática compara média e mediana para indicar uma
possível assimetria à direita, à esquerda ou uma distribuição mais
equilibrada.

---

# 8. Módulo 3 — Probabilidade e Simulação

## 8.1 Lei dos Grandes Números

Foi desenvolvido um experimento de Monte Carlo baseado em lançamentos
simulados de uma moeda.

Cada lançamento possui dois resultados possíveis.

A aplicação calcula continuamente a frequência relativa de caras.

Com o aumento do número de lançamentos, é possível observar a frequência
relativa se aproximando do valor teórico de 0,5.

O usuário controla a quantidade de lançamentos por meio da interface.

## 8.2 Teorema Central do Limite

A aplicação sorteia repetidamente amostras da variável selecionada no
dataset.

Para cada amostra é calculada a média utilizando a função implementada
pela equipe.

O usuário pode alterar:

- tamanho de cada amostra;
- número de repetições.

O histograma das médias amostrais permite observar que, sob as condições
do experimento, sua distribuição tende a assumir comportamento
aproximadamente Normal conforme o processo de amostragem é repetido.

---

# 9. Módulo 4 — Distribuições Teóricas

Foram utilizadas duas distribuições teóricas:

- Distribuição Normal;
- Distribuição Exponencial.

## 9.1 Distribuição Normal

A média e o desvio padrão são estimados a partir da variável escolhida.

A função densidade Normal utilizada é:

$$
f(x)=
\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{1}{2}
\left(\frac{x-\mu}{\sigma}\right)^2}
$$

A curva é sobreposta ao histograma dos dados para permitir comparação
visual.

## 9.2 Distribuição Exponencial

O parâmetro da distribuição Exponencial é estimado por:

$$
\lambda = \frac{1}{\bar{x}}
$$

Sua função densidade é:

$$
f(x)=\lambda e^{-\lambda x}, \quad x\geq0
$$

A curva também é comparada visualmente com o histograma.

A qualidade do ajuste é avaliada visualmente pela proximidade entre a
forma do histograma observado e a curva teórica.

---

# 10. Módulo 5 — Correlação e Regressão Linear

O usuário seleciona duas variáveis numéricas, X e Y.

A aplicação apresenta o diagrama de dispersão, covariância e correlação
de Pearson.

A regressão linear simples é calculada pelo método dos mínimos quadrados.

A reta possui a forma:

$$
\hat{Y}=aX+b
$$

O coeficiente angular é calculado por:

$$
a =
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
$$

O intercepto é calculado por:

$$
b=\bar{y}-a\bar{x}
$$

A aplicação apresenta:

- coeficiente angular;
- coeficiente linear;
- equação da reta;
- coeficiente de correlação;
- R²;
- gráfico de dispersão;
- reta ajustada;
- predição interativa.

O usuário pode informar um valor de X e receber o valor previsto de Y.

O coeficiente angular representa a alteração estimada em Y para cada
aumento de uma unidade em X.

O coeficiente linear representa o valor estimado de Y quando X é igual
a zero.

O R² indica a proporção da variabilidade de Y explicada pelo modelo
linear simples.

A aplicação também apresenta o alerta de que **correlação não implica
causalidade**.

---

# 11. Validação

Os resultados produzidos pelas funções próprias são comparados com
bibliotecas consolidadas.

A aplicação realiza comparações com NumPy para medidas como média,
mediana, variância, desvio padrão, correlação e regressão.

Também foram desenvolvidos testes automatizados utilizando Pytest.

A tolerância numérica adotada nas comparações deve ser documentada
junto aos testes automatizados.

Na versão final, os testes devem ser executados com:

```bash
python -m pytest -v
```

---

# 12. Módulo 6 — Descobertas Estatísticas

Nesta seção são apresentadas as três descobertas mais interessantes
obtidas por meio da análise do dataset.

# 12. Módulo 6 — Descobertas Estatísticas

A análise realizada pelo Laboratório Estatístico revelou padrões relevantes
sobre o comportamento dos usuários do site de comércio eletrônico.

## Descoberta 1 — Apenas 15,47% das sessões resultaram em compra

Das **12.330 sessões** presentes no dataset, apenas **1.908 resultaram em
compra**, correspondendo a aproximadamente **15,47%** do total.

As outras **10.422 sessões**, equivalentes a aproximadamente **84,53%**,
não resultaram em compra.

Esse resultado mostra que a maior parte das sessões de navegação não termina
em uma conversão, evidenciando um forte desbalanceamento entre sessões com
e sem compra.

---

## Descoberta 2 — BounceRates e ExitRates possuem correlação muito forte

A correlação de Pearson entre as variáveis **BounceRates** e **ExitRates**
foi de aproximadamente:

**r = 0,9130**

Esse valor indica uma **forte correlação linear positiva** entre as duas
variáveis.

Portanto, sessões que apresentam maiores taxas de rejeição também tendem
a apresentar maiores taxas de saída.

Apesar da forte associação encontrada, esse resultado não permite afirmar
que uma variável causa a outra, pois **correlação não implica causalidade**.

---

## Descoberta 3 — PageValues é muito maior nas sessões que resultam em compra

Foi observada uma diferença expressiva na variável **PageValues** entre
sessões que resultaram ou não em compra.

Nas sessões **sem compra**, o PageValues médio foi aproximadamente:

**1,98**

e a mediana foi:

**0,00**

Nas sessões **com compra**, o PageValues médio foi aproximadamente:

**27,26**

e a mediana foi:

**16,76**

Isso significa que o PageValues médio das sessões que terminaram em compra
foi aproximadamente **13,8 vezes maior** do que nas sessões sem compra.

Esse resultado mostra uma forte associação entre valores elevados de
PageValues e a ocorrência de compra no conjunto analisado.
---

# 13. Capturas de Tela

## 13.1 Estatística Descritiva

![Estatística Descritiva](imagens/estatistica_descritiva.png)

## 13.2 Simulações e Distribuições

![Simulações](imagens/simulacao.png)

## 13.3 Correlação e Regressão Linear

![Regressão Linear](imagens/regressao.png)

## 13.4 Validação

![Validação](imagens/validacao.png)

---

# 14. Tecnologias Utilizadas

- Python;
- Streamlit;
- Pandas;
- NumPy;
- Matplotlib;
- SciPy;
- Pytest.

---

# 15. Conclusão

O Laboratório Estatístico permitiu aplicar conceitos matemáticos e
estatísticos por meio da programação.

As principais medidas estatísticas foram implementadas manualmente,
permitindo compreender como as fórmulas são transformadas em algoritmos.

A utilização de um dataset real possibilitou explorar estatística
descritiva, identificação de outliers, distribuições de probabilidade,
simulações, correlação e regressão linear.

A comparação com bibliotecas consolidadas e a utilização de testes
automatizados contribuíram para verificar a corretude das implementações.

Por fim, a interface desenvolvida em Streamlit tornou a análise
interativa, permitindo ao usuário modificar variáveis e parâmetros e
observar seus efeitos nos resultados.