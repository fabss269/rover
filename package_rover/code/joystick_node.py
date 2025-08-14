from rclpy.node import Node
import pygame
import constants


class JoystickNode(Node):
    def __init__(self):
        super().__init__("joystick_node")
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            self.get_logger().error("No se detectó ningún mando.")
            return

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        self.get_logger().info(f"Mando detectado: {self.joystick.get_name()}")
        self.get_logger().info(f"Presiona el botón {constants.BTN_ON} (+) para encender el mando (simulación)")

        # Estado inicial
        self.mando_encendido = False
        self.modo = constants.MODE_2X2

        self.timer = self.create_timer(0.1, self.read_joystick)

    def read_joystick(self):
        pygame.event.pump()

        # Si está apagado, solo leer botón ON
        if not self.mando_encendido:
            for i in range(self.joystick.get_numbuttons()):
                if self.joystick.get_button(i) and i == constants.BTN_ON:
                    self.mando_encendido = True
                    self.get_logger().info("Mando encendido (simulación)")
            return

        # Leer botones
        for i in range(self.joystick.get_numbuttons()):
            if self.joystick.get_button(i):
                self.handle_button(i)

        # Leer HAT (D-Pad)
        hat_x, hat_y = self.joystick.get_hat(0)
        self.handle_hat(hat_x, hat_y)

        # Leer Joystick derecho
        axis_rx = self.joystick.get_axis(constants.AXIS_RIGHT_X)
        axis_ry = self.joystick.get_axis(constants.AXIS_RIGHT_Y)
        self.handle_right_joystick(axis_rx, axis_ry)

    def handle_button(self, button_index):
        if button_index == constants.BTN_OFF:
            self.mando_encendido = False
            self.get_logger().info("Mando apagado (simulación)")
            return

        if button_index == constants.BTN_STOP:
            self.get_logger().info("Parada total ejecutada")

        elif button_index == constants.BTN_RESET_WHEELS:
            self.get_logger().info("Reposición de ruedas ejecutada")

        elif button_index == constants.BTN_CHANGE_MODE:
            self.modo = constants.MODE_4X4 if self.modo == constants.MODE_2X2 else constants.MODE_2X2
            self.get_logger().info(f"Cambiado a modo {self.modo}")

        elif self.modo == constants.MODE_4X4:
            if button_index == constants.BTN_TURN_RIGHT:
                self.get_logger().info("Giro horario sobre su propio eje (4x4)")
            elif button_index == constants.BTN_TURN_LEFT:
                self.get_logger().info("Giro antihorario sobre su propio eje (4x4)")

    def handle_hat(self, x, y):
        # Avanzar / retroceder (ambos modos)
        if (x, y) == constants.HAT_UP:
            self.get_logger().info(f"Avanzar en modo {self.modo}")
        elif (x, y) == constants.HAT_DOWN:
            self.get_logger().info(f"Retroceder en modo {self.modo}")

        # Crab lateral (solo 4x4)
        if self.modo == constants.MODE_4X4:
            if (x, y) == constants.HAT_LEFT:
                self.get_logger().info("Crab lateral izquierda (4x4)")
            elif (x, y) == constants.HAT_RIGHT:
                self.get_logger().info("Crab lateral derecha (4x4)")

    def handle_right_joystick(self, rx, ry):
        if self.modo == constants.MODE_2X2:
            if ry < -0.5 and abs(rx) > 0.5:
                self.get_logger().info("Giro con ruedas delanteras (2x2)")
            elif ry > 0.5 and abs(rx) > 0.5:
                self.get_logger().info("Giro con ruedas traseras (2x2)")

        elif self.modo == constants.MODE_4X4:
            if abs(rx) > 0.5 and abs(ry) > 0.5:
                self.get_logger().info("Giro diagonal (4x4)")