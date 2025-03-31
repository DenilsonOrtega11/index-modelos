import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Sistema de Predicción", page_icon="🚗", layout="wide")

# Función para personalizar el fondo y colores
def set_dark_theme():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #2e2e2e;
            color: #ffffff;
        }}
        .sidebar .sidebar-content {{
            background-color: #2e2e2e;
            color: #ffffff;
        }}
        .stButton > button {{
            background-color: #4a4a4a;
            color: white;
            border: 1px solid #2e2e2e;
        }}
        .stButton > button:hover {{
            background-color: #555555;
        }}
        .stMarkdown {{
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Establecer el tema oscuro
set_dark_theme()

# Título principal
st.title("Sistema de Predicción para Transporte")

# Barra de navegación en el sidebar
navigation = st.sidebar.selectbox("Selecciona un sistema", ("Detector de Estado de Neumáticos", "Predictor de Consumo de Combustible"))

# Sección: Detector de Estado de Neumáticos
if navigation == "Detector de Estado de Neumáticos":
    # Sección con fondo oscuro para esta parte
    st.header("Detector de Estado de Neumáticos")
    st.write(""" 
    El detector de estado de neumáticos utiliza imágenes para identificar posibles fallos o desgaste irregular en los neumáticos.
    Utiliza un modelo de aprendizaje automático que analiza las imágenes para detectar problemas y proporciona recomendaciones para el mantenimiento.
    """)

    st.subheader("¿Cómo funciona?")
    st.write("""
    Puedes cargar una imagen del neumático, y el modelo analizará la imagen para determinar si está en buen estado o necesita atención.
    """)

    st.subheader("Beneficios")
    st.write("""
    - **Seguridad**: Detecta daños antes de que se conviertan en problemas graves.
    - **Prevención de accidentes**: Ayuda a identificar neumáticos en mal estado.
    - **Eficiencia operativa**: Evita fallos imprevistos.
    """)

    st.subheader("Tecnologías utilizadas")
    st.write("""
    - Modelo de aprendizaje automático.
    - Análisis de imágenes.
    """)

    # Enlace para redirigir al modelo de neumáticos
    st.markdown(
        "[Ir al Detector de Estado de Neumáticos](https://estadoneu-dyosb9wwmnc7h3uixb6bvh.streamlit.app/)", 
        unsafe_allow_html=True
    )

# Sección: Predictor de Consumo de Combustible
elif navigation == "Predictor de Consumo de Combustible":
    # Sección con fondo oscuro para esta parte
    st.header("Predictor de Consumo de Combustible")
    st.write("""
    El predictor de consumo de combustible estima el consumo de combustible en vehículos de carga utilizando datos del vehículo y de la ruta.
    Basado en datos como el peso de la carga, la distancia y el tipo de vehículo, predice el consumo de combustible y permite optimizar las rutas.
    """)

    st.subheader("¿Cómo funciona?")
    st.write("""
    Este sistema utiliza datos como el peso de la carga, la distancia recorrida, el tipo de vehículo y el tipo de combustible para predecir el consumo.
    """)

    st.subheader("Beneficios")
    st.write("""
    - **Optimización de rutas**: Reduce el consumo al elegir las mejores rutas.
    - **Control de costos**: Ayuda a gestionar el consumo de combustible.
    - **Sostenibilidad**: Minimiza el impacto ambiental al reducir el consumo de combustible.
    """)

    st.subheader("Tecnologías utilizadas")
    st.write("""
    - Algoritmos de predicción.
    - Optimización de rutas.
    """)

    # Enlace para redirigir al predictor de consumo de combustible
    st.markdown(
        "[Ir al Predictor de Consumo de Combustible](https://consumo-9ja385zt2x7wx5br7vk5tk.streamlit.app/)", 
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.write("Desarrollado por: Denilson Ortega Jimenez")
