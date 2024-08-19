import pytest
from unittest.mock import patch
import pandas as pd
import streamlit as st
from predi import show_history 

@patch('predi.pd.read_csv')
@patch('predi.st.dataframe')
    
def test_show_history(mock_dataframe, mock_read_csv):
        # Configuracion del mock para read_csv
        mock_read_csv.return_value = pd.DataFrame({
            'col1': [1, 2],
            'col2': ['a', 'b']
        })

        # Llamar la función
        show_history()

        # Verificacion de read_csv fue llamado correctamente
        mock_read_csv.assert_called_once_with('diagnosticos.csv')

        # Verificacion de dataframe fue llamado con el DataFrame correcto
        mock_dataframe.assert_called_once_with(mock_read_csv.return_value)