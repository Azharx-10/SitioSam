# Importar streamlit
import streamlit as st

# Configuración de Logo
st.logo(
    "Captura de pantalla 2023-09-02 141341.png",
)
# Configurar la pagina
st.set_page_config(
    page_title="_.Azharx._",
    page_icon=":video_camera:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)


#barra de navegación

pg = st.navigation(["HomePage.py","La_verdadera_historia_de_Little_Sam.py", "La_polémica.py", "Cómo_fue_descubierto.py", "La_pelicula.py", "Otras_noticias.py", "Información_autor.py"])
pg.run()