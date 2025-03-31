import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

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

    # Subir imagen de neumático
    uploaded_image = st.file_uploader("Sube una imagen del neumático", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        # Cargar la imagen y preprocesarla para el modelo
        img = image.load_img(uploaded_image, target_size=(64, 64))  # Redimensionamos la imagen
        img_array = image.img_to_array(img)  # Convertimos la imagen a un array
        img_array = np.expand_dims(img_array, axis=0)  # Añadimos una dimensión extra para batch

        # Normalizamos la imagen (dependiendo de tu modelo entrenado)
        img_array = img_array / 255.0

        # Cargar el modelo de neumáticos (asume que ya está entrenado y guardado)
        try:
            model = tf.keras.models.load_model('modelo_neumaticos.h5')
            prediction = model.predict(img_array)
            state = "en buen estado" if prediction[0][0] > 0.5 else "necesita atención"

            st.image(uploaded_image, caption="Imagen del Neumático", use_column_width=True)
            st.write(f"El neumático está {state}.")
        except Exception as e:
            st.write(f"Error al cargar el modelo o predecir: {e}")

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

    # Entradas para el modelo de predicción
    weight = st.number_input("Peso de la carga (kg)", min_value=0, max_value=100000, value=10000)
    distance = st.number_input("Distancia recorrida (km)", min_value=0, max_value=10000, value=100)
    vehicle_type = st.selectbox("Tipo de vehículo", ["Camión pequeño", "Camión mediano", "Camión grande"])
    fuel_type = st.selectbox("Tipo de combustible", ["Diesel", "Gasolina", "Eléctrico"])

    # Simular la predicción (Este es un ejemplo simple)
    if st.button("Predecir Consumo de Combustible"):
        # Aquí debería ir el modelo real de predicción, pero usaremos una fórmula simple como ejemplo
        if vehicle_type == "Camión pequeño":
            base_consumption = 12  # Ejemplo en L/100km
        elif vehicle_type == "Camión mediano":
            base_consumption = 18
        else:
            base_consumption = 25

        # Simulación de consumo dependiendo del peso y la distancia
        fuel_consumption = base_consumption * (weight / 10000) * (distance / 100)
        
        st.write(f"Predicción de consumo de combustible: {fuel_consumption:.2f} litros")

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
