#importa streamlit
import streamlit as st


#configura pestaña
st.set_page_config(
    page_title= "La polémica",
    page_icon=":video_camera:"
    )

#titulo pestaña
st.title("LA POLÉMICA: :rotating_light:")

#subtitulo
st.header("**El fatidico día que murió...**", divider= True)

#tipo etiqueta
st.badge("ALERTA SPOILER", color="orange", icon=":material/done_outline:")


#columna
col1, col2, col3 = st.columns(3)


#texto
col1.write(" ")
col1.write("Este despreciable ser, que ha fingido su muerte hace dos semanas para promocionar su película más reciente  _AVENTURAS CON SAM_ .")

#imagen
col3.image("ChatGPT Image 8 sept 2025, 14_44_19.png", caption= 'Imagen referencial de la verdadera naturaleza de Sam')


#texto
col1.write(" ")
col1.write("Las malvadas intenciones de este diablillo eran conseguir fondos para su pobre y miserable vida llena de lujos y mansiones en etiopía. :scream_cat:")
col2.write("""
Todo ocurrió un jueves de hace dos semanas, en el último día de rodaje. Sam se encontraba filmando la escena en donde su perro Maxi, muere a manos de un niño con un arma.
La farsa se dió cuando el niño _(desconocido hasta el momento)_ va a disparar con la supuesta arma de utileria hacia el cachorro. El montaje de esta situación nos dió a entender que al disparar accidentalmente un arma cargada hacia el cachorro, el pequeño Sam **salvó** a Maxi, sacrificando su vida en el proceso.
""")
col1.write("Su _desinteresado e impecable acto de **buena fé**_ logró recaudar más de **100000** millones a **supuesto** beneficio de organizaciones para salvar mascotas")
st.write("Ahora todos sabemos que ese dinero finalmente se lo quedó Sam... :face_with_head_bandage:")


#video
st.video("a0bbe74f-3182-4cf7-b1c7-382640c1fdfa.mp4")

