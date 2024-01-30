# Importar librerias necesarias
import streamlit as st
import streamlit_extras
import streamlit_authenticator as stauth
import re
import pymongo
from datetime import datetime

@st.cache_resource
def init_connection():
    """
    Establece y retorna una conexión a la base de datos MongoDB.

    Returns:
    pymongo.MongoClient: Cliente de MongoDB conectado al servidor especificado.
    """
    return pymongo.MongoClient(
        "mongodb+srv://aramirezsu:"  
        "Cbum2024@cluster0.gowlzlh.mongodb.net/"  
        "?retryWrites=true&w=majority" 
    )

# Se inicializa la conexión a la base de datos 
# llamando a la función init_connection().
client = init_connection()

# Se accede a la base de datos "scoregoals" a través del cliente de MongoDB.
db = client.scoregoals

@st.cache_data(ttl=600)
def insertar_usuario(email, username, password):
    """
    Inserta un nuevo usuario en la base de datos.

    Args:
    email (str): Correo electrónico único del usuario.
    username (str): Nombre de usuario del usuario.
    password (str): Contraseña del usuario.

    Returns:
    None

    Raises:
    pymongo.errors.WriteError: Si hay un error al insertar 
    el usuario en la base de datos.
    """
    db.users.insert_one({
        "key": email,        #
        "username": username,  
        "password": password,  
        "jugadores": []       
    })

# Funcion que retorna los emails de los usuarios registrados
def get_emails_usuarios():
    """
    Obtiene una lista con los correos electrónicos de cada usuario
    registrado en la Base de Datos.

    Returns:
    - list: Una lista que contiene los correos electrónicos de cada usuario.
    """
    # Guardar los datos de la Base de Datos en 'users'
    users = db.users.find({}, {"key": 1})
    
    # Inicializar una lista para almacenar los correos electrónicos
    emails = []

    # Filtrar los correos electrónicos del diccionario de usuarios y
    # agregarlos a la lista
    for user in users:
        emails.append(user["key"])

    return emails

# Funcion que retorna los nombres de usuario de los usuarios registrados
def get_usernames_usuarios():
    """
    Obtiene una lista con los nombres de usuario de cada usuario
    registrado en la Base de Datos.

    Returns:
    - list: Una lista que contiene los nombres de usuario de cada usuario.

    """
    # Guardar los datos de la Base de Datos en 'users'
    users = db.users.find({}, {"username": 1})

    # Inicializar una lista para almacenar los nombres de usuario
    usernames = []

    # Filtrar los nombres de usuario del diccionario de usuarios y
    # agregarlos a la lista
    for user in users:
        usernames.append(user["username"])

    return usernames

# Funcion que verifica si un email ingresado es valido
def validar_email(email):
    """
    Verifica si el email ingresado es válido según patrones típicos.

    Args:
    - email (str): La dirección de correo electrónico a validar.

    Returns:
    - bool: True si el email es válido, False de lo contrario.

    """
    # Patrones típicos de un email válido
    pattern = "^[a-zA-Z0_9-]+@[a-zA-Z0-9-]+\.[a-z]{1,3}$"
    pattern1 = "^[a-zA-Z0-9-]+@[a-zA-Z0-9-]+\.[a-z]{1,3}+\.[a-z]{1,3}$"

    # Verifica si el email ingresado coincide con alguno de los
    # patrones definidos
    if re.match(pattern, email) or re.match(pattern1, email):
        return True
    return False

def validar_username(username):
    """
    Verifica si el username ingresado es válido según un patrón típico.

    Args:
    - username (str): El nombre de usuario a validar.

    Returns:
    - bool: True si el username es válido, False de lo contrario.

    """
    # Utiliza directamente el resultado de re.match,
    # que es None si no hay coincidencia
    return bool(re.match("^[a-zA-Z0-9]*$", username))

# Titulo de la pagina
st.title("Registro")
# Se define un checkbox en el que se deben aceptar los
# T&C antes de enviar un registro
st.write("Debe aceptar los términos y condiciones antes de"
         "poder enviar el formulario")
aceptar_terminos = st.checkbox(
    "Acepto los [Términos y Condiciones]"
    "(https://github.com/aramirezsuarez/"
    "score_goals/blob/main/Politica%20de%20Tratamiento%20de%20Datos.md)"
)



if aceptar_terminos:
    # Creacion del formulario
    with st.form(key="registro", clear_on_submit=True):
        # Titulo del formulario
        st.subheader("Registrarse")

        # Campos a ser llenados por el usuario
        email = st.text_input("Email", placeholder="Ingrese su Email")
        username = st.text_input("Usuario", 
                                 placeholder="Ingrese su nombre de usuario")
        password = st.text_input("Contraseña", 
                       placeholder="Ingrese su contraseña", type="password")

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
                    st.warning("Nombre de usuario inválido "
                    "(solo debe tener letras y números)")
            else:
                st.warning("El email ya está en uso")
        else:
            st.warning("Email inválido")
    else:
        st.warning("Debe rellenar todos los campos")
else:
    st.warning("Debes aceptar los términos y condiciones "
    "antes de poder registrarte")

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
