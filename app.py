import streamlit as st
import streamlit.components.v1 as components

# Configurar la página en modo ancho y título
st.set_page_config(
    page_title="Nuestro álbum",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar márgenes y cabeceras de Streamlit para que parezca una web completa
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Leer tu archivo HTML (asegúrate de que el nombre coincida exactamente)
try:
    with open("Nuestro álbum.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # Mostrar la aplicación web
    components.html(html_code, height=900, scrolling=True)
except FileNotFoundError:
    st.error("No se encontró el archivo 'Nuestro álbum.html'. Verifica el nombre en la carpeta.")