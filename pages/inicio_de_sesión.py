# Pagina de inicio de sesion
# Importar librerias necesarias
import streamlit as st
import streamlit_extras
import streamlit_authenticator as stauth
import re
import pymongo

@st.cache_resource
def init_connection():
    """
    Establece y retorna una conexión a la base de datos MongoDB.

    Returns:
    pymongo.MongoClient: Cliente de MongoDB conectado al servidor especificado.
    """
    return pymongo.MongoClient(
        "mongodb+srv://aramirezsu:Cbum2024@"
        "cluster0.gowlzlh.mongodb.net/?retryWrites=true&w=majority"
    )

# Se inicializa la conexión a la base de datos 
# llamando a la función init_connection().
client = init_connection()

# Se accede a la base de datos "scoregoals" a través del cliente de MongoDB.
db = client.scoregoals

def fetch_usuarios():
    """
   Recupera y devuelve un diccionario con los usuarios
   registrados en la Base de Datos.

   Returns:
   - dict: Un diccionario que contiene la información de los
   usuarios registrados.
   Cada clave es la dirección de correo electrónico única del usuario,
   y cada valor es un diccionario con detalles como
   "username", "age", "height", y "password".
   """
    # guardamos los datos de la DB en users y retornamos su contenido
    users = db.users.find()
    return users

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
   Retorna True si el email ingresado es válido, de lo contrario retorna False

   Parameters:
   - email (str): Dirección de correo electrónico a validar.

   Returns:
   - bool: True si el email es válido, False si no lo es.
   """
    # Patrones tipicos de un email valido
    pattern = "^[a-zA-Z0_9-_]+@[a-zA-Z0_9-_]+\.[a-z]{1,3}$"
    pattern1 = "^[a-zA-Z0_9-_]+@[a-zA-Z0_9-_]+\.[a-z]{1,3}+\.[a-z]{1,3}$"

    # Verifica si el email ingresado coincide con algun patron definido
    if re.match(pattern, email) or re.match(pattern1, email):
        return True
    return False

# Funcion que verifica si un username ingresado es valido
def validar_username(username):
    """
    Retorna True si el nombre de usuario ingresado es válido,
    de lo contrario, retorna False.

    Parameters:
    - username (str): Nombre de usuario a validar.

    Returns:
    - bool: True si el nombre de usuario es válido, False si no lo es.
    """
    # Se define el patron de un username tipico
    pattern = "^[a-zA-Z0-9]*$"
    # Se verifica si el username ingresado coincide con el patron tipico
    if re.match(pattern, username):
        return True
    return False

# Función para actualizar la contraseña y/o el nombre de usuario
def actualizar_datos_usuario(username, new_username, new_password):
    """
    Actualiza la contraseña y/o el nombre de usuario de un usuario registrado.

    Parameters:
    - username (str): Nombre de usuario actual del usuario.
    - new_username (str): Nuevo nombre de usuario (puede ser el mismo).
    - new_password (str): Nueva contraseña (puede ser la misma).

    Returns:
    - bool: True si la actualización fue exitosa, False si hubo un error.
    """
    users = collection.find()
    for user in users:
        if user["username"] == username:
            if new_username:
                collection.update_one({"_id": user["_id"]}, {"$set":
                                      {"username": new_username}})
            if new_password:
                new_encrypted_password = Hasher([new_password]).generate()
                collection.update_one({"_id": user["_id"]}, {"$set": 
                 {"password": new_encrypted_password[0]}})
            return True
    return False

 # Se almacenan los datos necesarios de la DB
users = fetch_usuarios()
emails = get_emails_usuarios()
usernames = get_usernames_usuarios()
passwords = [user["password"] for user in users]

# Se crea el diccionario credentials necesario para el
# funcionamiento del autenticador de cuentas
credentials = {"usernames": {}}
for index in range(len(emails)):
    credentials["usernames"][usernames[index]] = {
        "email":emails[index],
        "name": usernames[index],
        "password": passwords[index]
    }

# Creacion del autenticador
Authenticator = stauth.Authenticate(
    credentials, cookie_name="Streamlit", key="cookiekey", cookie_expiry_days=3
)

# La funcion login regresa una tupla con estos
# 3 valores los cuales atrapamos
email, authentication_status, username = Authenticator.login()

# Comprobacion de la existencia del username dentro de la DB
# y mensajes de advertencia en caso de un mal inicio de sesion
if username:
    if username in usernames:
        if authentication_status:
            st.write(f"Bienvenido {username}")
            # Creacion de boton de cerrar sesion en la barra lateral
            Authenticator.logout("Cerrar sesion", location="sidebar")

            # Creacion de seccion de administracion de cuenta donde
            # el usuario puede actualizar sus datos si lo desea
            st.subheader("Actualizar Datos")

            # Obtener el nombre de usuario del usuario autenticado
            username = st.session_state["username"]

            # Crear formulario
            with st.form(key="actualizar_datos"):
                # Campos para ingresar nueva contraseña y nombre de usuario
                new_password = st.text_input("Nueva Contraseña", type="password")
                new_username = st.text_input("Nuevo Nombre de Usuario")

                # Botón para enviar el formulario
                st.form_submit_button("Actualizar Datos")
            st.warning("Tenga en cuenta que al actualizar sus datos debe iniciar"
                    " sesion nuevamente")

            # Procesar la actualización si se proporcionaron nuevos datos
            if new_password or new_username:
                success = actualizar_datos_usuario(
                    username, new_username, new_password
                )
                if success:
                    st.success("Datos actualizados con éxito.")
                    Authenticator.cookie_manager.delete(
                        Authenticator.cookie_name
                    )
                    st.session_state['logout'] = True
                    st.session_state['name'] = None
                    st.session_state['username'] = None
                    st.session_state['authentication_status'] = None
                else:
                    st.warning("Error al actualizar datos. Inténtelo de nuevo.")

        elif not authentication_status:
            st.warning("Contraseña o nombre de usuario incorrectos")
        else:
            st.warning("Por favor ingrese todos los campos")
    else:
        st.warning("Nombre de usuario no existe, por favor regístrese")


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
