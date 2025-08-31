import streamlit as st

st.set_page_config(
    page_title="Introducción",
    page_icon="📄"
)

st.title("📄 Introducción al Proyecto")

st.header("¿Qué es la Libertad Poiética?")
st.write("""
Este proyecto explora el concepto de **libertad poiética**: la capacidad de crear realidades que no se pueden deducir de reglas o razones previas.

A diferencia de los modelos que ven la libertad como una simple elección entre opciones predefinidas, la libertad poiética se centra en actos que expanden lo que es posible, como por ejemplo:
- La creación de nuevas leyes (ej. *habeas corpus*).
- La invención de técnicas revolucionarias (ej. la porcelana).
- La composición de formas artísticas inéditas.
""")

st.success("Este es el nuevo contenido de la página de introducción. ¡El mensaje de ejemplo ha sido reemplazado!")
