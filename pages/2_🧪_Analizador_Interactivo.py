import os
import tempfile

import streamlit as st

from src.mdl_delta import mdl_delta
from src.network_rupture import load_edge_list_csv, rupture_score

st.set_page_config(page_title="Analizador Interactivo", page_icon="🔬")

st.title("🔬 Analizador Interactivo de Actos Poiéticos")

st.info("Introduce tus propios datos para calcular las señales de novedad (MDL-Δ) y ruptura de red.")

st.markdown("---")

# --- SECCIÓN DE ENTRADA DE DATOS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Corpus Textual")
    pre_text = st.text_area("Texto Previo (Pre-Corpus)", height=150, placeholder="Escribe o pega aquí el texto base...")
    post_text = st.text_area("Texto Posterior (Post-Corpus)", height=150, placeholder="Escribe o pega aquí el texto con la novedad...")

with col2:
    st.subheader("2. Grafos de Red (CSV)")
    pre_graph_file = st.file_uploader("Sube el Grafo Previo (.csv)", type="csv")
    post_graph_file = st.file_uploader("Sube el Grafo Posterior (.csv)", type="csv")

st.markdown("---")


# --- SECCIÓN DE ANÁLISIS Y RESULTADOS ---
if st.button("Calcular Métricas", type="primary"):

    st.header("Resultados del Análisis")

    # Comprobamos que hay datos para analizar
    if not pre_text and not post_text and not pre_graph_file and not post_graph_file:
        st.warning("Por favor, introduce texto o sube archivos para analizar.")
    else:
        res_col1, res_col2 = st.columns(2)

        # --- Cálculo de MDL-Delta ---
        with res_col1:
            st.subheader("MDL-Δ (Novedad Textual)")
            if pre_text and post_text:
                try:
                    mdl_score = mdl_delta(pre_text, post_text)
                    st.metric(label="Puntuación MDL-Δ", value=f"{mdl_score:.4f}")
                    st.write("Esta métrica (proxy de Minimum Description Length) mide el cambio en la compresibilidad del texto. Un valor positivo alto sugiere la introducción de nueva información.")
                except Exception as e:
                    st.error(f"Error al calcular MDL-Δ: {e}")
            else:
                st.info("Introduce texto en ambos campos para calcular la novedad textual.")

        # --- Cálculo de Ruptura de Red ---
        with res_col2:
            st.subheader("Ruptura de Red")
            if pre_graph_file and post_graph_file:
                tmp_pre_path = None
                tmp_post_path = None
                try:
                    with tempfile.NamedTemporaryFile(mode="wb", suffix=".csv", delete=False) as tmp_pre:
                        tmp_pre.write(pre_graph_file.getvalue())
                        tmp_pre_path = tmp_pre.name

                    with tempfile.NamedTemporaryFile(mode="wb", suffix=".csv", delete=False) as tmp_post:
                        tmp_post.write(post_graph_file.getvalue())
                        tmp_post_path = tmp_post.name

                    g0 = load_edge_list_csv(tmp_pre_path)
                    g1 = load_edge_list_csv(tmp_post_path)

                    rupture = rupture_score(g0, g1)
                    st.metric(label="Puntuación de Ruptura", value=f"{rupture:.4f}")
                    st.write("Mide el cambio en la estructura del grafo (componente conectado más grande y clustering). Un valor alto sugiere una reorganización estructural significativa.")

                except Exception as e:
                    st.error(f"Error al procesar los archivos CSV: {e}")
                finally:
                    for path in (tmp_pre_path, tmp_post_path):
                        if path and os.path.exists(path):
                            os.remove(path)
            else:
                st.info("Sube ambos archivos CSV para calcular la ruptura de red.")
