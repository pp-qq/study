class UsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugUsbCable(self):
        self.isPlugged = True


class UsbPort:
    def __init__(self):
        self.portAvailable = True

    def plug(self, usbCable):
        if self.portAvailable:
            usbCable.plugUsbCable()
            self.portAvailable = False


# UsbCableは直接UsbPortに接続できる
usbCable = UsbCable()
usbPort1 = UsbPort()
usbPort1.plug(usbCable)


class MicroUsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugMicroUsbCable(self):
        self.isPlugged = True


class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.pulgMicroUsbCable()


# MicroUsbCableはadapterを介してUsbPortに接続できる
microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)
