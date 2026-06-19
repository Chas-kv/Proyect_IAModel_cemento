import os
import io
import joblib
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# 🔹 Título principal
st.title("🧪 Sistema de Predicción con Modelos Combinados")

st.markdown("""
Este sistema permite realizar predicciones basadas en un enfoque de **modelos combinados**.  
Se utilizan métricas como **RMSE** y **MAE** para evaluar el rendimiento de los modelos.  

### 📌 ¿Cómo usar este sistema?
- Puedes **ingresar manualmente** las cantidades de químicos para la predicción de la resistencia del cemento.
- O bien, **subir un archivo CSV o XLSX** con los datos para múltiples predicciones.
- Se mostrarán los resultados de predicción junto con **valores mínimo y máximo** de resistencia estimada.
""")

# 🔹 Separador
st.divider()

# 🔹 Sección de Análisis Gráfico
st.header("📊 Análisis Gráfico de los Modelos por Día")

st.markdown("""
Esta sección permite visualizar los **resultados de predicción para cada día del modelo entrenado** , mostrando:  
✔️ **Comportamiento del modelo**  
✔️ **Precisión y posibles errores**  
✔️ **Evaluación del desempeño en la estimación de la resistencia del cemento**
""")
# Definir la carpeta donde están las imágenes
carpeta_imagenes = "graficos del modelo"

# 🔹 Verificar si la carpeta existe y mostrar imágenes
if os.path.exists(carpeta_imagenes):
    imagenes = [f for f in os.listdir(carpeta_imagenes) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if imagenes:
        for imagen in imagenes:
            ruta_imagen = os.path.join(carpeta_imagenes, imagen)
            st.image(ruta_imagen, caption=f"📌 {imagen}", use_container_width=True)
    else:
        st.warning("⚠️ No se encontraron imágenes en la carpeta.")
else:
    st.warning("⚠️ La carpeta de imágenes no existe.")

# 🔹 Separador
st.divider()
# Datos de métricas de los modelos
model_metrics = {
    "r1_iram1622": {"MAE": 1.66, "RMSE": 2.59},
    "r2_iram1622": {"MAE": 1.49, "RMSE": 1.88},
    "r3_iram1622": {"MAE": 2.16, "RMSE": 3.05},
    "r7_iram1622": {"MAE": 1.75, "RMSE": 2.19},
    "r28_iram1622": {"MAE": 1.42, "RMSE": 1.81},
}

# 🔹 Selección de modelo
selected_model = st.selectbox("🔍 Selecciona un modelo para evaluar:", list(model_metrics.keys()))

# 🔹 Mostrar métricas del modelo seleccionado
if selected_model:
    metrics = model_metrics[selected_model]
    st.subheader(f"📊 Evaluación del Modelo: `{selected_model}`")
    st.write(f"- **MAE:** `{metrics['MAE']}`")
    st.write(f"- **RMSE:** `{metrics['RMSE']}`")

    # 🔹 Interpretación de precisión
    if metrics['MAE'] < 1.5 and metrics['RMSE'] < 2:
        st.success("✅ Este modelo es **altamente preciso**.")
    elif metrics['MAE'] < 1.8 and metrics['RMSE'] < 2.5:
        st.info("ℹ️ Este modelo tiene una **buena precisión**.")
    else:
        st.warning("⚠️ Este modelo tiene un **margen de error más alto**. Puede no ser la mejor opción.")

    # 🔹 Visualización con gráfico de barras
    st.subheader("📉 Comparación de Errores")
    df_metrics = pd.DataFrame.from_dict(model_metrics, orient='index')
    st.bar_chart(df_metrics)
    
# 🔹 Separador
st.divider()

# Directorio donde están los modelos dentro del repositorio
MODEL_DIR = "modelos_guardados"

# Cargar modelos usando rutas relativas
#MODELS = {
 #   "Resistencia del cemento D1": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r1_iram1622.joblib")),
  #  "Resistencia del cemento D2": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r2_iram1622.joblib")),
   # "Resistencia del cemento D3": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r3_iram1622.joblib")),
    #"Resistencia del cemento D7": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r7_iram1622.joblib")),
 #   "Resistencia del cemento D28": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r28_iram1622.joblib"))
#}

FEATURES = ['pf', 'so3', 'mgo', 'sio2', 'fe2o3', 'caot', 'al2o3', 'na2o', 'k2o']




st.sidebar.title("Configuración")
data_input_mode = st.sidebar.radio("Selecciona el modo de entrada de datos", ("Manual", "Archivo"))

# Entrada manual de datos
if data_input_mode == "Manual":
    st.sidebar.subheader("Ingresa los valores manualmente")
    input_data = {}
    for col in FEATURES:
        input_data[col] = st.sidebar.number_input(col, value=0.0, min_value=0.0)
    X_input = pd.DataFrame([input_data])

# Carga de archivo de datos
else:
    st.sidebar.subheader("Carga un archivo de datos")
    uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV o Excel", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            X_input = pd.read_csv(uploaded_file)
        else:
            X_input = pd.read_excel(uploaded_file)
        X_input = X_input[FEATURES]

if 'X_input' in locals():
    st.title("Aquí están los resultados de tu consulta")
    st.subheader("Predicciones")
    st.write("Datos de entrada:", X_input)
  #  predictions = {}
    summary_results = {}
    
   # for name, model in MODELS.items():
     #   try:
       #     pred_values = model.predict(X_input)
        #    predictions[name] = pred_values
         #   summary_results[name] = {"Mínimo": pred_values.min(), "Máximo": pred_values.max()}
        #except ValueError as e:
         #   st.error(f"Error al predecir con {name}: {e}")
          #  predictions[name] = []
           # summary_results[name] = {"Mínimo": None, "Máximo": None}
    
    predictions_df = pd.DataFrame(predictions)
    summary_df = pd.DataFrame.from_dict(summary_results, orient='index')
    
    st.subheader("Resultados de Predicción")
    st.write(predictions_df)
    
    st.subheader("Resumen de Predicciones (Máx y Mín)")
    st.write(summary_df)
    
    # Descargar resultados
    csv_data_results = predictions_df.to_csv(index=False)
    st.download_button(
        label="Descargar Resultados como CSV",
        data=csv_data_results,
        file_name="predicciones_resultados.csv",
        mime="text/csv"
    )
    
    csv_data_summary = summary_df.to_csv()
    st.download_button(
        label="Descargar Resumen como CSV",
        data=csv_data_summary,
        file_name="predicciones_resumen.csv",
        mime="text/csv"
    )
    
    excel_buffer_results = io.BytesIO()
    with pd.ExcelWriter(excel_buffer_results, engine='openpyxl') as writer:
        predictions_df.to_excel(writer, index=False, sheet_name='Predicciones')
    st.download_button(
        label="Descargar Resultados como Excel",
        data=excel_buffer_results.getvalue(),
        file_name="predicciones_resultados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
    excel_buffer_summary = io.BytesIO()
    with pd.ExcelWriter(excel_buffer_summary, engine='openpyxl') as writer:
        summary_df.to_excel(writer, sheet_name='Resumen')
    st.download_button(
        label="Descargar Resumen como Excel",
        data=excel_buffer_summary.getvalue(),
        file_name="predicciones_resumen.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    

