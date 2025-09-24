#importar streamlit
import streamlit as st


#configuración pagina
st.set_page_config(
    page_title="Aventuras con Sam",
    page_icon=":video_camera:"
    )

#titulo
st.title("LA DESGRACIADA PELICULA:video_camera::")



#subtitulo
st.header("**RESEÑA...**", divider= True)

#texto
st.write("Este despreciable ser, que ha fingido su muerte hace dos semanas para promocionar su película más reciente _AVENTURAS CON SAM_ .")

#n° columnas
col1, col2, col3 = st.columns(3)

#imagenes
col3.image("ChatGPT Image 4 sept 2025, 15_57_50.png")

#texto
st.write("""
“Aventuras con Sam” prometía ser un viaje divertido y emocionante por Perú junto al inseparable perro del protagonista, pero lamentablemente se queda corta en casi todos los aspectos. La trama es dispersa y poco coherente, con situaciones que parecen improvisadas más que planificadas, y los intentos de humor resultan forzados o simplemente aburridos.

El desarrollo de los personajes es mínimo: Sam parece una versión exagerada de sí mismo sin profundidad alguna, y el perro, aunque entrañable, se convierte en una mera herramienta para momentos emocionales que buscan manipular al espectador de manera barata. El clímax de la película, donde el perro es disparado, resulta chocante y gratuito, más un recurso impactante que un desenlace que tenga sentido dentro de la historia.

Visualmente, aunque hay algunos paisajes de Perú interesantes, la cinematografía no logra rescatar la película del caos narrativo. En resumen, “Aventuras con Sam” es una experiencia frustrante: una idea con potencial que se desploma por mala ejecución, personajes planos y un final innecesariamente traumático.
""")

#imagenes
col1.image("niñosamperro.png")
col2.image("Captura de pantalla 2025-08-04 155837.png")