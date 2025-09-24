#importar streamlit
import streamlit as st

#configuracion pestaña
st.set_page_config(
    page_title="Noticias similares",
    page_icon=":video_camera:"
    )


#titulo
st.title("MÁS POLÉMICA :woman_technologist::")

#subtitulo
st.header("_El caso Monserratt:_", divider= True)

#"etiqueta" de la pestaña
st.badge("Información", color="orange")


#columna
col1, col3 = st.columns(2)


#subtitulo
col1.header(" :rotating_light::rotating_light::rotating_light:", divider= True)

#texto
col1.write("En relación al caso Miyuzzet, tenemos sus **testimonios** sobre los colombianos rescatados de su propiedad:")
col3.write(" ")
col3.write(" ")
col3.write(" ")
col3.write(" ")
col3.write(" ")
col3.write("_Entonces ¿que tienes para decir sobre tu polémica?_")
col3.write("_-No diré nada más que recalcar que me quitaron a mis colombianitos!!!!_")
col3.write("_-Efectivamente esta mujer no tiene sentido común_")

#video
col1.video("envato_video_gen_Sep_22_2025_18_32_19.mp4")

#texto
col1.write("_explicación grafica de como Miyuzzet se enfurecía y mostraba su doble cara :scream_cat:_ ")

#audio
col3.audio("luvvoice.com-20250922-lYs1zn.mp3")


#texto
col3.write("audio extraído de una entrevista realizada por ***MEGA100*** a Miyuzzett, si quieres verla puedes hacerlo en las redes sociales de la plataforma.")