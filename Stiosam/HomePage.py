#importar streamlit
import streamlit as st


#configuración pestaña
st.set_page_config(
    page_title="Azharx-MEGA100",
    page_icon=":video_camera:"
    )

#titulo de la página
st.title("Mega100:scream_cat:: _¿quienes somos ***REALMENTE***?_")
st.badge("Quienes somos :eyes:", color="red")




#titulo y división
st.header(":poop: Quienes somos :poop::", divider=True)

#cuantas columnas son y sus nombres
col1, col2 = st.columns(2)

#texto
st.write("En _**MEGA100**_ somos una página dedicada a informar sobre las figuras más despreciables del mundo de la farándula. ")

col1.write("""
En MEGA100 somos una página dedicada a exponer y analizar, con un tono satírico y sin filtros, a las figuras más despreciables y polémicas del mundo de la farándula.
Desde personajes como _Miyuzzett_, pasando por el _niño Sam_, hasta el cuestionable _***Daniel el más variado***_, aquí encontrarás la información farandulesca que otros no se atreven a contar.

Un espacio de humor, crítica y chismerío 100% farandulesco, donde la exageración, la sátira y la burla son nuestra marca registrada.
Porque en el show no todo es brillo… también hay ***mugre***, ¡y nosotros la sacamos a la luz!:scream_cat:
""")
col2.write(" ")
col2.write(" ")

col2.write(" ")

col2.write(" ")


#imagen
col2.image("elmasvariado.jpg", caption= "Imagenes reales de ***Daniel el Más Variado*** reconocido por ser el _ابزار خودکار برای بیماری‌های سرگردان_ más famoso de internet" )