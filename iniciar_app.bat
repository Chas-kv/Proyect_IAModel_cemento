@echo off
setlocal

:: Verificar si Streamlit ya está corriendo
tasklist | find /i "python.exe" | find /i "streamlit" >nul
if not errorlevel 1 (
    echo La aplicación ya está en ejecución.
    exit /b
)

echo Activando entorno virtual...
cd /d "D:\Inteligencia artifical\Modelo IA Resistencia cemento"
call env_ia\Scripts\activate

echo Iniciando Streamlit...
start "" python -m streamlit run app.py

exit
