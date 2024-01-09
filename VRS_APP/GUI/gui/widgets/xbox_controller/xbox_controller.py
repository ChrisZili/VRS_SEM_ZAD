import pygame


def get_direction(x, y):
    if abs(x) < 0.1 and abs(y) < 0.1:
        return "Center", 0

    if abs(x) > abs(y):
        if x > 0.5:

            return "Right", x
        elif x < -0.5:
            return "Left", x
    else:
        if y > 0.5:
            return "Down", y
        elif y < -0.5:
            return "Up", y

    return "Neutral", 0


class XboxController():

    def __init__(self, left_joystick_connection,right_joystick_connection):
        self.running = False
        self.left_joystick_connection = left_joystick_connection
        self.right_joystick_connection = right_joystick_connection
        self.joystick_count = 0
        self.controller = None

    def start(self):
        pass

    def get_sign(self, number):
        if "-" in str(number):
            return "-"
        else:
            return "+"

    def calculate_motor_outputs(self,speed, direction):
        """
        Calculate motor outputs based on speed and direction.

        :param speed: Speed value between -100 and 100
        :param direction: Direction value between -100 and 100
        :return: Tuple of two values (motor1, motor2) each between -100 and 100
        """
        # Ensure input values are within the expected range
        speed = max(-100, min(100, speed))
        direction = max(-100, min(100, direction))

        # Basic differential drive formula
        motor1 = speed + direction
        motor2 = speed - direction

        # Ensure output values are within the range -100 to 100
        motor1 = max(-100, min(100, motor1))
        motor2 = max(-100, min(100, motor2))

        return motor1, motor2


    def fill_caracters(self, number, camera=False):
        num = number
        if num is not None:
            if not camera:
                if 20 > num > 0:
                    num = 0
                if -20 < num < 0:
                    num = 0
            if str(num).__len__() == 1:
                sign = self.get_sign(number)
                if sign == "-":
                    return sign + "00" + str(num).replace(sign, "")
                else:

                    return sign +"00" + str(num)
            if str(num).__len__() == 2:
                sign = self.get_sign(num)
                number_str = str(num)
                if sign == "-":
                    return sign + "00" + number_str.replace(sign, "")
                else:
                    return sign+"0" + number_str
            if str(num).__len__() == 3:
                sign = self.get_sign(num)
                if sign == "-":
                    return sign + "0" + str(num).replace(sign, "")
                else:
                    return sign+ str(num)




    def interpret_joystick_value(self, up_down, left_right):
        msg = ""

        helper,helper2 = self.calculate_motor_outputs(left_right*(-100),up_down*100)
        u = self.fill_caracters(round(helper))
        r = self.fill_caracters(round(helper2))
        if u is not None and r is not None:

            msg = "L" + u + "R" + r

        return msg

    def convert_to_camera(self, x, y):
        u = self.fill_caracters(round(x*4), True)
        r = self.fill_caracters(round((y*-4)), True)
        if u is not None and r is not None:
            msg = "X" + u + "Y" + r

            return msg
        # Mapping -1 to 1 to -90 to 90

    def connect(self):
        pygame.init()
        pygame.joystick.init()

        # Check the number of joysticks/controllers connected
        self.joystick_count = pygame.joystick.get_count()
        while self.joystick_count == 0:
            pygame.quit()
            pygame.joystick.quit()
            pygame.init()
            pygame.joystick.init()
            self.joystick_count = pygame.joystick.get_count()
            print("Waiting for joystick connection...")
        if self.joystick_count > 0:
            # Initialize the first joystick
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()

            # Get the number of axes, buttons, and hats
            # num_axes = controller.get_numaxes()
            # num_buttons = controller.get_numbuttons()
            # num_hats = controller.get_numhats()
            #
            # print(f"Number of axes: {num_axes}")
            # print(f"Number of buttons: {num_buttons}")
            # print(f"Number of hats: {num_hats}")
        print("Joystick connected")
    def run(self):


        # Initialize the joystick module
        self.connect()
        self.running = True
        print(f"Number of joysticks connected: {self.joystick_count}")

        # If a controller is connected

        while self.running:
            if pygame.joystick.get_count() == 0:
                print("No joystick detected")
                self.connect()
                # Get the number of axes, buttons, and hats

                #
                # print(f"Number of axes: {num_axes}")
                # print(f"Number of buttons: {num_buttons}")
                # print(f"Number of hats: {num_hats}")
            num_axes = self.controller.get_numaxes()
            num_buttons = self.controller.get_numbuttons()
            num_hats = self.controller.get_numhats()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check joystick events
                if event.type == pygame.JOYAXISMOTION:
                    # Read input from left joystick (axes 0 and 1)
                    left_x = self.controller.get_axis(0)
                    left_y = self.controller.get_axis(1)
                    left_direction, value = get_direction(left_x, left_y)

                    # print(f"Left Joystick - {left_direction} with value {value}%")
                    left_joystick_msg = self.interpret_joystick_value(left_x, left_y)
                    if left_joystick_msg is not None:
                        self.left_joystick_connection(left_joystick_msg)

                    # Read input from right joystick (axes 2 and 3)
                    right_x = self.controller.get_axis(2)
                    right_y = self.controller.get_axis(3)
                    right_direction, value1 = get_direction(right_x, right_y)
                    # print(f"Right Joystick - {right_direction} with value {value1}%")
                    right_joystick_msg = self.convert_to_camera(right_y, right_x)
                    if right_joystick_msg is not None:
                        self.right_joystick_connection(right_joystick_msg)


                if event.type == pygame.JOYBUTTONDOWN:

                    for i in range(num_buttons):
                        button_value = self.controller.get_button(i)
                        if (button_value):
                            print(f"Button {i}: {button_value}")
                            print(event.type)
                        # print(f"Button {i}: {button_value}")

                if event.type == pygame.JOYHATMOTION:

                    for i in range(num_hats):
                        hat_value = controller.get_hat(i)
                        print(f"Hat {i}: {hat_value}")
                elif event.type == pygame.KEYDOWN:
                    print(f"key pressed{event.key}")
