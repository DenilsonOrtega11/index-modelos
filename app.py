import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Sistema de Predicción", page_icon="🚗", layout="wide")

# Título principal
st.title("Sistema de Predicción para Transporte")

# Barra de navegación en el sidebar
navigation = st.sidebar.selectbox("Selecciona un sistema", ("Detector de Estado de Neumáticos", "Predictor de Consumo de Combustible"))

# Sección: Detector de Estado de Neumáticos
if navigation == "Detector de Estado de Neumáticos":
    st.header("Detector de Estado de Neumáticos")
    st.write("""
    El detector de estado de neumáticos utiliza imágenes para identificar posibles fallos, desgaste irregular o baja presión en los neumáticos.
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

# Sección: Predictor de Consumo de Combustible
elif navigation == "Predictor de Consumo de Combustible":
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

# Footer
st.markdown("---")
st.write("Desarrollado por: Tu nombre o tu empresa")
