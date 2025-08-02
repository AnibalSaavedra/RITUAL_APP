
import streamlit as st
from fpdf import FPDF
from datetime import datetime
import base64
from io import BytesIO

def modulo_disociacion():
    st.header("Test de Disociación o Trauma (DES-II)")
    st.markdown("Este módulo evalúa la presencia de disociación psíquica, una desconexión emocional o fragmentación del yo que puede tener origen en eventos traumáticos.")
    st.markdown("**Instrucciones:** Lee cada afirmación y responde cuánto te identificas con ella del 1 al 5. Si no entiendes alguna afirmación, puedes presionar el botón “¿Qué significa esto?” para una breve explicación.")

    afirmaciones = [
        "A menudo siento que no soy yo quien está experimentando lo que hago.",
        "Siento que estoy observando mi vida como si fuera una película.",
        "Pierdo la noción del tiempo y no recuerdo lo que hice.",
        "A veces me encuentro en un lugar sin saber cómo llegué ahí.",
        "Me desconecto emocionalmente cuando algo me molesta.",
        "Siento que tengo múltiples versiones de mí mismo.",
        "Tengo recuerdos que no parecen míos.",
        "Me cuesta recordar detalles de momentos importantes.",
        "Mi cuerpo se siente ajeno a mí en algunas ocasiones.",
        "Siento que funciono como un robot, sin emociones."
    ]

    explicaciones = [
        "Sensación de no habitar el propio cuerpo durante acciones cotidianas.",
        "Vivencias similares a mirar una película en tercera persona.",
        "Períodos de tiempo con lagunas de memoria inexplicables.",
        "Llegar a lugares sin recordar el trayecto.",
        "Desconectarse emocionalmente frente a conflictos.",
        "Percepción interna de tener varias identidades.",
        "Recuerdos que parecen ajenos o confusos.",
        "Fallas para recordar eventos clave personales.",
        "Sensación de que el cuerpo no es propio.",
        "Actuar sin emoción, como si fueras una máquina."
    ]

    if "respuestas" not in st.session_state:
        st.session_state.respuestas = {}
    if "mostrar_explicacion" not in st.session_state:
        st.session_state.mostrar_explicacion = [False]*len(afirmaciones)

    for i, pregunta in enumerate(afirmaciones):
        cols = st.columns([6, 1])
        with cols[0]:
            st.session_state.respuestas[i] = st.slider(f"{i+1}. {pregunta}", 1, 5, 3, key=f"slider_{i}")
        with cols[1]:
            if st.button("❓", key=f"btn_{i}"):
                st.session_state.mostrar_explicacion[i] = not st.session_state.mostrar_explicacion[i]
        if st.session_state.mostrar_explicacion[i]:
            st.info(f"ℹ️ {explicaciones[i]}")

    if st.button("Obtener resultados"):
        puntaje_total = sum(st.session_state.respuestas.values())
        promedio = puntaje_total / len(afirmaciones)
        estado = "Alta disociación" if promedio > 3.5 else "Disociación leve o moderada"

        st.success(f"Tu nivel de disociación: **{estado}** (Promedio: {promedio:.2f}/5)")
        st.markdown("🔎 A continuación puedes descargar tu informe personalizado en PDF o contactar por WhatsApp.")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Informe – Test de Disociación", ln=1)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Fecha: {datetime.today().strftime('%d/%m/%Y')}", ln=1)
        pdf.multi_cell(0, 10, f"Resultado: {estado} (Promedio: {promedio:.2f}/5)\n\nEste resultado sugiere que existe un nivel {'alto' if promedio > 3.5 else 'moderado'} de desconexión emocional, posiblemente asociado a experiencias traumáticas. Se recomienda una evaluación terapéutica más profunda.")

        pdf.cell(0, 10, "", ln=1)
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 10, "Aníbal Saavedra – Biotecnólogo MIB", ln=1)

        buffer = BytesIO()
        pdf.output(buffer)
        buffer.seek(0)
        b64_pdf = base64.b64encode(buffer.read()).decode("utf-8")
        href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="informe_disociacion.pdf">📄 Descargar informe PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

        st.markdown("📲 ¿Deseas apoyo terapéutico? [Contáctame por WhatsApp](https://wa.me/56967010107)")
