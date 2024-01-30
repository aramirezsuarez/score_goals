

import streamlit as st
#from SessionState import get
# Función de inicio de sesión
def login(username, password):
    return username == "testuser" and password == "testpassword"

# Verificar el estado de la sesión
def check_session_state():
    session_state = get(username="", logged_in=False)
    return session_state

# Página de inicio de sesión
def login_page():
    st.title("Iniciar Sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        if login(username, password):
            session_state = get(username=username, logged_in=True)
            st.success("Inicio de sesión exitoso.")
            st.experimental_rerun()
        else:
            st.error("Nombre de usuario o contraseña incorrectos.")

# Página del perfil de usuario
def user_profile():
    st.title("Perfil de Usuario")
    session_state = check_session_state()

    if session_state.logged_in:
        st.write(f"Bienvenido, {session_state.username}!")
        # Puedes agregar contenido adicional de perfil aquí
    else:
        st.error("Debes iniciar sesión para ver esta página.")

# Página principal
def main():
    st.set_page_config(page_title="App con Inicio de Sesión", page_icon=":unlock:")
    st.sidebar.title("Navegación")
    pages = {"Inicio de Sesión": login_page, "Perfil de Usuario": user_profile}
    selection = st.sidebar.radio("Ir a", list(pages.keys()))

    pages[selection]()

if __name__ == "__main__":
    main()
