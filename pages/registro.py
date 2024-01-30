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
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

@st.cache_data(ttl=600)
def get_data():
    db = client.mydb
    items = db.usuarios.insert_one({"name"="cbum"})

def main():
    st.title("Ejemplo con botón y @st.cache_data")

    if st.button("Ejecutar get_data()"):
        result = get_data()
        st.write(f"Función ejecutada. Resultado: {result}")

if __name__ == "__main__":
    main()

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
