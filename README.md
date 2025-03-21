# Proyecto IA para Predicción de la Resistencia del Cemento

## Descripción

Este proyecto fue desarrollado como parte del Bootcamp en Talento Tech con el objetivo de crear un modelo de Inteligencia Artificial capaz de predecir la resistencia del cemento en distintos días, utilizando como características de entrada nueve compuestos químicos clave en su fabricación. Esta solución busca abordar un problema relevante en la industria de la construcción, optimizando la formulación del cemento y mejorando su desempeño.

## Objetivos

- Aplicar técnicas de preprocesamiento de datos para limpiar y preparar el conjunto de datos.
- Construir modelos predictivos utilizando algoritmos de Machine Learning.
- Evaluar y seleccionar el mejor modelo basado en métricas de desempeño.
- Implementar técnicas de ajuste de hiperparámetros para optimizar el modelo.
- Desplegar el modelo final en una aplicación web interactiva utilizando Streamlit.

## Metodología

El desarrollo del modelo siguió un enfoque estructurado que incluyó:

1. **Exploración de Datos:** Análisis inicial del conjunto de datos para comprender su estructura y distribución.
2. **Preprocesamiento y Limpieza:** Manejo de valores nulos, normalización y transformación de datos.
3. **Modelado:** Entrenamiento de modelos de Machine Learning para la predicción de la resistencia del cemento.
4. **Evaluación del Modelo:** Uso de métricas como MAE (Mean Absolute Error) y RMSE (Root Mean Squared Error) para medir el desempeño.
5. **Despliegue:** Implementación del modelo en una aplicación web interactiva mediante Streamlit.

## Conjunto de Datos

El dataset utilizado contiene información sobre la composición química del cemento en diferentes lotes, junto con mediciones de su resistencia en distintos días. Sin embargo, el conjunto de datos presentaba un número significativo de valores nulos y una cantidad limitada de registros, lo que impactó en la eficiencia del modelo.

## Resultados

Los modelos entrenados y sus métricas de evaluación fueron:

| Modelo                               | MAE  | RMSE |
| ------------------------------------ | ---- | ---- |
| r1\_iram1622 (RandomForestRegressor) | 1.66 | 2.59 |
| r2\_iram1622 (RandomForestRegressor) | 1.49 | 1.88 |
| r3\_iram1622 (RandomForestRegressor) | 2.16 | 3.05 |
| r7\_iram1622 (CatBoostRegressor)     | 1.75 | 2.19 |
| r28\_iram1622 (CatBoostRegressor)    | 1.42 | 1.81 |

Si bien el desempeño del modelo no fue óptimo debido a las limitaciones del conjunto de datos, los resultados obtenidos son aceptables en función del entrenamiento realizado.


## 📌 Instrucciones para Probar el Modelo  

### 🔹 Opción 1: Ejecutar la Aplicación desde el Ejecutable (`app.exe`)  
> **Recomendado para usuarios sin experiencia en Python**  

1. **Descarga la aplicación desde Google Drive:**  
   👉 [Descargar `app.exe`](https://drive.google.com/drive/folders/1HVEtPPX2jOQ8dWTR4lIZld2GLFH6FEO7?usp=drive_link)  

2. **Extrae los archivos si están comprimidos** (`.zip`).  

3. **Ejecuta `iniciar_app.bat`**  
   - Esto iniciará automáticamente la aplicación en **Streamlit**.  
   - Una ventana del navegador se abrirá con la interfaz.  

---

### 🔹 Opción 2: Ejecutar desde el Código Fuente  
> **Para usuarios con Python instalado**  

**Descargar archivos:**

Descarga los siguientes archivos y carpetas en una misma ubicación en tu PC:
iniciar_app
install_dependencies
Carpeta modelos_guardados
Carpeta graficos_modelo
Instalar dependencias:

Ejecuta install_dependencies (doble clic sobre el archivo).
Esto iniciará la instalación de los paquetes necesarios.
Ejecutar la aplicación:

Una vez finalizada la instalación, ejecuta iniciar_app (doble clic).
Se abrirá una línea de comandos que iniciará un servidor local.
Podrás visualizar la aplicación en Streamlit desde tu navegador.


1.1 **Clona este repositorio:**  
   ```bash
   git clone https://github.com/Chas-kv/Proyect_IAModel_cemento.git
   cd Proyect_IAModel_cemento
1.2 **Crea y activa un entorno virtual**
   ```bash
   python -m venv env
   source env/bin/activate  # En macOS/Linux
   env\Scripts\activate  # En Windows
1.3 **Instala las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
1.4 **Ejecuta la aplicación en streamlit:**
   ```bash
   streamlit run app.py



Esto permitirá visualizar y probar la funcionalidad del modelo en una interfaz web interactiva.

## Conclusión

Este proyecto demuestra la aplicación de técnicas de Machine Learning en la industria de la construcción. A pesar de las limitaciones en los datos, los modelos lograron generar predicciones con un margen de error razonable. En futuras mejoras, se recomienda utilizar un conjunto de datos más amplio y con menos valores nulos para mejorar la precisión del modelo.

---

📌 **Autores:** Kevin Julian Chavarria Olarte\
📌 **Tecnologías utilizadas:** Python, Pandas, Scikit-Learn, CatBoost, RandomForest,xgboost, Streamlit

 
