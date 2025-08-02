
import streamlit as st

def modulo_epigenetico():
    st.header("Módulo 2: Estado Epigenético Emocional")
    st.markdown("Este módulo evalúa las cargas emocionales heredadas de tus líneas materna y paterna, basándose en principios epigenéticos y observaciones clínicas.")
    st.markdown("**Instrucciones:** Marca cuánto te identificas con cada afirmación relacionada con tu madre y tu padre biológicos. Las respuestas ayudarán a detectar posibles heridas epigenéticas activas.")

    lineas = {
        "Línea Materna": [
            "Siento que debo cuidar de los demás incluso cuando estoy agotado.",
            "Me cuesta poner límites con personas cercanas.",
            "Tiende a atraer relaciones en las que no me valoran.",
            "Me culpo por errores que no son míos.",
            "Tengo una sensación de vacío a pesar de tener afecto."
        ],
        "Línea Paterna": [
            "Me cuesta confiar en la vida o en los demás.",
            "Necesito demostrar constantemente mi valor.",
            "Me exijo en exceso y me cuesta descansar.",
            "Tengo miedo de fallar o ser débil.",
            "Siento que tengo que hacerlo todo solo."
        ]
    }

    resultados = {"Línea Materna": 0, "Línea Paterna": 0}

    for linea, preguntas in lineas.items():
        st.subheader(linea)
        for i, p in enumerate(preguntas):
            respuesta = st.slider(f"{p}", 1, 5, 3, key=f"{linea}_{i}")
            resultados[linea] += respuesta

    if st.button("Analizar carga epigenética"):
        st.markdown("## Resultado:")
        for linea, puntaje in resultados.items():
            promedio = puntaje / 5
            if promedio >= 4:
                estado = "Herida epigenética intensa"
            elif promedio >= 3:
                estado = "Herida epigenética moderada"
            else:
                estado = "Carga emocional leve o ausente"
            st.info(f"{linea}: {estado} (Promedio: {promedio:.2f}/5)")

        st.markdown("📲 Si deseas explorar cómo liberar estas cargas, puedes contactarme directamente: [WhatsApp +56967010107](https://wa.me/56967010107)")
