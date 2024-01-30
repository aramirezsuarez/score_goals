import streamlit as st
import random

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
st.markdown(footer, unsafe_allow_html=True)

# Lista de equipos que participaron en el Mundial 2022
equipos = [
    "Qatar", "Alemania", "Dinamarca", "Brasil", "Bélgica", "Francia",
    "Croacia", "España", "Serbia", "Inglaterra", "Suiza", "Países Bajos",
    "Argentina", "Irán", "Corea del Sur", "Japón", "Arabia Saudita", "Uruguay",
    "Ecuador", "Canadá", "Ghana", "Senegal", "Portugal", "Polonia", "Túnez",
    "Marruecos", "Camerún", "Estados Unidos", "México", "Gales",
    "Australia", "Costa Rica"
]

# Definir las fases del torneo
fases = ["Octavos de final", "Cuartos de final", "Semifinales", "Final"]

# Función para calcular resultados
def calcular_resultados():
    """
    Simula los resultados de un torneo de eliminación directa,
    mostrando los enfrentamientos y ganadores en cada fase.

    Returns:
        str: El nombre del equipo ganador del torneo.
    """
    ganador = None
    equipos_fase_actual = equipos.copy()

    for i, fase in enumerate(fases):
        num_partidos = 2 ** (len(fases) - i - 1)
        st.write(f"\n{fase} ({num_partidos} partidos):")
        equipos_ganadores = []

        for _ in range(num_partidos):
            equipo1 = random.choice(equipos_fase_actual)
            equipos_fase_actual.remove(equipo1)
            equipo2 = random.choice(equipos_fase_actual)
            equipos_fase_actual.remove(equipo2)
            ganador = random.choice([equipo1, equipo2])
            equipos_ganadores.append(ganador)
            st.write(f"{equipo1} vs {equipo2} => Ganador: {ganador}")

        equipos_fase_actual = equipos_ganadores.copy()

    return equipos_fase_actual[0]

# Crear la aplicación de Streamlit
st.title("Score Goals")
st.header("Simulación del Mundial 2022")

# Botón para calcular nuevos resultados
if st.button("Calcular Resultados"):
    ganador = calcular_resultados()

    # Anunciar al ganador del Mundial
    st.subheader("Ganador del Mundial 2022")
    st.success(f"¡{ganador} es el ganador del Mundial 2022!")
