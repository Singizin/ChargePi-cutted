# import sys

from threading import Thread as th
import time
# import struct

# from . import Loggers
from . import ModbusRTU
# from . import ModbusRegisersHelper as mb_reg_helper
from . import DeviceBase

# from . import DeviceChademo
# from . import DeviceType2
# from . import DeviceElectroMeter

# PORT = 'COM14'
# # PORT = '/dev/serial0'
# BAUD = 19200
DATA_EXCHANGE_PAUSE = 0.1  # 0.01


class cDeviceDispetcher:
    def __init__(self, modbus_port: str, baud_rate: int) -> None:
        self.list_poll_devs = []

        # self.electro_meter = DeviceElectroMeter.cDeviceElectroMeter()
        # self.AddDeviceForPolling(self.electro_meter)
        # self.hmi = None
        # self.AddDeviceForPolling(self.hmi)
        # self.type2 = DeviceType2.cDeviceType2()
        # self.AddDeviceForPolling(self.type2)
        # self.chademo = DeviceChademo.cDeviceChademo()
        # self.AddDeviceForPolling(self.chademo)
        # self.gb_t = None
        # self.AddDeviceForPolling(self.gb_t)

        self.poll_thread_enable = False

        # self.mb_reg_helper = mb_reg_helper.cModbusRegisers(port = PORT)
        self.modbus_client = ModbusRTU.cModbusClient(_port=modbus_port, _baudrate=baud_rate)
        self.modbus_client.Connect()

    def __del__(self):
        self.poll_thread_enable = False
        self.modbus_client.Disconnect()

    def AddDeviceForPolling(self, dev: DeviceBase.cDeviceBase):
        if dev == None:
            return
        dev.AddModbusPort(self.modbus_client)
        self.list_poll_devs.append(dev)

    def RunPollingDevices(self):
        self.poll_thread = th(target=self.DevicesPollingThread, daemon=True)
        self.poll_thread_enable = True
        self.poll_thread.start()

    # def SetChargeEnable(self, enable: bool):
    #     self.chademo.SetChargeEnable(self.modbus_client, enable)

    def DevicesPollingThread(self):
        dev_counter = 0
        while self.poll_thread_enable:
            # print(f'{__name__}.py ┐')
            time.sleep(DATA_EXCHANGE_PAUSE)

            if dev_counter >= len(self.list_poll_devs):
                dev_counter = 0
            next_poll_dev = self.list_poll_devs[dev_counter]
            dev_counter += 1

            if self.modbus_client.IsConnected() == False:
                self.modbus_client.Connect()

            # else:
            #
            next_poll_dev.ReadAllRegisters()

            # next_poll_dev.PrintAllRegs()

            # print(f'cDeviceDispetcher: {dev_counter}')
