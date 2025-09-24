#importa streamlit
import streamlit as st

#configura la pestaña
st.set_page_config(
    page_title="_.Azharx._",
    page_icon=":video_camera:"
    )


#titulo pestaña
st.title("Azharx:slot_machine::")

#audio
st.audio("WhatsApp Audio 2025-09-23 at 18.46.55.mp4")

#texto
st.write("_audio de relleno_ :sunglasses:")

#subtitulo
st.header("**Sobre los autores:scream_cat::**", divider= True)

#columnas
col1, col3 = st.columns(2)

#imagen
col3.image("wDdfb1758667048.jpg", caption = "_Logo ***no oficial*** de MEGA100, pero el más amado por los fans_")

#escribir
col1.write("""
Para evitar cualquier inconveniente con los verdaderos autores debido a la naturaleza de la farándula expuesta, todos los colaboradores de este artículo serán nombrados bajo el seudónimo “Los Azharx” (y no, no es narcisismo, solo prevención:sunglasses:).
""")
col1.write("Este documento corresponde a un artículo publicado en Mega100, titulado “El Caso Sam”, dentro de nuestra sección de farándula y actualidad.")

#subtitulo
col1.header("Cómo citar: _(porque este artículo es tan increíble que merece una tesis):sunglasses:_", divider= True)

#texto
st.write("""Si deseas citar este trabajo, utiliza el siguiente formato sugerido:

Mega100 (2025). “El Caso Sam”. Los Azharx.
(Disponible en las redes sociales de la empresa :sunglasses:)

Para cualquier consulta, comentario o aclaración, puedes escribirnos a:
📧 contacto@mega100.com

📞 +1 (555) 234-9876
""")