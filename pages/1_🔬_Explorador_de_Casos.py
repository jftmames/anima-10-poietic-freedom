import streamlit as st
import json
import glob
import os
from src.lstar import l_star # Importamos la función para calcular L*

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Explorador de Casos",
    page_icon="🎨",
    layout="wide"
)

# --- TÍTULO PRINCIPAL ---
st.title("🎨 Explorador de Casos de Estudio")
st.write("Esta página permite analizar los casos de estudio del proyecto usando el Poietic Index `L*`.")

# --- FUNCIÓN PARA CARGAR DATOS ---
# Una función para cargar el contenido de un archivo JSON de forma segura.
def load_case_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error al cargar el archivo {os.path.basename(file_path)}: {e}")
        return None

# --- BARRA LATERAL CON EL SELECTOR ---
st.sidebar.header("Selecciona un Caso de Estudio")

# Buscamos todos los archivos de casos
case_files_paths = glob.glob("data/case_files/**/*.json", recursive=True)

if not case_files_paths:
    st.sidebar.warning("No se encontraron casos de estudio.")
else:
    # Creamos una lista de nombres amigables para el menú
    # Leemos el campo "title" de cada archivo JSON
    case_titles = []
    for path in case_files_paths:
        data = load_case_data(path)
        if data and 'title' in data:
            case_titles.append(data['title'])
        else:
            # Si no hay título, usamos el nombre del archivo
            case_titles.append(os.path.basename(path))

    # Creamos el menú desplegable en la barra lateral
    selected_title = st.sidebar.selectbox(
        "Elige un caso para analizar:",
        options=sorted(case_titles) # Ordenamos los títulos alfabéticamente
    )

    # --- LÓGICA PRINCIPAL DE LA PÁGINA ---
    # Encontrar el archivo correspondiente al título seleccionado
    selected_path = ""
    for path in case_files_paths:
        data = load_case_data(path)
        if data and data.get('title') == selected_title:
            selected_path = path
            break

    if selected_path:
        # Cargamos los datos del caso seleccionado
        case_data = load_case_data(selected_path)
        
        if case_data:
            st.header(f"Análisis de: {case_data.get('title', 'N/A')}")
            
            # Usamos columnas para organizar la información
            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("Puntuación Poietic Index (L*)")
                lstar_scores = case_data.get("Lstar", {})
                
                # Calculamos el L* score final
                final_score = l_star(lstar_scores)
                
                # Mostramos el resultado con un widget de métrica
                st.metric(label="L* Score", value=f"{final_score:.2f}")

                st.write("Puntuaciones por criterio:")
                st.json(lstar_scores)

            with col2:
                st.subheader("Metadatos del Caso")
                st.info(f"**ID:** `{case_data.get('id', 'N/A')}`")
                st.info(f"**Dominio:** {case_data.get('domain', 'N/A')}")
                st.info(f"**Localización:** {case_data.get('locale', 'N/A')}")
                st.info(f"**Fecha:** {case_data.get('t0_interval', 'N/A')}")

            # Mostramos el contenido completo del JSON en un expansor
            with st.expander("Ver datos completos del archivo JSON"):
                st.json(case_data)
