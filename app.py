import os
import io
import joblib
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# 🔹 CONFIGURACIÓN GENERAL
# =========================

st.title("🧪 Sistema de Predicción con Modelos Combinados")

st.markdown("""
Este sistema permite realizar predicciones basadas en modelos de Machine Learning.
Puedes ingresar datos manualmente o subir archivos.
""")

st.divider()

# =========================
# 🔹 GRÁFICOS DE MODELO
# =========================

st.header("📊 Análisis Gráfico de los Modelos")

carpeta_imagenes = "graficos del modelo"

if os.path.exists(carpeta_imagenes):
    imagenes = [f for f in os.listdir(carpeta_imagenes)
                 if f.endswith(('.png', '.jpg', '.jpeg'))]

    if imagenes:
        for img in imagenes:
            ruta = os.path.join(carpeta_imagenes, img)
            st.image(ruta, caption=img, use_container_width=True)
    else:
        st.warning("No hay imágenes en la carpeta.")
else:
    st.warning("Carpeta de gráficos no encontrada.")

st.divider()

# =========================
# 🔹 MÉTRICAS MODELOS
# =========================

model_metrics = {
    "r1_iram1622": {"MAE": 1.66, "RMSE": 2.59},
    "r2_iram1622": {"MAE": 1.49, "RMSE": 1.88},
    "r3_iram1622": {"MAE": 2.16, "RMSE": 3.05},
    "r7_iram1622": {"MAE": 1.75, "RMSE": 2.19},
    "r28_iram1622": {"MAE": 1.42, "RMSE": 1.81},
}

selected_model = st.selectbox(
    "🔍 Selecciona un modelo:",
    list(model_metrics.keys())
)

metrics = model_metrics[selected_model]

st.write(f"MAE: {metrics['MAE']}")
st.write(f"RMSE: {metrics['RMSE']}")

st.divider()

# =========================
# 🔹 MODELOS ML
# =========================

MODEL_DIR = "modelos_guardados"

# ⚠️ IMPORTANTE:
# Cargar modelos con cuidado (puede fallar si archivos no existen)

try:
    MODELS = {
        "D1": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r1_iram1622.joblib")),
        "D2": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r2_iram1622.joblib")),
        "D3": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r3_iram1622.joblib")),
        "D7": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r7_iram1622.joblib")),
        "D28": joblib.load(os.path.join(MODEL_DIR, "mejor_modelo_r28_iram1622.joblib")),
    }
except Exception as e:
    st.error(f"❌ Error cargando modelos: {e}")
    MODELS = {}

# =========================
# 🔹 FEATURES
# =========================

FEATURES = ['pf', 'so3', 'mgo', 'sio2', 'fe2o3', 'caot', 'al2o3', 'na2o', 'k2o']

# =========================
# 🔹 INPUT DE DATOS
# =========================

st.sidebar.title("Configuración")

modo = st.sidebar.radio("Modo de entrada", ["Manual", "Archivo"])

# -------------------------
# Entrada manual
# -------------------------
if modo == "Manual":
    datos = {}

    for col in FEATURES:
        datos[col] = st.sidebar.number_input(col, value=0.0)

    X_input = pd.DataFrame([datos])

# -------------------------
# Entrada archivo
# -------------------------
else:
    file = st.sidebar.file_uploader("Sube CSV o XLSX", type=["csv", "xlsx"])

    if file:
        if file.name.endswith(".csv"):
            X_input = pd.read_csv(file)
        else:
            X_input = pd.read_excel(file)

        X_input = X_input[FEATURES]

# =========================
# 🔹 PREDICCIÓN
# =========================

if "X_input" in locals() and MODELS:

    st.subheader("📊 Resultados")

    st.write(X_input)

    predictions = {}          # ✔️ IMPORTANTE: debe existir
    summary_results = {}

    # 🔁 recorrer modelos
    for name, model in MODELS.items():
        try:
            pred = model.predict(X_input)

            predictions[name] = pred
            summary_results[name] = {
                "Mínimo": pred.min(),
                "Máximo": pred.max()
            }

        except Exception as e:
            st.error(f"Error en modelo {name}: {e}")

    # =========================
    # 🔹 RESULTADOS
    # =========================

    predictions_df = pd.DataFrame(predictions)
    summary_df = pd.DataFrame.from_dict(summary_results, orient="index")

    st.write("### Predicciones")
    st.dataframe(predictions_df)

    st.write("### Resumen")
    st.dataframe(summary_df)

    # =========================
    # 🔹 DESCARGAS
    # =========================

    st.download_button(
        "Descargar CSV",
        predictions_df.to_csv(index=False),
        "predicciones.csv",
        "text/csv"
    )

    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        predictions_df.to_excel(writer, index=False)

    st.download_button(
        "Descargar Excel",
        buffer.getvalue(),
        "predicciones.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
