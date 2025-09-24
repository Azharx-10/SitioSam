
# importa streamlit
import streamlit as st

#configuración pestaña
st.set_page_config(
    page_title="Su origen",
    page_icon=":video_camera:"
    )


#titulo pestaña
st.title("La verdadera historia de Sam")

#subtitulo
st.badge("Este es un sitio Web", color="yellow", icon=":material/done_outline:")

#texto
st.write("INFORMACIÓN MUY IMPORTANTE")
st.write("TODO SOBRE LA MASIVA FUNA HACIA **SAM**, MÁS CONOCIDO COMO PEQUEÑO O LITTLE SAM")
st.write("_(:scream_cat:)_")


#audio
st.audio("ytmp3free.cc_musica-de-fondo-para-noticiero-urgente-cortina-musical-de-noticias-youtubemp3free.org.mp3")


#subtitulo
st.header("Los primeros pasos de Sam", divider=True)

#columna
col1, col3 = st.columns(2)


#texto
col1.write("Su primera palabra fue _PEQUEÑO_ y la segunda fue **SAM.**")
col1.write("**LO MÁS SORPRENDENTE ES...**")
col1.write("Su _**TERCERA**_ palabra fue _100_. Esto tiene relevancia ya que el tres es la mitad de 6, y 6 es el número del diablo... ¿coincidencia? no lo creo.")
col1.write("Todo esto anterior sumado a que 100 tiene un significado tan pero que tan negativo, que ni con fines informativos puedo comentarlo")
col1.write("_**Yo también me impresioné muuuchooo.**_")
col3.write("Es conocido por ser el anticristo, pero nadie sabe que realmente es el elegido de Jesús")



#video
col3.video("videoplayback (1).mp4")


#texto
col3.write("...¿O no?")


#imagen
col3.image("Captura de pantalla 2025-08-04 155837.png", caption="No le creas nada.")



#texto
col1.write("_Algunos de sus aportes:_ ", divider= True)

col1.write("Little Sam desde su nacimiento ha hecho muchos aportes para la humanidad entera;")
col1.write("Desde la invención del capitalismo hasta la abolición de la esclavitud en la casa de la monse, (donde tenían decenas de colombianos trabajando días enteros solo por un trocito de pan)")

col1.write("El pequeño Sam ha sido figura de salvador desde su salto a la fama en 2003 cuando aseguró ser el anticristo en su video más reconocido para su canal de youtube, en donde acabó descubriendo gracias a un sacerdote  que realmente era el elegido del señor")
st.write("Lo que ninguno de nosotros sabía era que realmente el le había pagado a sacerdote para _chantajear_ a la población para que nadie se enterara que realmente es un demonio... Ahora todos lo sabemos")




