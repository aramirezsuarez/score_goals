import streamlit as st

def login(username, password):
    # Agrega aquí tu lógica de autenticación (por ejemplo, puedes usar variables de entorno para almacenar usuarios y contraseñas)
    # Aquí se asume que "testuser" es el usuario y "testpassword" es la contraseña
    return username == "testuser" and password == "testpassword"

def main():
    st.set_page_config(page_title="App con Inicio de Sesión", page_icon=":unlock:")
    st.sidebar.title("Navegación")

    # Verificar si el usuario ha iniciado sesión
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None

    pages = {"Inicio de Sesión": login_page, "Perfil de Usuario": user_profile}
    selection = st.sidebar.radio("Ir a", list(pages.keys()))

    # Renderizar la página seleccionada
    pages[selection]()

def login_page():
    st.title("Iniciar Sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        if login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Inicio de sesión exitoso.")
        else:
            st.error("Nombre de usuario o contraseña incorrectos.")

def user_profile():
    st.title("Perfil de Usuario")

    if st.session_state.logged_in:
        st.write(f"Bienvenido, {st.session_state.username}!")
        # Puedes agregar contenido adicional de perfil aquí
    else:
        st.error("Debes iniciar sesión para ver esta página.")

if __name__ == "__main__":
    main()
