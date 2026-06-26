import pandas as pd

def recommend_by_index(indice,
                    df_modelagem_escalado,
                    modelo_NN,
                    df_spotify):
    
    musica = df_modelagem_escalado[indice]
    
    genero_musical = df_spotify.iloc[indice]["track_genre"]
    
    musica = musica.reshape(1,-1)
    
    distancias, vizinhos = modelo_NN.kneighbors(musica)
    
    df_recommendation_music = df_spotify.iloc[vizinhos[0]][["track_name", "artists", "album_name", "track_genre"]]

    condicao_genero = df_recommendation_music["track_genre"].str.lower() == genero_musical.lower()
    
    mesmo_genero = df_recommendation_music[condicao_genero]
    outros_generos = df_recommendation_music[~condicao_genero]

    resultado = pd.concat([mesmo_genero, outros_generos])

    
    return resultado