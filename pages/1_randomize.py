import streamlit as st
import pandas as pd
import random
import time  # For delay simulation

# Load the Excel file
file_path = "Random Groups Bruxism Treatment.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Sheet1')

# Mapping of groups to treatment descriptions
treatment_mapping = {
    1: "Férula Oclusal",
    2: "Férula Oclusal + Terapia Manual",
    3: "Férula Oclusal + Terapia Manual + Terapia Cognitiva Conductual"
}

# Streamlit Page Configuration
st.set_page_config(page_title="Asignación de Tratamiento",
                   page_icon="💊", layout="centered")

# Custom CSS to match Figma Design
st.markdown(
    """
    <style>
        body {
            background-color: #F7F7F7;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #A2C4E5;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .input-box label {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        .stTextInput>div>div>input {
            background-color: #EDEDED;
            border: 1px solid #D1D1D1;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton>button {
            width: 100%;
            padding: 15px;
            font-size: 18px;
            font-weight: bold;
            background-color: #B0D0E8;
            color: black;
            border-radius: 12px;
            border: none;
            box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.2);
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #94BBD7;
        }
        .result {
            text-align: center;
            font-size: 20px;
            font-weight: normal;
            color: #333;
            margin-top: 20px;
        }
        .result b {
            font-weight: bold;
            color: black;
        }
        .result a {
            font-weight: bold;
            text-decoration: none;
            color: #1E4E79;
        }
        .loading-text {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #A2C4E5;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="title">Asignación de Tratamiento</div>',
            unsafe_allow_html=True)

# Input for Name
nombre_apellido = st.text_input("Nombre y Apellido:", "", key="name_input")

# Button above the response
generate_button = st.button("Generar Número y Asignar Tratamiento")

# Placeholder for response (ensures button stays above)
response_placeholder = st.empty()

if generate_button:
    if nombre_apellido.strip():  # Ensure name is not empty
        with response_placeholder:  # Use placeholder for dynamic update
            with st.spinner("Asignando tratamiento..."):  # Show loading animation
                time.sleep(2.5)  # Delay for effect

        # Generate a random number between 1 and 48
        numero_aleatorio = random.randint(1, 48)

        # Find the corresponding row in the DataFrame
        persona_id = f"Persona {numero_aleatorio}"
        row = df[df["NOMBRE"] == persona_id]

        if not row.empty:
            grupo = int(row.iloc[0]["GRUPO"])
            tratamiento = treatment_mapping.get(
                grupo, "Tratamiento Desconocido")

            # Update the placeholder with result
            response_placeholder.markdown(
                f'<div class="result">A <a>{nombre_apellido}</a> le corresponde el número <b>{numero_aleatorio}</b> '
                f'y le corresponde el tratamiento de <b>{tratamiento}</b>.</div>',
                unsafe_allow_html=True
            )
        else:
            response_placeholder.error(
                f"No se encontró información para el número {numero_aleatorio}.")
    else:
        st.warning(
            "Por favor, ingresa tu Nombre y Apellido antes de generar el número.")
