import pandas as pd

def recommend_by_index(indice,
                    df_modelagem_escalado,
                    modelo_NN,
                    df_spotify,
                    qtd_musicas_buscar=6):
    
    if qtd_musicas_buscar < 1:
        raise ValueError
    
    musica = df_modelagem_escalado[indice]
    
    genero_musical = df_spotify.iloc[indice]["track_genre"]
    
    musica = musica.reshape(1,-1)
    
    distancias, vizinhos = modelo_NN.kneighbors(musica,n_neighbors=qtd_musicas_buscar)
    
    df_recommendation_music = df_spotify.iloc[vizinhos[0]][["track_name", "artists", "album_name", "track_genre"]]

    condicao_genero = df_recommendation_music["track_genre"].str.lower() == genero_musical.lower()
    
    # Prioriza recomendações do mesmo genero musical.
    # Caso não exista recomendações suficientes, musicas de outros generos.
    # Também são mantidas para não reduzir a quantidade de resultados.
    mesmo_genero = df_recommendation_music[condicao_genero]
    outros_generos = df_recommendation_music[~condicao_genero]

    resultado = pd.concat([mesmo_genero, outros_generos])

    
    return resultado