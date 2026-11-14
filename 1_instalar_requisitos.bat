@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================================
echo   INSTALANDO LIBRERIAS NECESARIAS...
echo ==========================================================
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo ==========================================================
echo   INSTALACION FINALIZADA
echo ==========================================================
timeout /t 2 /nobreak >nul