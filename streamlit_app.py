import streamlit as st
import glob
import os

# Configuración de la página
st.set_page_config(
    page_title="ANIMa-10: Poietic Freedom",
    page_icon="🎨",
    layout="wide"
)

# Título y descripción
st.title("ANIMa-10: Explorador de Libertad Poiética 🎨")
st.write("""
Esta aplicación acompaña al paper **“Creative Freedom: Novelty, Non-Necessity, and Self-Determination Without Prior Rule.”**

Utiliza el menú de la izquierda para navegar por las diferentes secciones y explorar los casos de estudio.
""")

# Mostrar los casos de estudio disponibles
st.header("Casos de Estudio Disponibles")
case_files = glob.glob("data/case_files/**/*.json", recursive=True)

if not case_files:
    st.warning("No se encontraron archivos de casos en la carpeta `data/case_files/`.")
else:
    # Creamos dos columnas para mostrar los casos
    col1, col2 = st.columns(2)
    
    # Dividimos la lista de archivos para las columnas
    mid_point = len(case_files) // 2
    
    with col1:
        for file in case_files[:mid_point]:
            st.info(os.path.basename(file).replace('.json', ''))
    
    with col2:
        for file in case_files[mid_point:]:
            st.info(os.path.basename(file).replace('.json', ''))
