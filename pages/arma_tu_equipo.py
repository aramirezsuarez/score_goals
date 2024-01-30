# Importar librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests

# URL de datasets
url_players = ("https://raw.githubusercontent.com/aramirezsuarez"
              "/Score_Goals/main/datasets/players.csv")

# Cargar el DataFrame desde la URL
df_players = pd.read_csv(url_players)

# Verifica si el usuario inició sesión
if st.session_state["authentication_status"]:
    
    # Crear un diccionario con la cantidad deseada de jugadores por posición
    posiciones_deseadas = {"Goalkeeper": 1, "Defender": 4, "Midfield": 4, "Attack": 3}

    # Inicializar un diccionario para mantener un recuento de jugadores seleccionados por posición
    jugadores_seleccionados_por_posicion = {posicion: 0 for posicion in posiciones_deseadas}

    # Crear widgets de selección dinámicamente
    for posicion, cantidad_deseada in posiciones_deseadas.items():
        jugadores_seleccionados = st.multiselect(
            f"Selecciona los {posicion.lower()}",
            df_players[df_players["position"] == posicion]["name"],
            key=f"{posicion.lower()}_key"
        )

        # Filtrar el DataFrame para obtener las filas correspondientes a los jugadores seleccionados
        df_filtrado = df_players[df_players["name"].isin(jugadores_seleccionados)]

        # Contar el número de jugadores seleccionados por posición
        jugadores_posicion = df_filtrado[df_filtrado["position"] == posicion]
        jugadores_seleccionados_posicion = min(len(jugadores_posicion), cantidad_deseada)
        jugadores_seleccionados_por_posicion[posicion] = jugadores_seleccionados_posicion

    # Mostrar el resultado
    st.write("Jugadores seleccionados por posición:")
    st.write(jugadores_seleccionados_por_posicion)

else:
    st.warning("Si deseas acceder a esta función iniciar sesion")

