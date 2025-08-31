# streamlit_app.py
import streamlit as st

st.set_page_config(
    page_title="Introducción | ANIMa-10",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Creative Freedom: El Paper")

st.header("Resumen (Abstract)")

# Texto extraído del paper art3.pdf
st.info("""
Este artículo reconceptualiza la libertad humana como **libertad poiética**: la capacidad de instituir realidades no deducibles de reglas o razones previas. En contra de los modelos electivos dominantes —que reducen la agencia a seleccionar entre opciones predefinidas—, argumentamos que los casos paradigmáticos de libertad (ej., fundar instituciones legales, inventar técnicas, crear arte) implican una expansión ontológica en lugar de una optimización.
""") #

st.markdown("---")

# Botón para descargar el PDF del paper
st.subheader("Descargar Artículo Completo")
st.write("Puedes descargar el documento PDF completo para conocer la metodología en detalle.")

try:
    with open("pages/art3.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Descargar art3.pdf",
        data=PDFbyte,
        file_name="creative_freedom_paper.pdf",
        mime='application/octet-stream'
    )
except FileNotFoundError:
    st.error("No se pudo encontrar el archivo 'pages/art3.pdf'. Asegúrate de que está en la ubicación correcta.")
