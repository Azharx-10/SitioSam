#importar streamlit
import streamlit as st

#configura la pestaña
st.set_page_config(
    page_title="La mentira",
    page_icon=":video_camera:"
    )

#titulo pestaña
st.title("LA POLÉMICA: :rotating_light:")

#texto
st.write("_audio de musica relajante para evitar muertes causadas por la sorpresa de descubrir que Sam es malvado :scream_cat:_")

#audio
st.audio("5 Minutos Música Relajante Para Meditar. Conecta tu cuerpo y mente, encuentra paz interior, 001.mp3")

#subtitulo
st.header("**El fatidico día que murió...**", divider= True)

#título y división
st.badge("ALERTA SPOILER", color="orange", icon=":material/done_outline:")

#columnas
col1, col3 = st.columns(2)

#subtítulo y otra división
col1.header("Cómo se descubrió la verdad:", divider= True)

#texto
col1.write(" Little Sam se encontraba _**MUY**_ oculto en una isla desierta del norte de Perú, disfrutando de su nueva fama cuando un programa de televisión, comandado por _Monsolaf_ llegó a la isla en busca de material para un filme sobra la (hasta ese entonces) reconocida ilustre vida de Sam")
col1.write(" Cuando el reconocido programa _Ilustres y famosos_ arrivó a la isla para filmar sobre los inicios humildes de Sam recolectando cocos para sobrevivir, vieron a lo lejos un hotel de lujo y al acercarse, se dieron cuenta que realmente era la casa de alguien... Enterándose así que Sam había construido en aquella isla **¡Y NO SOLO ESO!**, tambíen descubrieron a Sam en un estado muy ebrio, bebiendo mojitos con una camiseta que decía _ODIO A LOS PERRITOS_ :scream_cat:")

col3.write(" ")
col3.write(" ")
col3.write(" ")
col3.write(" ")
col3.write(" ")


#subtitulo
col3.header("Evidencia :scream_cat:", divider= True)

#texto
col3.write(" ")

#audio
col3.audio("fakeyou_srnqdf22yyq2pyvn1y6vwmm4dygnw391.wav")

#texto
col3.write("""
**_transcripción del audio:_**
_Aquí nos encontramos en una isla desierta..._  
_el lugar donde Sam dio sus primeros pasos_

_y grabó aquellos videos que lo llevaron a la fama..._

_Espera... ¿qué es eso?..._
_¡OOOH, SAM!_ 
_¡Pero tú... tú estabas muerto!_
""")

col3.write("**Gentileza del programa _Ilustres y famosos_**")


#imagen
col3.image("envato-labs-image-edit.png", caption= "Imagen extraída desde el programa")