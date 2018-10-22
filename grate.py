from serial import Serial


class Grate():
    """
    Class for communication to motor controller on grate.
    """
    position = 0
    serial = None

    def __init__(self, port='', serial=None, position=0):
        """
        Use serial object specified, or create serial object if none passed and
        port is specified.
        """
        if (serial is None and port != ''):
            self.serial = Serial(port)
        else:
            self.serial = serial
        self.position = position

    def set_port(self, port):
        """
        Set serial object to port.
        """
        self.serial = Serial(port)

    def change_position(self, position):
        """
        Change the grate position. Position must be between 100 and 0. 100
        means 100% closed. 0 means 0% closed so the grate is open.
        """
        self.serial.write(position)

    def open(self):
        """
        Opens the grate. Sets position to 0.
        """
        self.change_position(0)

    def close(self):
        """
        Closes the grate. Sets position to 100.
        """
        self.change_position(100)
