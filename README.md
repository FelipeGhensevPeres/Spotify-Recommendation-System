# 🎵 Spotify Recommendation System

Projeto de Machine Learning para recomendação de músicas utilizando características musicais extraídas do Spotify.

O objetivo foi desenvolver um sistema que identifica músicas semelhantes a uma faixa de referência utilizando técnicas de recomendação baseada em conteúdo (*Content-Based Filtering*).

---

# 🎯 Problema de Negócio

Plataformas de streaming musical utilizam sistemas de recomendação para aumentar o engajamento dos usuários e facilitar a descoberta de novas músicas.

Nesse projeto, busquei responder algumas perguntas -

* É possível recomendar músicas semelhantes usando apenas características musicais?
* Quais atributos melhor representam a similaridade entre faixas?
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

Realizei uma análise inicial do dataset para entender a estrutura.

Principais verificações -

* Quantidade de registros e atributos
* Valores nulos
* Valores duplicados
* Distribuição das variáveis
* Características dos gêneros musicais

Também construí histogramas para ver o comportamento das principais features utilizadas pelo modelo.

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
* Padronização dos dados utilizando StandardScaler

O escalonamento foi necessário porque algumas variáveis possuem escalas muito diferentes, o que poderia impactar o cálculo das distâncias entre músicas.

---

## 🔹 Construção do Modelo

O algoritmo escolhido foi -

### Nearest Neighbors (KNN)

O modelo calcula a distância entre músicas utilizando suas características musicais.

Músicas com menor distância são consideradas mais semelhantes.

Configuração utilizada:

```python
NearestNeighbors(
    n_neighbors=6,
    metric="euclidean"
)
```

A distância Euclidiana foi uma métrica principal para medir a similaridade entre as faixas.

---

# 📊 Visualização com PCA

Como cada música é representada por 9 características musicais, apliquei a técnica PCA (*Principal Component Analysis*) para reduzir os dados para duas dimensões.

Isso facilitou visualizar - 

* A distribuição geral das músicas
* A posição da música consultada
* A proximidade das recomendações geradas

As duas componentes principais preservaram aproximadamente 48% da variabilidade original dos dados.

---

# 🔍 Sistema de Recomendação

Desenvolvi uma função para consultar o modelo treinado:

```python
recommendation_song(song_name, artist="")
```

A função permite - 

* Buscar músicas semelhantes pelo nome
* Filtrar por artista quando necessário
* Retornar recomendações com - 

  * Nome da música
  * Artista
  * Álbum
  * Gênero musical

Exemplo:

```python
recommendation_song("Believer")
```

---

# 💡 Principais Insights

## 🎧 Similaridade Musical

As recomendações geradas apresentaram características bem próximas das músicas consultadas.

As variáveis que mais contribuíram para a formação dos grupos de músicas semelhantes foram:

* Danceability
* Energy
* Speechiness
* Valence
* Tempo

---

## 📈 PCA

A projeção em duas dimensões mostrou que as músicas recomendadas tendem a ocupar regiões próximas da música de referência.

Isso reforça que o algoritmo está encontrando vizinhos coerentes dentro do espaço de características musicais.

---

## 🎼 Dataset

Durante a análise foi identificado que algumas músicas aparecem mais de uma vez na base de dados.

Em vários casos isso ocorre porque -

* A música pertence a diferentes gêneros
* A música aparece em álbuns diferentes
* Existem versões diferentes cadastradas na plataforma

Por esse motivo, o campo `album_name` foi incluído nos resultados das recomendações.

---

# 🤖 Modelo Final

O sistema final utiliza - 

* Content-Based Filtering
* StandardScaler
* Nearest Neighbors
* Distância Euclidiana

A solução permite recomendar músicas semelhantes com base em suas características sonoras.

---

# 💡 Conclusões

Com base na análise, foi possível concluir que -

* Características musicais são suficientes para gerar recomendações coerentes
* O algoritmo Nearest Neighbors apresentou bons resultados para este problema
* O escalonamento dos dados foi importantíssimo para o cálculo correto das distâncias
* PCA foi uma ferramenta útil para visualizar os agrupamentos formados pelo modelo
* O sistema consegue recomendar músicas semelhantes sem depender de avaliações ou histórico de usuários
