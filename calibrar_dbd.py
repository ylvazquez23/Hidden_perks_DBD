import pyautogui
import json

ARCHIVO_CONFIG = "dbd_coords.json"

def capturar_punto(mensaje):
    input(f"{mensaje} -> Pulsa ENTER en la consola cuando tengas el ratón encima...")
    pos = pyautogui.position()
    print(f"   [OK] Coordenada guardada: ({pos.x}, {pos.y})\n")
    return pos

def ejecutar_calibracion():
    print("==========================================================")
    print("  CALIBRADOR DE COORDENADAS PARA DEAD BY DAYLIGHT")
    print("==========================================================")
    print("Sitúate en la página 2 del inventario (para ver ambas flechas '<' y '>').")
    print("Coloca el cursor encima de cada elemento SIN hacer clic y pulsa ENTER.\n")

    p1 = capturar_punto("1/5. Centro de la PRIMERA perk (arriba a la izquierda)")
    p15 = capturar_punto("2/5. Centro de la ÚLTIMA perk de la cuadrícula (fila 3 col 5)")
    flecha_izq = capturar_punto("3/5. Flecha izquierda '<' (retroceder página)")
    flecha_der = capturar_punto("4/5. Flecha derecha '>' (avanzar página)")
    boton_cerrar = capturar_punto("5/5. Botón que cierra el menú de perks (ej. icono Equipamiento a la izquierda)")

    paso_x = (p15.x - p1.x) / 4.0
    paso_y = (p15.y - p1.y) / 2.0

    grid = []
    for fila in range(3):
        offset_fila = (paso_x * 0.5) if fila == 1 else 0.0
        for col in range(5):
            cx = int(p1.x + col * paso_x + offset_fila)
            cy = int(p1.y + fila * paso_y)
            grid.append([cx, cy])

    datos = {
        "grid": grid,
        "flecha_izq": [flecha_izq.x, flecha_izq.y],
        "flecha_der": [flecha_der.x, flecha_der.y],
        "boton_cerrar": [boton_cerrar.x, boton_cerrar.y]
    }

    with open(ARCHIVO_CONFIG, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

    print("==========================================================")
    print(f"¡Calibración guardada en '{ARCHIVO_CONFIG}'!")
    print("==========================================================")

if __name__ == "__main__":
    ejecutar_calibracion()