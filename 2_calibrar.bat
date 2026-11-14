@echo off
chcp 65001 >nul
cd /d "%~dp0"
python calibrar_dbd.py
timeout /t 2 /nobreak >nul