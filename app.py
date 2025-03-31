import streamlit as st

# Encabezado de la aplicación
st.set_page_config(page_title="Sistema de Predicción", page_icon="🚗", layout="wide")

# Título principal
st.title("Sistema de Predicción para Transporte")

# Agregar barra de navegación
navigation = st.sidebar.selectbox("Selecciona un sistema", ("Detector de Estado de Neumáticos", "Predictor de Consumo de Combustible"))

# Sección: Detector de Estado de Neumáticos
if navigation == "Detector de Estado de Neumáticos":
    st.header("Detector de Estado de Neumáticos")
    st.write("""
    El detector de estado de neumáticos utiliza sensores y algoritmos de aprendizaje automático para monitorear las condiciones de los neumáticos en tiempo real. 
    Puede detectar patrones que indican desgaste irregular, baja presión o posibles fallos. 
    Esto ayuda a prevenir accidentes y mejora la eficiencia del vehículo al mantener los neumáticos en condiciones óptimas.
    """)

    st.subheader("¿Cómo funciona?")
    st.write("""
    Este sistema utiliza sensores de presión, temperatura y vibración para monitorizar el estado de los neumáticos. 
    Los datos recogidos se envían a un modelo de aprendizaje automático que los analiza y proporciona alertas sobre la necesidad de mantenimiento o reemplazo.
    """)

    st.subheader("Beneficios")
    st.write("""
    - **Mayor seguridad**: Detecta fallos antes de que ocurran.
    - **Reducción de costos**: Previene desgastes y accidentes costosos.
    - **Eficiencia operativa**: Mejora la eficiencia del combustible al asegurar que los neumáticos estén en buen estado.
    """)


# Sección: Predictor de Consumo de Combustible
elif navigation == "Predictor de Consumo de Combustible":
    st.header("Predictor de Consumo de Combustible")
    st.write("""
    El predictor de consumo de combustible utiliza datos de rutas, condiciones del vehículo y el entorno para estimar el consumo de combustible. 
    Esto es especialmente útil para optimizar las rutas y reducir los costos operativos en el transporte de carga.
    """)

    st.subheader("¿Cómo funciona?")
    st.write("""
    Este sistema se basa en modelos predictivos que analizan diferentes factores como el peso de la carga, la distancia recorrida, 
    las condiciones meteorológicas y el tipo de vehículo para predecir el consumo de combustible.
    """)

    st.subheader("Beneficios")
    st.write("""
    - **Optimización de rutas**: Reduce el consumo de combustible al elegir las rutas más eficientes.
    - **Control de costos**: Mejora la gestión de los costos operativos.
    - **Reducción de emisiones**: Contribuye a la sostenibilidad al minimizar el consumo de combustible.
    """)


# Footer
st.markdown("---")
st.write("Desarrollado por: Tu nombre o tu empresa")
