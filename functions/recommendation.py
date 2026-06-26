def recommend_by_index(indice,
                    df_modelagem_escalado,
                    modelo_NN,
                    df_spotify):
    musica = df_modelagem_escalado[indice]
    musica = musica.reshape(1,-1)
    distancias, indices = modelo_NN.kneighbors(musica)
    
    df_recommendation_music = df_spotify.iloc[indices[0]][["track_name", "artists", "album_name", "track_genre"]]
    
    return df_recommendation_music