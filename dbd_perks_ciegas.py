import pyautogui
import random
import time
import json
import os
import winsound
import keyboard

pyautogui.FAILSAFE = True
ARCHIVO_CONFIG = "dbd_coords.json"
TOTAL_PAGINAS = 12
PERKS_EN_ULTIMA_PAGINA = 11  # En la pág. 12 solo son válidas las 11 primeras (0..10)

# =================================================================
# VARIABLE DE DEBUG / LOG:
#   1 -> Muestra en consola los movimientos de flechas y "perk-pagina"
#   0 -> Modo a ciegas total (no imprime nada de la selección)
# =================================================================
LOG = 0

def escribir_log(mensaje):
    if LOG == 1:
        print(mensaje)

def clic_real(x, y):
    """Movimiento suave + retención de clic de 60ms para que DbD lo registre siempre."""
    pyautogui.moveTo(int(x), int(y), duration=0.08)
    time.sleep(0.03)
    pyautogui.mouseDown()
    time.sleep(0.06)
    pyautogui.mouseUp()
    time.sleep(0.08)

def cargar_config():
    if not os.path.exists(ARCHIVO_CONFIG):
        print(f"[ERROR] No existe '{ARCHIVO_CONFIG}'. Ejecuta primero 'calibrar_dbd.py'.")
        return None
    with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as f:
        return json.load(f)

def ir_a_pagina_aleatoria(datos, pagina_actual):
    """Mueve el inventario usando navegación circular (1 <-> 12) eligiendo siempre el camino más corto."""
    objetivo = random.randint(1, TOTAL_PAGINAS)
    if objetivo == pagina_actual:
        escribir_log(f"   -> Se mantiene en página {pagina_actual}")
        return pagina_actual

    pasos_der = (objetivo - pagina_actual) % TOTAL_PAGINAS
    pasos_izq = (pagina_actual - objetivo) % TOTAL_PAGINAS

    if pasos_der <= pasos_izq:
        escribir_log(f"   -> Moviendo de pág. {pagina_actual} a pág. {objetivo} ({pasos_der} clics '>')")
        for _ in range(pasos_der):
            clic_real(*datos["flecha_der"])
            time.sleep(0.16)
    else:
        escribir_log(f"   -> Moviendo de pág. {pagina_actual} a pág. {objetivo} ({pasos_izq} clics '<')")
        for _ in range(pasos_izq):
            clic_real(*datos["flecha_izq"])
            time.sleep(0.16)

    return objetivo

def asignar_perks_visual():
    datos = cargar_config()
    if not datos:
        winsound.Beep(250, 400)
        return

    winsound.Beep(450, 150)
    escribir_log("\n--- INICIANDO ASIGNACIÓN DE PERKS (desde pág. 1) ---")

    pagina_actual = 1
    grid = datos["grid"]
    usadas = set()

    for ranura in range(1, 5):
        escribir_log(f"\n[Ranura {ranura}/4]")
        pagina_actual = ir_a_pagina_aleatoria(datos, pagina_actual)
        time.sleep(0.2)

        limite_celdas = PERKS_EN_ULTIMA_PAGINA if pagina_actual == TOTAL_PAGINAS else len(grid)
        celdas_validas = [i for i in range(limite_celdas) if (pagina_actual, i) not in usadas]

        elegida = random.choice(celdas_validas)
        usadas.add((pagina_actual, elegida))

        numero_perk = elegida + 1
        escribir_log(f"   -> Perk seleccionada: {numero_perk}-{pagina_actual}")

        px, py = grid[elegida]
        clic_real(px, py)
        time.sleep(0.2)

    # Cierra el menú de equipamiento al finalizar para apartar el ratón y evitar spoilers
    if "boton_cerrar" in datos:
        escribir_log("\n[Fin] Cerrando menú de equipamiento...")
        clic_real(*datos["boton_cerrar"])

    escribir_log("--- ASIGNACIÓN COMPLETADA ---\n")
    winsound.Beep(900, 350)

if __name__ == "__main__":
    if cargar_config():
        print("=================================================================")
        print(f"  DBD RANDOMIZER A CIEGAS - LISTO (MODO LOG = {LOG})")
        print("=================================================================")
        print(" [!] REQUISITOS ANTES DE PULSAR [0]:")
        print("     1. Este script NO quita builds ya puestas: vacía los 4 huecos")
        print("        de perks manualmente antes de activarlo.")
        print("     2. Sitúate en la PÁGINA 1 del inventario antes de pulsar [0]")
        print("        (el script parte siempre desde la página 1).")
        print("-----------------------------------------------------------------")
        print(" -> Pulsa [0] (apartando la vista) para asignar 4 perks al azar.")
        print(" -> Pulsa [9] para cerrar el script.")
        print("=================================================================")

        keyboard.add_hotkey("0", asignar_perks_visual)
        keyboard.wait("9")