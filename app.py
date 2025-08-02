
import streamlit as st
from modulo_disociacion import modulo_disociacion

st.set_page_config(page_title="MBI 360° – Evaluación Integral del Ser", layout="centered")

st.title("🌀 MBI 360° – Evaluación Integral del Ser")
st.markdown("Bienvenido al sistema **MBI 360°**, una herramienta única para conocer en profundidad tu estado emocional, epigenético, físico y energético.")
st.markdown("**Marca:** RITUAL  \\n**Creador:** Aníbal Saavedra – Biotecnólogo MIB")

st.markdown("Selecciona uno o varios módulos que deseas realizar:")
modulos = {
    "Test de disociación o trauma": st.checkbox("Test de disociación o trauma")
}

seleccionados = [k for k, v in modulos.items() if v]

if seleccionados:
    st.markdown("### Has seleccionado los siguientes módulos:")
    if "Test de disociación o trauma" in seleccionados:
        st.markdown("🔹 **Test de disociación o trauma**: Evaluar desconexión emocional y fragmentación del yo.")

    if st.button("👉 Presiona aquí para comenzar"):
        if "Test de disociación o trauma" in seleccionados:
            modulo_disociacion()
else:
    st.warning("Selecciona al menos un módulo para continuar.")
