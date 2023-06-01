from . import ModbusRTU
import struct
from . import Loggers

type_float = 'float'
type_uint16 = 'uint16'
type_uint32 = 'uint32'
type_bool = 'bool'

## тип данных и длина в словах
TypeSize = {
            type_float : 2,
            type_uint16 : 1,
            type_uint32 : 2,
            type_bool : 1
## TODO добавить тип данных - enum 
            }

##------------------------------------------------------------------------------
class cRegisterDescription:
    def __init__(self, unit_id, name, addr, data_type):
        self.unit_id     = unit_id
        self.name        = name
        self.addr        = addr
        self.data_type   = data_type
        self.current_val = 0
        self.reg_len     = TypeSize[data_type]

    def __repr__(self):
        text = ''
        if self.data_type == type_float:
            text = ( 'unit_id: %d, current_val: %f; reg_name: %s; addr: %d; data_type: %s' %
                ( self.unit_id, self.current_val, self.name, self.addr, self.data_type ) )
        else:
            text = ( 'unit_id: %d, current_val: %d; reg_name: %s; addr: %d; data_type: %s' %
                (self.unit_id, self.current_val, self.name, self.addr, self.data_type) )
        
        return text
##------------------------------------------------------------------------------
class cRegistersBase(Loggers.cDebugLogger):
    def __init__(self, modbus_client):
        super().__init__()
        self.modbus_client = modbus_client

    def AddRegistersList(self, reg_list):
        self.reg_list = reg_list

    def GetRegistersAsDict(self):
        result = {}
        for reg in self.reg_list:
#            result[reg.name] = reg.current_val
            result.update({reg.name : reg.current_val})
        return result

    def ConvertRegsToFloat(reg_list):
        word_hi = reg_list[1]
        word_lo = reg_list[0]
        uint32 = word_hi<<16 | word_lo
        uint32_bytes = 0
        try:
            uint32_bytes = struct.pack('I',uint32)
        except Exception as e:
            print('ConvertRegsToFloat Exception:',e, uint32)
            return 0
            
        float32 = struct.unpack('<f', uint32_bytes)[0]
        return float32

    def ConvertFromFloatToRegs(float_value):
        word_hi = 0
        word_lo = 0
        bs = struct.pack('<f', float_value)
        word_hi = (int(bs[3])<<8) | int(bs[2])
        word_lo = (int(bs[1]<<8)) | int(bs[0])
        return (word_lo, word_hi)

    def CheckAddr(self, addr):
        print(f'CheckAddr: {addr}')
        print(self.reg_list)
        for reg in self.reg_list:
            if reg.addr == addr:
                return True
        return False

    def Logging(self, text):
        print('cRegistersBase' + text)
        pass
##------------------------------------------------------------------------------
class cCoils(cRegistersBase):
    def __init__(self, modbus_client):
        super().__init__(modbus_client)
        self.Logging('cCoils.__init__()')

    def SetCoil(self, reg):
        print(f'SetCoil: {reg}')
##        if self.CheckAddr(reg.addr) == True:
        res = self.modbus_client.WriteOneCoil(reg.unit_id, reg.addr, True)
        return res
##        return False

    def ResetCoil(self, reg):
#        if self.CheckAddr(addr) == True:
        return self.modbus_client.WriteOneCoil(reg.unit_id, reg.addr, False)
#        return False

    def GetCoilState(self, addr):
        if self.CheckAddr(addr) == True:
            res, state = self.modbus_client.ReadOneCoil(addr)
            return (res and state)
        return False        

    def GetAllRegisters(self):
        for reg in self.reg_list:
            result, value = self.modbus_client.ReadMultipleCoils(reg.addr, TypeSize[reg.data_type])
            if result == True:
                reg.current_val = value[0]
                
        return self.reg_list
##------------------------------------------------------------------------------
class cInputs(cRegistersBase):
    def __init__(self, modbus_client):
        super().__init__(modbus_client)
        self.Logging('cInputs.__init__()')

    def GetAllRegisters(self):
        for reg in self.reg_list:
            result, value = self.modbus_client.ReadMultipleInputs(reg.addr, TypeSize[reg.data_type])
            if result == True:
                reg.current_val = value[0]
                
        return self.reg_list
##------------------------------------------------------------------------------
class cHoldingRegs(cRegistersBase):
    def __init__(self, modbus_client):
        super().__init__(modbus_client)
        self.Logging('cHoldingRegs.__init__()')

    def WhiteHoldingRegFloatType(self, reg_addr, float_value):
        word_lo, word_hi = cRegistersBase.ConvertFromFloatToRegs(float_value)
        return self.modbus_client.WriteMultipleHoldingRegs(reg.unit_id, reg_addr, [word_lo, word_hi])

    def WhiteHoldingRegUint16Type(self, reg, val):
        print(f'WhiteHoldingRegUint16Type({reg}, {val})')
        result = self.modbus_client.WriteOneHoldingReg(reg.unit_id, reg.addr, val)
        print(f'result: {result}')
        return result

    def GetAllRegisters(self):
        for reg in self.reg_list:
            if reg.data_type == type_float:
                result, value = self.modbus_client.ReadMultipleHoldingRegs(reg.unit_id, reg.addr, TypeSize[reg.data_type])
                if result == True:
                    reg.current_val = cRegistersBase.ConvertRegsToFloat(value)
            if reg.data_type == type_uint32:
                result, value = self.modbus_client.ReadMultipleHoldingRegs(reg.unit_id, reg.addr, TypeSize[reg.data_type])
                if result == True:
                    reg.current_val = value[1]<<16 | value[0] #value
            if reg.data_type == type_uint16:
                result, value = self.modbus_client.ReadMultipleHoldingRegs(reg.unit_id, reg.addr, TypeSize[reg.data_type])
                if result == True:
                    reg.current_val = value[0]
        return self.reg_list
##------------------------------------------------------------------------------
class cInputsRegs(cRegistersBase):
    def __init__(self, modbus_client):
        super().__init__(modbus_client)
        self.Logging('cInputsRegs.__init__()')

    def GetAllRegisters(self):
        for reg in self.reg_list:
            if reg.data_type == type_float:
                result, value = self.modbus_client.ReadMiltipleInputRegs(reg.unit_id, reg.addr, TypeSize[reg.data_type])
                if result == True:
                    reg.current_val = cRegistersBase.ConvertRegsToFloat(value)
            if reg.data_type == type_uint32:
                result, value = self.modbus_client.ReadMiltipleInputRegs(reg.unit_id, reg.addr, TypeSize[reg.data_type])
                if result == True:
                    reg.current_val = value[1]<<16 | value[0]
            if reg.data_type == type_uint16:
                result, value = self.modbus_client.ReadMiltipleInputRegs(reg.unit_id, reg.addr, TypeSize[reg.data_type])
                if result == True:
                    reg.current_val = value[0]
                
        return self.reg_list
##------------------------------------------------------------------------------
class cModbusRegisers(Loggers.cDebugLogger):
    'класс для работы со всеми регистрами'
    def __init__(self,
       port = 'COM1',
       stopbits = 1,
       bytesize = 8,
       parity = 'N' ,
       baudrate = 19200):

        super().__init__()
        self.modbus_client = ModbusOCPP.ModbusRTU.cModbusClient(_port = port, _baudrate = baudrate)
        self.modbus_client.Connect()
        self.coils = cCoils(self.modbus_client)
        self.inputs = cInputs(self.modbus_client)
        self.holdingRegs = cHoldingRegs(self.modbus_client)
        self.inputsRegs = cInputsRegs(self.modbus_client)

    def __del__(self):
        self.modbus_client.Disconnect()

    def IsConnected(self):
        return self.modbus_client.IsConnected()

    def AddDiscreteOutputsRegList(self, do_list):
        self.coils.AddRegistersList(do_list)
    def GetDiscreteOutputsAsDict(self):
        return self.coils.GetRegistersAsDict()

    def AddDiscreteInputsRegList(self, di_list):
        self.inputs.AddRegistersList(di_list)
    def GetDiscreteInputsAsDict(self):
        return self.inputs.GetRegistersAsDict()

    def AddHoldingRegList(self, hr_list):
        self.holdingRegs.AddRegistersList(hr_list)
    def GetHoldingRegsAsDict(self):
        return self.holdingRegs.GetRegistersAsDict()

    def AddInputsRegList(self, ir_list):
        self.inputsRegs.AddRegistersList(ir_list)
    def GetInputsRegsAsDict(self):
        return self.inputsRegs.GetRegistersAsDict()

    def GetAllRegistrsAsDict(self):
        result = self.GetDiscreteOutputsAsDict()
        result.update(self.GetDiscreteInputsAsDict())
        result.update(self.GetHoldingRegsAsDict())
        result.update(self.GetInputsRegsAsDict())
        return result

    def SetDoRegister(self, reg):
        return self.coils.SetCoil(reg)
    def ResetDoRegister(self, reg):
        return self.coils.ResetCoil(reg)
    def GetDoRegisterState(self, addr):
        return self.coils.GetCoilState(addr)

    def WhiteHoldingRegUint16Type(self, reg_addr, uint16_value):
        return self.holdingRegs.WhiteHoldingRegUint16Type(reg_addr, uint16_value)
    def WhiteHoldingRegFloatType(self, reg_addr, float_value):
        return self.holdingRegs.WhiteHoldingRegFloatType(reg_addr, float_value)

    def GetAllRegsFromModbus(self):
        is_connect = self.modbus_client.IsConnected()
        if not is_connect:
            self.modbus_client.Connect()

        regs = self.coils.GetAllRegisters()
        for i in regs:
            self.Logging(' ' + str(i))

        regs = self.inputs.GetAllRegisters()
        for i in regs:
            self.Logging(' ' + str(i))

        regs = self.holdingRegs.GetAllRegisters()
##        print(f'regs: {regs}')
##        for reg in regs:
##            print(f'reg:{reg}')

        regs = self.inputsRegs.GetAllRegisters()
        for i in regs:
            self.Logging(' ' + str(i))
##------------------------------------------------------------------------------

##------------------------------------------------------------------------------
def main():
    import ModbusRegisers

    PORT = 'COM11'
    BAUD = 19200
    UINT_ID = 0x01
##    UINT_ID_EVSE = 0x0F

    modbus_client = ModbusRTU.cModbusClient(_port = 'COM11', _baudrate = 19200)
    modbus_client.Connect()

    reg = cRegisterDescription(UINT_ID, 'name', 1, 'float')
    print(reg)

    coils = cCoils(modbus_client)
    inputs = cInputs(modbus_client)
    holdingRegs = cHoldingRegs(modbus_client)
    inputsRegs = cInputsRegs(modbus_client)
    
    print('\nCoils')
    coils.AddRegistersList(ModbusRegisers.DiscreteOutputRegisters)
    do = coils.GetAllRegisters()
    for o in do:
        print(' ',o)

    print('\nInputs')
    inputs.AddRegistersList(ModbusRegisers.DiscreteInputsRegisters)
    di = inputs.GetAllRegisters()
    for i in di:
        print(' ',i)

    print('\nHoldingRegs')
    holdingRegs.AddRegistersList(ModbusRegisers.HoldingRegisters)
    hr = holdingRegs.GetAllRegisters()
    for i in hr:
        print(' ',i)
##    holdingRegs.WhiteHoldingRegUint16Type(4, 12345)

    print('\ninputsRegs')
    inputsRegs.AddRegistersList(ModbusRegisers.InputRegisters)
    ir = inputsRegs.GetAllRegisters()
    for i in ir:
        print(' ',i)


    modbus_client.Disconnect()

    mbrs = cModbusRegisers(port = 'COM11', baudrate = 19200)
    mbrs.LoggingSwitch(True)

    mbrs.AddDiscreteOutputsRegList(ModbusRegisers.DiscreteOutputRegisters)
    mbrs.AddDiscreteInputsRegList(ModbusRegisers.DiscreteInputsRegisters)
    mbrs.AddHoldingRegList(ModbusRegisers.HoldingRegisters)
    mbrs.AddInputsRegList(ModbusRegisers.InputRegisters)

    mbrs.GetAllRegsFromModbus()

    print('coils.GetRegistersAsDict():', coils.GetRegistersAsDict())
    print('inputs.GetRegistersAsDict():', inputs.GetRegistersAsDict())
    print('holdingRegs.GetRegistersAsDict():', holdingRegs.GetRegistersAsDict())
    print('inputsRegs.GetRegistersAsDict():', inputsRegs.GetRegistersAsDict())

    do = mbrs.GetDiscreteOutputsAsDict()
    print('do',do)
    di = mbrs.GetDiscreteInputsAsDict()
    print('di',di)
    hr = mbrs.GetHoldingRegsAsDict()
    print('hr',hr)
    ir = mbrs.GetInputsRegsAsDict()
    print('ir',ir)

    print(mbrs.GetAllRegistrsAsDict())

    coils.LoggingSwitch(False)


    st = mbrs.GetDoRegisterState(1)
    print('GetDoRegisterState():', st)


    print('mbrs.IsConnected():', mbrs.IsConnected())

if __name__ == '__main__':
    main()
