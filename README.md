# 🎵 Spotify Recommendation System

Projeto de Machine Learning para recomendação de músicas usando características musicais extraídas do Spotify.

O objetivo foi desenvolver um sistema que identifica músicas semelhantes a uma referência utilizando técnicas de recomendação baseada em conteúdo (*Content-Based Filtering*).

---

# 🎯 Problema de Negócio

Plataformas de streaming musical utilizam sistemas de recomendação aumentando o engajamento dos usuários e facilitando a descoberta de novas músicas.

Nesse projeto, busquei responder algumas perguntas --

* É possível recomendar músicas semelhantes usando apenas características musicais?
* Quais atributos melhor representam a similaridade entre músicas?
* Como medir proximidade entre músicas?
* O algoritmo Nearest Neighbors consegue produzir recomendações coerentes?

---

# 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Scikit-Learn
* Matplotlib
* Jupyter Notebook
* Git
* GitHub

---

# 📂 Estrutura do Projeto

```text
spotify-recommendation-system/
│
├── data/
│   └── dataset.csv
│
├── functions/
│   ├── __init__.py
│   └── recommendation.py
│
├── images/
│   ├── Believer_recommendations_scatter.png
│   ├── features_histogram.png
│   └── PCA_spotify_scatter.png
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_recommendation_model.ipynb
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 📈 Etapas da Análise

## 🔹 Análise Exploratória (EDA)

Fiz uma análise inicial do dataset para entender sua estrutura.

Principais verificações --

* Quantidade de registros e atributos
* Valores nulos
* Valores duplicados
* Distribuição das variáveis
* Características dos gêneros musicais

Também construí histogramas para analisar o comportamento das principais features utilizadas pelo modelo.

### Features analisadas

* Danceability
* Energy
* Loudness
* Speechiness
* Acousticness
* Instrumentalness
* Liveness
* Valence
* Tempo

---

## 🔹 Limpeza e Pré-processamento

As seguintes etapas foram realizadas -

* Remoção de registros com valores nulos
* Remoção da coluna auxiliar `Unnamed: 0`
* Seleção das features relevantes para recomendação
* Padronização dos dados utilizando **StandardScaler**

O escalonamento foi necessário porque algumas variáveis possuem escalas muito diferentes, o que poderia impactar diretamente o cálculo das distâncias entre músicas.

---

## 🔹 Construção do Modelo

O algoritmo escolhido foi --

### Nearest Neighbors (KNN)

O modelo calcula a distância entre músicas utilizando suas características musicais.

Músicas com menor distância são consideradas mais semelhantes.

Configuração que usei para o treinamento:

```python
NearestNeighbors(
    metric="euclidean"
)
```

Durante a geração das recomendações, o sistema busca inicialmente um conjunto maior de vizinhos e depois reorganiza os resultados para produzir recomendações mais relevantes.

---

# 📊 Visualização com PCA

Como cada música é representada por nove características musicais, usei a técnica PCA (*Principal Component Analysis*) reduzindo os dados para duas dimensões.

Isso facilitou visualizar --

* A distribuição geral das músicas
* A posição da música consultada
* A proximidade das recomendações geradas

As duas componentes principais preservaram **48% da variabilidade original dos dados**.

---

# 🔍 Sistema de Recomendação

O sistema foi dividido em duas responsabilidades principais --

### recommendation_song()

Responsável por -- 

* localizar a música pesquisada;
* validar artista (se for informado);
* levar a busca ao mecanismo de recomendação.

### recommend_by_index()

Responsável por -- 

* localizar os vizinhos com o Nearest Neighbors;
* priorizar recomendações do mesmo gênero musical;
* limitar a quantidade de recomendações retornadas;
* validar a quantidade solicitada pelo usuário.

A função principal pode ser utilizada assim -- 

```python
recommendation_song(
    song_name="Believer",
    qtd_musicas_buscar=10
)
```

ou

```python
recommendation_song(
    song_name="Shape Of You",
    artist="Andrew Foy",
    qtd_musicas_buscar=10
)
```

Cada recomendação retorna --

* Nome da música
* Artista
* Álbum
* Gênero musical

---

# 🚀 Melhorias Implementadas

Depois da primeira versão do projeto, adicionei melhorias o sistema ficar mais flexível e produzir recomendações mais relevantes.

## Priorização por gênero musical

O algoritmo continua encontrando músicas semelhantes usando apenas características sonoras.

Após a busca dos vizinhos, as recomendações são reorganizadas para priorizar músicas pertencentes ao mesmo `track_genre` da música consultada.

Caso não existam recomendações suficientes do mesmo gênero, músicas de outros gêneros também são aparecem para preservar a quantidade de resultados.

---

## Quantidade configurável de recomendações

O usuário pode escolher quantas recomendações deseja receber através do parâmetro --

```python
qtd_musicas_buscar
```

Além disso, a função realiza validações para impedir valores inválidos.

---

## Refatoração

Coloquei parte da lógica da função principal em um módulo separado (`functions/recommendation.py`), reduzindo duplicação de código e deixando o projeto mais organizado e reutilizável.

---

# 💡 Principais Insights

## 🎧 Similaridade Musical

As recomendações apresentaram características bem próximas das músicas consultadas.

As variáveis que mais contribuíram para a formação dos grupos de músicas semelhantes foram --

* Danceability
* Energy
* Speechiness
* Valence
* Tempo

Mesmo que algumas features apresentem forte concentração em valores baixos (como `speechiness`, `instrumentalness` e `liveness`), elas ainda ajudam para diferenciar músicas específicas, então foram mantidas no modelo.

---

## 📈 PCA

A projeção em duas dimensões mostrou que as músicas recomendadas tendem a ocupar regiões próximas da música de referência.


---

## 🎼 Dataset

Durante a análise foi identificado que algumas músicas aparecem mais de uma vez na base de dados.

Em vários casos isso acontece pois --

* A música pertence a diferentes gêneros;
* A música aparece em álbuns diferentes;
* Existem versões diferentes cadastradas na plataforma.

Por isso, inclui o campo `album_name` nas recomendações.

---

# 🤖 Modelo Final

O sistema final --

* Content-Based Filtering
* StandardScaler
* Nearest Neighbors
* Distância Euclidiana
* Priorização por gênero musical
* Arquitetura modular para o mecanismo de recomendação

---

# 💡 Conclusões

Com base na análise, foi possível concluir que -- 

* características musicais são suficientes para gerar recomendações coerentes;
* o algoritmo Nearest Neighbors apresentou bons resultados para este problema;
* o escalonamento dos dados foi essencial para o cálculo correto das distâncias;
* PCA foi uma ferramenta útil para visualizar os agrupamentos formados pelo modelo;
* priorizar músicas do mesmo gênero melhorou a experiência das recomendações sem alterar o algoritmo de Machine Learning;
* a modularização fez com que o projeto ficasse mais organizado e reutilizável.
