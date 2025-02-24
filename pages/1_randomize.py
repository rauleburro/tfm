import streamlit as st
import pandas as pd
import random
import time  # For delay simulation
from datetime import datetime

# Load the reference Excel file
file_path = "random.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Sheet1')

# File to store assignments
assignments_file = "asignaciones.xlsx"
try:
    assignments_df = pd.read_excel(assignments_file)
except FileNotFoundError:
    assignments_df = pd.DataFrame(
        columns=['Fecha', 'Nombre', 'Número', 'Tratamiento'])

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
        # Check if name already exists
        if nombre_apellido in assignments_df['Nombre'].values:
            st.error("Este nombre ya ha sido registrado anteriormente.")
        else:
            with response_placeholder:  # Use placeholder for dynamic update
                with st.spinner("Asignando tratamiento..."):  # Show loading animation
                    time.sleep(0.4)  # Delay for effect

            # Generate random numbers until finding one that hasn't been used
            assigned_numbers = assignments_df['Número'].tolist()
            numero_aleatorio = random.randint(1, 48)
            while numero_aleatorio in assigned_numbers:
                numero_aleatorio = random.randint(1, 48)

            # Find the corresponding row in the DataFrame
            persona_id = f"Persona {numero_aleatorio}"
            row = df[df["NOMBRE"] == persona_id]

            if not row.empty:
                grupo = int(row.iloc[0]["GRUPO"])
                tratamiento = treatment_mapping.get(
                    grupo, "Tratamiento Desconocido")

                # Save to assignments DataFrame
                new_row = {
                    'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'Nombre': nombre_apellido,
                    'Número': numero_aleatorio,
                    'Tratamiento': tratamiento
                }
                assignments_df = pd.concat(
                    [assignments_df, pd.DataFrame([new_row])], ignore_index=True)
                assignments_df.to_excel(assignments_file, index=False)

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


# Display assignments table
if not assignments_df.empty:
    st.markdown("### Asignaciones Realizadas")

    # Create a copy and add selection column
    display_df = assignments_df.copy().sort_values(
        by='Fecha', ascending=True)  # Changed to ascending
    display_df.insert(0, 'Seleccionar', False)
    display_df.insert(1, 'Orden', range(1, len(display_df) + 1))

    # Display the table with checkboxes first
    edited_df = st.data_editor(
        display_df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Seleccionar": st.column_config.CheckboxColumn(
                "Seleccionar",
                help="Select for bulk deletion",
                default=False,
                width="small",
            ),
            "Orden": st.column_config.Column(
                "N°",
                width="small",
            ),
            "Fecha": st.column_config.Column("Fecha", width="medium"),
            "Nombre": st.column_config.Column("Nombre", width="medium"),
            "Número": st.column_config.Column("Número", width="small"),
            "Tratamiento": st.column_config.Column("Tratamiento", width="large"),
        },
        disabled=["Orden", "Fecha", "Nombre", "Número", "Tratamiento"]
    )

    # Add bulk action button after the table is created
    col1, col2 = st.columns([0.2, 0.8])
    with col1:
        if st.button("🗑️"):
            selected_indices = edited_df[edited_df['Seleccionar']].index
            assignments_df.drop(selected_indices, inplace=True)
            assignments_df.to_excel(assignments_file, index=False)
            st.rerun()
