# Importar librerias necesarias
import streamlit as st
import streamlit_extras
import streamlit_authenticator as stauth
import re
import pymongo

# Initialize connection.
# Uses st.cache_resource to only run once.

@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://aramirezsu:Cbum2024@cluster0.gowlzlh.mongodb.net/?retryWrites=true&w=majority")

client = init_connection()

db = client.scoregoals


@st.cache_data(ttl=600)
def insertar_usuario(email, username, password):
    # Agregar un nuevo usuario a la Base de Datos con la
    # información proporcionada
    db.users.insert_one({"key": email, "username": username, "password": password,
            "jugadores": []})

# Formulario para ingresar la información del usuario
email = st.text_input("Correo Electrónico")
username = st.text_input("Nombre de Usuario")
password = st.text_input("Contraseña", type="password")

# Botón para ejecutar la función
if st.button("Insertar Usuario"):
    insertar_usuario(email, username, password)
    st.success("Usuario insertado correctamente en la base de datos.")


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
st.title("Registro")
