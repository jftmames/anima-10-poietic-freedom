import streamlit as st

# Esta será la nueva página de inicio que el servidor ejecutará.
st.set_page_config(
    page_title="Bienvenida | ANIMa-10",
    page_icon="👋",
)

# Ocultamos el nombre "Streamlit app" del menú y le damos un título a la página.
st.title("Bienvenido al Explorador de Libertad Poiética 👋")

st.sidebar.success("Selecciona una página para continuar.")

st.markdown(
    """
    Esta aplicación interactiva es el complemento del paper **“Creative Freedom: Novelty, Non-Necessity, and Self-Determination Without Prior Rule.”**

    ### ¿Cómo usar esta herramienta?

    **👈 Selecciona una de las opciones del menú lateral** para comenzar:

    - **Explorador de Casos:** Visualiza y analiza los casos de estudio del proyecto.
    - **Introducción:** Lee el resumen y descarga el paper completo.
    - **Analizador Interactivo:** Prueba las métricas con tus propios textos y grafos.
    """
)
