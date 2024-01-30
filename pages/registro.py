# Importar librerias necesarias
import streamlit as st
import streamlit_extras
import streamlit_authenticator as stauth
import re
import pymongo
from datetime import datetime

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


st.title("registro")

# Si se aceptan los términos y condiciones habilitar el registro
aceptar_terminos = st.checkbox("Acepto los términos y condiciones")

if aceptar_terminos:
    # Creacion del formulario
    with st.form(key="registro", clear_on_submit=True):
        # Titulo del formulario
        st.subheader("Registrarse")

        # Campos a ser llenados por el usuario
        email = st.text_input("Email", placeholder="Ingrese su Email")
        username = st.text_input("Usuario", placeholder="Ingrese su nombre de usuario")
        password = st.text_input("Contraseña", placeholder="Ingrese su contraseña", type="password")



        # Boton de envio de datos de registro
        st.form_submit_button("Registrate")

    # Revisar validez de los datos ingresados por el usuario y registro a la DB
    if email and username and password:
        if validar_email(email):
            if email not in get_emails_usuarios():
                if validar_username(username):
                    if username not in get_usernames_usuarios():
                        password_encriptada = stauth.Hasher([password]).generate()
                        insertar_usuario(email, username, password_encriptada[0])
                        st.success("Cuenta creada con éxito!")
                    else:
                        st.warning("Nombre de usuario en uso")
                else:
                    st.warning("Nombre de usuario inválido (solo debe tener letras y números)")
            else:
                st.warning("El email ya está en uso")
        else:
            st.warning("Email inválido")
    else:
        st.warning("Debe rellenar todos los campos")
else:
    st.warning("Debes aceptar los términos y condiciones antes de poder registrarte")



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
