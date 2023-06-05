# ls -l /dev - вывести список портов
# Порты, которые нам нужны
# serial0 -> ttyS0 (/dev/ttyS0)
# serial1 -> ttyAMA0 (/dev/ttyAMA0)
# Определение версии ОС
## print(os.name) import os
## print(platform.system()) import platform

import sys

from threading import Thread as th
import time
import struct

import ModbusOCPP.ModbusRegisersHelper as mbrs
import ModbusOCPP.ModbusRegisers as modbus_registers
import ModbusOCPP.Loggers

SERIAL_PORT = ''
if sys.platform == 'win32':
    #SERIAL_PORT = 'COM1'
    SERIAL_PORT = 'COM14'
else:
    #SERIAL_PORT = '/dev/ttyS0'
    SERIAL_PORT = '/dev/serial0'

##------------------------------------------------------------------------------

class cOcppModbus(ModbusOCPP.Loggers.cDebugLogger):
    
    def __init__(self, PORT, BAUD = 19200, on_data_updata_cb = None):
        super().__init__()

        self.mb_regs = mbrs.cModbusRegisers(port = PORT, baudrate = BAUD)
        self.json_logger = ModbusOCPP.Loggers.cJsonLogger()
        self.json_logger.LoggingSwitch(True)
        self.poll_thread_enable = False

        do = ModbusOCPP.ModbusRegisers.DiscreteOutputRegisters
        di = ModbusOCPP.ModbusRegisers.DiscreteInputsRegisters
        hr = ModbusOCPP.ModbusRegisers.HoldingRegisters
        ir = ModbusOCPP.ModbusRegisers.InputRegisters
        self.AddAllRegistersDescription(do, di, hr, ir)
        self.on_data_updata_cb = on_data_updata_cb

    def __del__(self):
        self.Logging('__del__')
        del self.mb_regs
        self.poll_thread_enable = False
        
    def AddAllRegistersDescription(self, do, di, hr, ir):
        self.Logging('AddAllRegistersDescription')
        self.mb_regs.AddDiscreteOutputsRegList(do)
        self.mb_regs.AddDiscreteInputsRegList(di)
        self.mb_regs.AddHoldingRegList(hr)
        self.mb_regs.AddInputsRegList(ir)

    # управляющие сигналы
    def SetChargeEnable(self, _bool):
        if _bool:
            self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_CHARGE_PERMIT)
        else:
            self.mb_regs.ResetDoRegister(modbus_registers.EVSE_CHADEMO_CHARGE_PERMIT)
    def SetResetError(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_RESET_ERROR)
    def SetLogEnable(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_LOGGING_ENABLE)
    def SetCpOn(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_CP_ON)
    def SetCp3On(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_CP3_ON)
    def SetK1On(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_K1_ON)
    def SetLedYelloOn(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_LED_YELLO_ON)
    def SetLedBlueOn(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_LED_BLUE_ON)
    def SetLedRedOn(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_LED_RED_ON)
    def SetK12On(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_K12_ON)
    def SetLockOn(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_LOCK_ON)
    def SetConverter1On(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_CONVETER_1_ON)
    def SetConverter2On(self):
        self.mb_regs.SetDoRegister(modbus_registers.EVSE_CHADEMO_CONVETER_2_ON)


    def SetTestMode(self, val):
        self.mb_regs.WhiteHoldingRegUint16Type(modbus_registers.EVSE_CHADEMO_TEST_MODE_ON, val)
    def SetPower(self, val):
        self.mb_regs.WhiteHoldingRegUint16Type(modbus_registers.EVSE_CHADEMO_SET_POWER_IN_TEST_MODE, val)
    def SetConverter1OutputVoltage(self, val):
        self.mb_regs.WhiteHoldingRegUint16Type(modbus_registers.EVSE_CHADEMO_SET_CONVERTER_1_OUTPUT_VOLTAGE, val)
    def SetConverter1OutputCurrent(self, val):
        self.mb_regs.WhiteHoldingRegUint16Type(modbus_registers.EVSE_CHADEMO_SET_CONVERTER_1_OUTPUT_CURRENT, val)
    def SetConverter2OutputVoltage(self, val):
        self.mb_regs.WhiteHoldingRegUint16Type(modbus_registers.EVSE_CHADEMO_SET_CONVERTER_2_OUTPUT_VOLTAGE, val)
    def SetConverter2OutputCurrent(self, val):
        self.mb_regs.WhiteHoldingRegUint16Type(modbus_registers.EVSE_CHADEMO_SET_CONVERTER_2_OUTPUT_CURRENT, val)


    def IsConnected(self):
        return self.mb_regs.IsConnected()


    def RunPolling(self):
        print('<RunPolling>')
        self.Logging('RunPolling')
        self.poll_thread = th(target = self.PollingProcessThread, daemon = True)
        self.poll_thread_enable = True
        self.poll_thread.start()

    def StopPolling(self):
        self.poll_thread_enable = False

    def GetAllRegistersAsDict(self):
        return self.mb_regs.GetAllRegistrsAsDict()
    def PrintAllRegisters(self):
        regs_dict = self.mb_regs.GetAllRegistrsAsDict()
        result_str = ''
        for key in regs_dict.keys():
            hex_value = regs_dict[key]
            if type(hex_value) == float:
                word_hi = 0
                word_lo = 0
                bs = struct.pack('<f', hex_value)
                word_hi = (int(bs[3])<<8) | int(bs[2])
                word_lo = (int(bs[1]<<8)) | int(bs[0])
                hex_value = hex(word_lo<<16 | word_hi)
                # hex_value = float.hex(hex_value)
            else:
                hex_value = hex(hex_value)
            result_str += f'HEX: {hex_value}; DEC: {str(regs_dict[key])}; DESCR: "{key}"\n'
        return result_str

    def GetDoRegistersAsDict(self):
        return self.mb_regs.GetDiscreteOutputsAsDict()
    def PrintDoRegisters(self):
        regs_dict = self.mb_regs.GetDiscreteOutputsAsDict()
        result_str = ''
        for key in regs_dict.keys():
            result_str += str(regs_dict[key]) + ' - ' + key + '\n'
        return result_str

    def GetDiRegistersAsDict(self):
        return self.mb_regs.GetDiscreteInputsAsDict()
    def PrintDiRegisters(self):
        regs_dict = self.mb_regs.GetDiscreteInputsAsDict()
        result_str = ''
        for key in regs_dict.keys():
            result_str += str(regs_dict[key]) + ' - ' + key + '\n'
        return result_str

    def GetHoldingRegistersAsDict(self):
        return self.mb_regs.GetHoldingRegsAsDict()
    def PrintHoldingRegisters(self):
        regs_dict = self.mb_regs.GetHoldingRegsAsDict()
        result_str = ''
        for key in regs_dict.keys():
            value = '{:.3f}'.format(regs_dict[key])
            result_str += value + ' - ' + key + '\n'
##            result_str += str(regs_dict[key]) + ' - ' + key + '\n'
        return result_str

    def GetInputRegistersAsDict(self):
        return self.mb_regs.GetInputsRegsAsDict()
    def PrintInputRegisters(self):
        regs_dict = self.mb_regs.GetInputsRegsAsDict()
        result_str = ''
        for key in regs_dict.keys():
            value = '{:.3f}'.format(regs_dict[key])
            result_str += value + ' - ' + key + '\n'
##            result_str += str(regs_dict[key]) + ' - ' + key + '\n'
        return result_str

    def PollingProcessThread(self):
        'поток опроса регистров'
        print('<PollingProcessThread start>')
        self.Logging('PollingProcessThread')
        cur_time = time.monotonic()
        self.prev_time = cur_time
        while self.poll_thread_enable:
            output_string = '## -----------------------------------------\n'
            time.sleep(0.1)
##            print('<PollingProcessThread>')

            cur_time = time.monotonic()
            time_diff = (cur_time - self.prev_time)
##            print(f'time_diff: {time_diff}')
            if time_diff > 0.1:
                self.prev_time = cur_time

##                if not self.IsConnected():
##                    self.json_logger.Logging({'Poligon':'not connect'})
##                    continue
##                print(f'cur_time: {cur_time}')
                self.mb_regs.GetAllRegsFromModbus()
                regs_dict = self.mb_regs.GetAllRegistrsAsDict()
##                self.json_logger.Logging(regs_dict)
                if self.on_data_updata_cb != None:
                    self.on_data_updata_cb(regs_dict)
                
                for key in regs_dict.keys():
                    if type(regs_dict[key]) == float:
                        hex_ = struct.pack('<f', regs_dict[key])
                        output_string += f'{type(regs_dict[key])} {key}: {regs_dict[key]}, {hex_}\n'
                    else:
                        output_string += f'{type(regs_dict[key])} {key}: {regs_dict[key]}, {regs_dict[key]:#x}\n'
##                    print(output_string)

##------------------------------------------------------------------------------
def main():

    poligon = cOcppModbus(SERIAL_PORT, None)
    poligon.LoggingSwitch(True)

    # do = ModbusRegisers.DiscreteOutputRegisters
    # di = ModbusRegisers.DiscreteInputsRegisters
    # hr = ModbusRegisers.HoldingRegisters
    # ir = ModbusRegisers.InputRegisters
    # poligon.AddAllRegistersDescription(do, di, hr, ir)
    poligon.RunPolling()

    menu_dict = {}


    KEY_CHARGE_ENABLE = '0'
    COMMENT_CHARGE_ENABLE = 'charge enable'
    menu_dict[KEY_CHARGE_ENABLE] = (COMMENT_CHARGE_ENABLE, poligon.SetChargeEnable)

    KEY_RESET_ERROR = '1'
    COMMENT_RESET_ERROR = 'reset error'
    menu_dict[KEY_RESET_ERROR] = (COMMENT_RESET_ERROR, poligon.SetResetError)

    KEY_LOG_ENABLE = '2'
    COMMENT_LOG_ENABLE = 'log enable'
    menu_dict[KEY_LOG_ENABLE] = (COMMENT_LOG_ENABLE, poligon.SetLogEnable)

    KEY_CP_ON = '3'
    COMMENT_CP_ON = 'CP_ON'
    menu_dict[KEY_CP_ON] = (COMMENT_CP_ON, poligon.SetCpOn)

    KEY_CP3_ON = '4'
    COMMENT_CP3_ON = 'CP3_ON'
    menu_dict[KEY_CP3_ON] = (COMMENT_CP3_ON, poligon.SetCp3On)

    KEY_K1_ON = '5'
    COMMENT_K1_ON = 'K1_ON'
    menu_dict[KEY_K1_ON] = (COMMENT_K1_ON, poligon.SetK1On)

    KEY_LED_YELLO_ON = '6'
    COMMENT_LED_YELLO_ON = 'LED_YELLO_ON'
    menu_dict[KEY_LED_YELLO_ON] = (COMMENT_LED_YELLO_ON, poligon.SetLedYelloOn)

    KEY_LED_BLUE_ON = '7'
    COMMENT_LED_BLUE_ON = 'LED_BLUE_ON'
    menu_dict[KEY_LED_BLUE_ON] = (COMMENT_LED_BLUE_ON, poligon.SetLedBlueOn)

    KEY_LED_RED_ON = '8'
    COMMENT_LED_RED_ON = 'LED_RED_ON'
    menu_dict[KEY_LED_RED_ON] = (COMMENT_LED_RED_ON, poligon.SetLedRedOn)

    KEY_K12_ON = '9'
    COMMENT_K12_ON = 'K12_ON'
    menu_dict[KEY_K12_ON] = (COMMENT_K12_ON, poligon.SetK12On)

    KEY_LOCK_ON = '10'
    COMMENT_LOCK_ON = 'LOCK_ON'
    menu_dict[KEY_LOCK_ON] = (COMMENT_LOCK_ON, poligon.SetLockOn)

    KEY_LED_CONVETER_1_ON = '11'
    COMMENT_CONVETER_1_ON = 'CONVETER_1_ON'
    menu_dict[KEY_LED_CONVETER_1_ON] = (COMMENT_CONVETER_1_ON, poligon.SetConverter1On)

    KEY_CONVETER_2_ON = '12'
    COMMENT_CONVETER_2_ON = 'CONVETER_2_ON'
    menu_dict[KEY_CONVETER_2_ON] = (COMMENT_CONVETER_2_ON, poligon.SetConverter2On)


# ----------------------

    KEY_PRINT_REGS = 'p'
    COMMENT_PRINT_REGS = 'print registers'
    menu_dict[KEY_PRINT_REGS] = (COMMENT_PRINT_REGS, poligon.PrintAllRegisters)

    KEY_PRINT_DO_REGS = 'pdo'
    COMMENT_PRINT_DO_REGS = 'print discrete output registers'
    menu_dict[KEY_PRINT_DO_REGS] = (COMMENT_PRINT_DO_REGS, poligon.PrintDoRegisters)

    KEY_PRINT_DI_REGS = 'pdi'
    COMMENT_PRINT_DI_REGS = 'print discrete inputs registers'
    menu_dict[KEY_PRINT_DI_REGS] = (COMMENT_PRINT_DI_REGS, poligon.PrintDiRegisters)

    KEY_PRINT_HOLD_REGS = 'ph'
    COMMENT_PRINT_HOLD_REGS = 'print discrete inputs registers'
    menu_dict[KEY_PRINT_HOLD_REGS] = (COMMENT_PRINT_HOLD_REGS, poligon.PrintHoldingRegisters)

    KEY_PRINT_INPUT_REGS = 'pi'
    COMMENT_PRINT_INPUT_REGS = 'print discrete inputs registers'
    menu_dict[KEY_PRINT_INPUT_REGS] = (COMMENT_PRINT_INPUT_REGS, poligon.PrintInputRegisters)


    KEY_TEST_MODE = 'test'
    COMMENT_TEST_MODE = 'switch test mode'
    menu_dict[KEY_TEST_MODE] = (COMMENT_TEST_MODE, poligon.SetTestMode)

    KEY_SET_PWR = 'pwr'
    COMMENT_SET_PWR = 'set power'
    menu_dict[KEY_SET_PWR] = (COMMENT_SET_PWR, poligon.SetPower)

    KEY_SET_CONV_1_OUT_VOLT = 'ov1'
    COMMENT_SET_CONV_1_OUT_VOLT = 'set converter 1 out voltage'
    menu_dict[KEY_SET_CONV_1_OUT_VOLT] = (COMMENT_SET_CONV_1_OUT_VOLT, poligon.SetConverter1OutputVoltage)

    KEY_SET_CONV_1_OUT_CURRENT = 'oc1'
    COMMENT_SET_CONV_1_OUT_CURRENT = 'set converter 1 out current'
    menu_dict[KEY_SET_CONV_1_OUT_CURRENT] = (COMMENT_SET_CONV_1_OUT_CURRENT, poligon.SetConverter1OutputCurrent)

    KEY_SET_CONV_2_OUT_VOLT = 'ov2'
    COMMENT_SET_CONV_2_OUT_VOLT = 'set converter 2 out voltage'
    menu_dict[KEY_SET_CONV_2_OUT_VOLT] = (COMMENT_SET_CONV_2_OUT_VOLT, poligon.SetConverter2OutputVoltage)

    KEY_SET_CONV_2_OUT_CURRENT = 'oc2'
    COMMENT_SET_CONV_2_OUT_CURRENT = 'set converter 2 out current'
    menu_dict[KEY_SET_CONV_2_OUT_CURRENT] = (COMMENT_SET_CONV_2_OUT_CURRENT, poligon.SetConverter2OutputCurrent)

    KEY_EXIT = 'q'
    COMMENT_EXIT = 'exit'
    menu_dict[KEY_EXIT] = (COMMENT_EXIT, poligon.StopPolling)

    message = '\nMENU:\n'

    for key in menu_dict.keys():
        comment, func = menu_dict[key]
        message += key + ' - ' + comment + '\n'

    # message += KEY_EXIT + ' - exit\n'

    while True:
        print(message)

        mode = input('Input command:')

        if mode == KEY_CHARGE_ENABLE:
            comment, func = menu_dict[mode]
            func(True)
        if mode == KEY_RESET_ERROR:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_LOG_ENABLE:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_CP_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_CP3_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_K1_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_LED_YELLO_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_LED_BLUE_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_LED_RED_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_K12_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_LOCK_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_LED_CONVETER_1_ON:
            comment, func = menu_dict[mode]
            func()
        if mode == KEY_CONVETER_2_ON:
            comment, func = menu_dict[mode]
            func()


        if mode == KEY_PRINT_REGS:
            print(poligon.PrintAllRegisters())
        elif mode == KEY_PRINT_DO_REGS:
            print(poligon.PrintDoRegisters())
        elif mode == KEY_PRINT_DI_REGS:
            print(poligon.PrintDiRegisters())
        elif mode == KEY_PRINT_HOLD_REGS:
            print(poligon.PrintHoldingRegisters())
        elif mode == KEY_PRINT_INPUT_REGS:
            print(poligon.PrintInputRegisters())

        elif mode == KEY_TEST_MODE:
            poligon.SetTestMode(0x1234)
        elif mode == KEY_SET_PWR:
            poligon.SetPower(20)
        elif mode == KEY_SET_CONV_1_OUT_VOLT:
            poligon.SetConverter1OutputVoltage(30)
        elif mode == KEY_SET_CONV_1_OUT_CURRENT:
            poligon.SetConverter1OutputCurrent(40)
        elif mode == KEY_SET_CONV_2_OUT_VOLT:
            poligon.SetConverter2OutputVoltage(50)
        elif mode == KEY_SET_CONV_2_OUT_CURRENT:
            poligon.SetConverter2OutputCurrent(14)

        elif mode == KEY_EXIT:
            break
        else:
            print('Unknown command:', mode)
        
    poligon.StopPolling()

    print('main thread exit')
##------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
