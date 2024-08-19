import streamlit as st
from predi import clear_window

def test_clear_window():
    # Inicializar el estado de la sesión
    st.session_state['name'] = 'Monica Cuellar'
    st.session_state['id_number'] = '1234568'
    
    # Llamar a la función
    clear_window()
    
    # Verificar que los valores se han limpiado
    assert st.session_state['name'] == ''
    assert st.session_state['id_number'] == ''
