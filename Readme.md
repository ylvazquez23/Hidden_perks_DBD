# DBD Blind Perk Randomizer (Reto de Perks Ocultas)

Herramienta en Python para **Dead by Daylight** diseñada para jugar partidas a ciegas sin saber qué ventajas (perks) llevas equipadas y tener que deducirlas durante la partida por sus efectos.

El proyecto automatiza la selección y equipamiento aleatorio de 4 perks en el lobby mediante control de ratón calibrado a tu pantalla, navegando de forma circular por todas las páginas del inventario (`1 <-> 12`) y cerrando el menú al terminar para evitar spoilers.

---

## Estructura del Proyecto

* `calibrar_dbd.py`: Asistente de calibración única (5 puntos) que guarda las coordenadas exactas de tu resolución en `dbd_coords.json`.
* `dbd_perks_ciegas.py`: Script principal que escucha en segundo plano y equipa 4 perks aleatorias al pulsar `0`.
* `generar_pack_oculto.py`: Utilidad opcional para generar en local tu propio pack de iconos ocultos a partir de `token.png`.
* `requirements.txt`: Dependencias necesarias (`pyautogui` y `keyboard`).
* `1_instalar_requisitos.bat`: Instala automáticamente las librerías de Python.
* `2_calibrar.bat`: Ejecuta el calibrador de coordenadas.
* `3_ejecutar_randomizer.bat`: Lanza el randomizer en segundo plano.

---

## Paso 1: Ocultar los iconos de perks con NightLight

Para que no puedas reconocer tus perks por el dibujo en el lobby ni en la esquina inferior derecha durante la partida, instala el pack personalizado creado específicamente para este proyecto usando **NightLight**:

1. Descarga e instala la app de escritorio desde **[nightlight.gg](https://nightlight.gg)** (es segura y está permitida por Behaviour al modificar únicamente archivos visuales locales en `Content/UI/Icons`).
2. Entra en el catálogo de packs de NightLight (**[nightlight.gg/packs](https://nightlight.gg/packs)**) y busca el pack:
   * **Hidden Perks Pack** (por **DeadSuperY**) — Reemplaza todos los iconos de perks por el rombo morado de nivel 3, ocultando por completo qué ventajas llevas equipadas.
   
3. Pulsa **Install** desde NightLight y aplícalo antes de abrir *Dead by Daylight*.

---

## Paso 2: Instalación y Calibración

### Requisitos previos
* **Python 3** instalado en Windows.
* Configurar *Dead by Daylight* en modo **Ventana sin bordes** (*Borderless*) desde los ajustes gráficos (en pantalla completa exclusiva Windows bloquea los clics simulados).

### 1. Instalar dependencias
Ejecuta **`1_instalar_requisitos.bat`** (solo la primera vez).

### 2. Calibrar coordenadas de tu pantalla
1. Abre *Dead by Daylight*, entra en la pestaña **Equipamiento** de Superviviente y sitúate en la **página 2** del inventario (para que sean visibles tanto la flecha `<` como la `>`).
2. Ejecuta **`2_calibrar.bat`**.
3. Coloca el cursor encima de cada uno de los **5 puntos** que pide la consola (sin hacer clic, solo dejando el ratón encima y pulsando `Enter` en la terminal):
   1. Centro de la **primera perk** (arriba a la izquierda).
   2. Centro de la **última perk** de la cuadrícula (fila 3, columna 5).
   3. **Flecha izquierda `<`** (retroceder página).
   4. **Flecha derecha `>`** (avanzar página).
   5. **Botón de cerrar menú** (icono de *Equipamiento* a la izquierda, para retirar el ratón al acabar y cerrar la lista).
4. Se generará el archivo `dbd_coords.json`. No tendrás que repetir este paso salvo que cambies la resolución o la escala de interfaz del juego.

---

## Paso 3: Cómo usar el Randomizer en partida

1. Ejecuta **`3_ejecutar_randomizer.bat`** (recomendable ejecutarlo como Administrador si algún juego bloquea los atajos de teclado globales).
2. En el lobby de *Dead by Daylight*, entra en **Equipamiento** y asegúrate de:
   * **Vaciar los 4 huecos de perks** manualmente (el script no desequipará una build ya puesta).
   * Estar situado en la **Página 1** del inventario.
3. **Aparta la vista de la pantalla** (o cierra los ojos) y pulsa la tecla **`0`**.
4. Oirás un **pitido grave** al empezar, el script navegará por las páginas y equipará 4 perks al azar sin repetir ninguna, cerrará el menú de perks y emitirá un **pitido agudo** al terminar.
5. Pulsa **Listo** sin pasar el cursor por encima de las ranuras de perks para no leer sus nombres.
6. Cuando termines con este procedimiento, pulsa **`9`** para cerrar el programa en segundo plano.

*(Seguridad: Si necesitas abortar el movimiento automático del ratón en cualquier instante, desplaza el cursor de golpe hacia la **esquina superior izquierda** de la pantalla).*

---

## Configuración y Mantenimiento (`dbd_perks_ciegas.py`)

Al principio del archivo `dbd_perks_ciegas.py` puedes ajustar las siguientes variables según tus necesidades o cuando Behaviour añada nuevos personajes:

```python
TOTAL_PAGINAS = 12           # Número total de páginas de perks en tu inventario
PERKS_EN_ULTIMA_PAGINA = 11  # Cantidad de perks reales en la última página (evita huecos vacíos)
LOG = 0                      # 1 = Muestra en consola qué perk-página elige (debug) | 0 = Modo a ciegas# 
