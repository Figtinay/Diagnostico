from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import streamlit as st
from urllib.parse import urlparse, urlunparse
from borrar import clear_window
from guardar import save_diagnosis
from historial import show_history

# Cargar el modelo guardado
model = load_model('modelo_enferm.h5')
categories = ['Quiste', 'Cálculo', 'Tumor', 'Normalidad']

st.title('Predicción de Enfermedades del Riñón a partir de Radiografías')

# Inicializar el estado de la sesión
if 'uploaded_file' not in st.session_state:
    st.session_state['uploaded_file'] = None
if 'result' not in st.session_state:
    st.session_state['result'] = ''
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'id_number' not in st.session_state:
    st.session_state['id_number'] = ''
    
# Entrada de datos del usuario
st.session_state['name'] = st.text_input('Nombre:', st.session_state['name'])
st.session_state['id_number'] = st.text_input('Cédula:', st.session_state['id_number'])   

uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

img_container = st.empty()
result_container = st.empty()

if uploaded_file:
    st.session_state['uploaded_file'] = uploaded_file
    img = Image.open(uploaded_file).convert('L')
    img = img.resize((128, 128), Image.LANCZOS)
    img_container.image(img, caption='Radiografía subida', use_column_width=True)

    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    st.session_state['result'] = categories[np.argmax(prediction)]
    result_container.write(f'Diagnóstico: Paciente con {st.session_state["result"]}')
    # Guardar el diagnóstico con el nombre y la cédula
    save_diagnosis(st.session_state['result'], st.session_state['name'], st.session_state['id_number'])    
    
# Botón para limpiar (puedes implementar la función clear_window)
if st.button('Limpiar'):
    clear_window()
    img_container.empty()
    result_container.empty()

# Botón para ver historial (puedes implementar la función show_history)
if st.button('Ver Historial'):
    show_history()
    st.write("Historial Mostrado con Éxito")