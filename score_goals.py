
# Importar librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests

# Funcion para cargar las animaciones
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#URL de datasets
url_players = ("https://raw.githubusercontent.com/aramirezsuarez"
              "/Score_Goals/main/datasets/players.csv")
url_games = ("https://raw.githubusercontent.com/aramirezsuarez/"
            "Score_Goals/main/datasets/games.csv")
url_clubs = ("https://raw.githubusercontent.com/aramirezsuarez/"
              "Score_Goals/main/datasets/clubs.csv")

# Cargar el DataFrame desde la URL
df_players = pd.read_csv(url_players)
df_games = pd.read_csv(url_games)
df_clubs = pd.read_csv(url_clubs)

# Crear pie de pagina con los datos de contacto de los creadores
footer = """
<style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        z-index: 10;
        width: 100%;
        background-color: rgb(14, 17, 23);
        color: black;
        text-align: center;
    }
    .footer p {
        color: white;
    }
</style>
<div class="footer">
    <p>App desarrollada por: <br />
    Andres Felipe Ramirez Suarez <br />
    Contactenos: <a href="#">aramirezsu@unal.edu.co</a>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# Título de la aplicación
st.title("Score Goals")
# URL de animacion #1
lottie_chilena= load_lottieurl("https://raw.githubusercontent.com/aramirez"
         "suarez/Score_Goals/main/animaciones/animacion_pagina_principal.json")

# Mostrar animacion #1
st_lottie(lottie_chilena, height = 180, key="chilena")

# Sección de Información de Partidos
st.header("Información de Partidos")
st.write("### Lista de Juegos disputados:")
st.write(df_games)

# Crear una lista única de equipos combinando,
# las columnas "home_club_name" y "away_club_name"
equipos_disponibles = list(set(df_games["home_club_name"])
                              .union(df_games["away_club_name"]))

# Permitir al usuario seleccionar dos equipos
team_select = st.multiselect("Selecciona los equiposque quieras consultar",
                                       equipos_disponibles, default=[])

# Verificar si se seleccionaron exactamente dos equipos
if len(team_select) == 2:
    equipo_local, equipo_visitante = team_select

    # Filtrar el DataFrame para los partidos donde se enfrentaron,
    # los dos equipos seleccionados
    df_filtrado = df_games[
        ((df_games["home_club_name"] == equipo_local) &
         (df_games["away_club_name"] == equipo_visitante)) |
        ((df_games["home_club_name"] == equipo_visitante) &
         (df_games["away_club_name"] == equipo_local))
    ]

    # Mostrar la información de los partidos seleccionados
    st.write(f"Partidos entre {equipo_local} y {equipo_visitante}:")
    st.write(df_filtrado)

else:
    st.warning("Por favor, selecciona exactamente dos equipos.")

# Sección de Información de Jugadores
st.header("Información de Jugadores")
st.write("### Lista de Jugadores:")
st.write(df_players)

# URL de animacion #2
lottie_player= load_lottieurl("https://raw.githubusercontent.com/aramirez"
           "suarez/Score_Goals/main/animaciones/animacion_pagina_players.json")

# Mostrar animacion #2
st_lottie(lottie_player, height = 180, key="player")

jugador_seleccionados = st.multiselect(
    "Selecciona el/los jugadores que quieras consultar",
    df_players["name"]
)

# Filtrar el DataFrame para obtener las filas,
# correspondientes a los jugadores seleccionados
df_filtrado = df_players[df_players["name"].isin(jugador_seleccionados)]

# Verificar si se seleccionaron jugadores
if not df_filtrado.empty:
    st.write("### Informacion jugador/jugadores Seleccionados:")
    st.dataframe(df_filtrado)
    # Crear un gráfico de barras para mostrar los valores más altos de mercado
    plt.figure(figsize=(10, 6))
    plt.bar(df_filtrado["name"], df_filtrado["highest_market_value_in_eur"])
    plt.xlabel("Jugadores")
    plt.ylabel("Valor de mercado más alto (en Millones de EUR)")
    plt.title("Valores de mercado más altos de jugadores seleccionados")
    plt.xticks(rotation=45)

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt.gcf())
else:
    st.warning("Selecciona al menos un jugador para graficar")

# Sección de Información de Clubes
st.write("### Lista de clubs:")
st.write(df_clubs)

club_seleccionados = st.multiselect(
    "Selecciona el/los clubs que quieras consultar",
    df_clubs["name"]
)

# Filtrar el DataFrame para obtener solo los clubes seleccionados
selected_clubs_info = df_clubs[df_clubs["name"].isin(club_seleccionados)]

# Mostrar la información en una tabla
st.write("Información de los clubes seleccionados:")
st.write(selected_clubs_info)
