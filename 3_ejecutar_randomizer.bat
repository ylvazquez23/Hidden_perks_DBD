@echo off
chcp 65001 >nul
cd /d "%~dp0"
python dbd_perks_ciegas.py
timeout /t 2 /nobreak >nul