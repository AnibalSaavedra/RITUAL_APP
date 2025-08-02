
import streamlit as st
from modulo_disociacion import ejecutar_test_disociacion
from modulo_epigenetico import ejecutar_test_epigenetico

st.set_page_config(page_title="MBI 360° – Evaluación Integral del Ser", layout="centered")

st.title("🌀 MBI 360° – Evaluación Integral del Ser")

st.markdown("""
Bienvenido al sistema **MBI 360°**, una herramienta única para conocer en profundidad tu estado emocional, epigenético, físico y energético.

**Marca:** RITUAL  
**Creador:** Aníbal Saavedra – Biotecnólogo MIB
""")

st.markdown("### Selecciona uno o varios módulos que deseas realizar:")

modulos = {
    "Test de disociación o trauma": False,
    "Estado epigenético emocional (líneas materna/paterna)": False
}

seleccion = []
seleccion.append(st.checkbox("Test de disociación o trauma"))
seleccion.append(st.checkbox("Estado epigenético emocional (líneas materna/paterna)"))

if not any(seleccion):
    st.warning("Selecciona al menos un módulo para continuar.")
else:
    if seleccion[0]:
        ejecutar_test_disociacion()
    if seleccion[1]:
        ejecutar_test_epigenetico()
