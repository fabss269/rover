# Ejes de joystick
AXIS_LEFT_X = 0        # Joystick izq X -> Pan LED
AXIS_LEFT_Y = 1        # Joystick izq Y -> Tilt LED
AXIS_RIGHT_X = 3       # Joystick der X -> Dirección rover / crab lateral
AXIS_RIGHT_Y = 4       # Joystick der Y -> Avance/retroceso rover
AXIS_L2 = 2            # Gatillo izquierdo
AXIS_R2 = 5            # Gatillo derecho

# Botones
BTN_B = 0              # Botón B
BTN_TRIANGLE = 1       # Botón triángulo
BTN_Y = 2              # Botón Y
BTN_X = 3              # Botón X
BTN_R = 4              # Botón R
BTN_L = 5              # Botón L
BTN_MINUS = 6          # Botón "-"
BTN_PLUS = 7           # Botón "+"
BTN_HOME = 8           # Botón casa

# -------------------------
# Asignaciones funcionales
# -------------------------
BTN_STOP = BTN_B                  # Parada total
BTN_RESET_WHEELS = BTN_TRIANGLE   # Reposición de ruedas
BTN_TOGGLE_LED = BTN_Y            # Encender/apagar LED
BTN_CHANGE_MODE = BTN_X           # Cambiar modo 2x2 / 4x4
BTN_TURN_RIGHT = BTN_R            # Giro horario rover (modo 4x4)
BTN_TURN_LEFT = BTN_L             # Giro antihorario rover (modo 4x4)
BTN_OFF = BTN_MINUS               # Apagar mando (simulación)
BTN_ON = BTN_PLUS                 # Encender mando (simulación)

# Hat (D-Pad)
HAT_LEFT = (-1, 0)
HAT_RIGHT = (1, 0)
HAT_UP = (0, 1)
HAT_DOWN = (0, -1)

# Modos
MODE_2X2 = "2x2"
MODE_4X4 = "4x4"
