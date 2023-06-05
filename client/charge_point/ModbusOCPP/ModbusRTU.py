from pymodbus.client import ModbusSerialClient as MbClient
##from pymodbus.client import ModbusTcpClient as MbClient
from . import Loggers
class cModbusClient(Loggers.cDebugLogger):

    def __init__(
        self,
##        _method = 'rtu',
        _port = 'COM10',
        _stopbits = 1,
        _bytesize = 8,
        _parity = 'N' ,
        _baudrate = 19200
    ):
        super().__init__()
##        unit_id = int(_unit_id)
        self.client = MbClient( method = 'rtu', 
                                port = _port, 
                                stopbits = 1, 
                                bytesize = 8, 
                                parity = 'N' , 
                                baudrate = _baudrate,
                                timeout = 0.1,
                                strict = False # отключение жесткой паузы ожидания ответа (silent time)
                                )

#TODO сделать деструктор

    def Connect(self):
        if self.client.is_socket_open():
            self.self.Logging('is_socket_open:', self.client.is_socket_open())
            self.Logging('Socket is open. Return')
            return False
        self.client.connect()
        self.Logging('Connect().is_socket_open() - %s' % self.client.is_socket_open())
        return self.client.is_socket_open()

    def IsConnected(self):
        return self.client.is_socket_open()

    def Disconnect(self):
        if self.client.is_socket_open():
            self.client.close()
        self.Logging('Disconnect().is_socket_open() - %s' % self.client.is_socket_open())

    def ReadOneCoil(self, unit_id, reg_addr):
        self.Logging('ReadOneCoil(reg_addr = %d)' % (reg_addr))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)

        rc = self.client.read_coils(reg_addr, 1, slave = unit_id)
        if rc.isError():
            self.Logging('  Error ReadOneCoil(reg_addr = %d)' % reg_addr)
            return (False, None)

        self.Logging('  reg_addr: %d, value: %d' % (reg_addr, rc.bits[0]))
        return (True, rc.bits[0])

    def WriteOneCoil(self, unit_id, reg_addr, value):
        print(f'{__name__}.py WriteOneCoil(\n\t└ {reg_addr=},\n\t└ {value=}),\n\t└ {unit_id=}),\n\t└ {self.client.is_socket_open()=}')
        if not self.client.is_socket_open():
            return False

        rq = self.client.write_coil(reg_addr, value, slave = unit_id)
        print(f'\t└ {str(rq)=}')
        self.Logging('WriteOneCoil(reg_addr = %d, value = %u): %s' %  (reg_addr, value, str(rq)))
        return not rq.isError()

    def ReadMultipleCoils(self, unit_id, reg_addr, regs_count):
        self.Logging('ReadMultipleCoils(reg_addr = %d, regs_count = %d)' % (reg_addr, regs_count))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)

        rc = self.client.read_coils(reg_addr, regs_count, slave = unit_id)
        if rc.isError():
            self.Logging('  Error ReadMultipleCoils(reg_addr = %d)' % reg_addr)
            return (False, None)

        self.Logging('  reg_addr: %d, value: %s' % (reg_addr, rc.bits))
        return (True, rc.bits)

    def ReadOneInput(self, unit_id, reg_addr):
        self.Logging('ReadOneInput(reg_addr = %d)' % (reg_addr))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)

        ri = self.client.read_discrete_inputs(reg_addr, 1, unit = unit_id)
        if ri.isError():
            self.Logging('  Error ReadOneInput(reg_addr = %d)' % reg_addr)
##            self.Logging('  Read error. code = %d' % ri.exception_code)
            return (False, None)

        self.Logging('  reg_addr: %d, value: %d' % (reg_addr, ri.bits[0]))
        return (True, ri.bits[0])

    def ReadMultipleInputs(self, unit_id, reg_addr, regs_count):
        'чтение дискретных входов'
        self.Logging('ReadOneInput(reg_addr = %d, regs_count = %d)' % (reg_addr, regs_count))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)

        ri = self.client.read_discrete_inputs(reg_addr, regs_count, unit = unit_id)
        if ri.isError():
##            self.Logging('  Read error. code = %d' % ri.exception_code)
            self.Logging('  Error ReadMultipleInputs(reg_addr = %d)' % reg_addr)
            return (False, None)

        self.Logging('  reg_addr: %d, value: %s' % (reg_addr, ri.bits))
        return (True, ri.bits)

    def ReadOneHoldingReg(self, unit_id, reg_addr):
        # print(f'{__name__}.py ReadOneHoldingReg:┐\n\t└ {unit_id=}\n\t└ {reg_addr}')
        self.Logging('ReadOneHoldingReg(reg_addr = %d)' % (reg_addr))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)


        rh = self.client.read_holding_registers(reg_addr, 1, unit = unit_id)


        if rh.isError():
            self.Logging('  Error ReadOneHoldingReg(reg_addr = %d)' % reg_addr)
##            self.Logging('  Read error. code = %d' % rh.exception_code)
            return (False, None)
        
        self.Logging('  reg_addr: %d, value: %d' % (reg_addr, rh.registers[0]))
        return (True, rh.registers[0])

    def WriteOneHoldingReg(self, unit_id, reg_addr, value):
        # print(f'{__name__}.py WriteOneHoldingReg:┐\n\t└ {unit_id=}\n\t└ {reg_addr}')
        if not self.client.is_socket_open():
            return False
        rq = self.client.write_register(reg_addr, value, slave = unit_id)
        self.Logging('WriteOneHoldingReg(reg_addr = %d, value = %u): %s' %  (reg_addr, value, str(rq)))
        return not rq.isError()
        

    def ReadMultipleHoldingRegs(self, unit_id, reg_addr, regs_count):
        self.Logging('ReadMultipleHoldingRegs(reg_addr = %d, regs_count = %d)' % (reg_addr, regs_count))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)

        rh = self.client.read_holding_registers(reg_addr, regs_count, slave = unit_id)
        if rh.isError():
            self.Logging('  Error ReadMultipleHoldingRegs(reg_addr = %d)' % reg_addr)
##            self.Logging('  Read error. code = %d' % rh.exception_code)
            return (False, None)
        
        self.Logging('  reg_addr: %d, value: %s' % (reg_addr, rh.registers))
        return (True, rh.registers)

    def WriteMultipleHoldingRegs(self, unit_id, reg_addr, values_list):
        if not self.client.is_socket_open():
            return False
        rq = self.client.write_registers(reg_addr, values_list, unit = unit_id)
        self.Logging('WriteOneHoldingReg(reg_addr = %d, value = %s): %s' %  (reg_addr, str(values_list), str(rq)))
        return not rq.isError()

    def ReadOneInputReg(self, unit_id, reg_addr):
        self.Logging('ReadOneInputReg(reg_addr = %d)' % (reg_addr))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)
        
        ri = self.client.read_input_registers(reg_addr, 1, unit = unit_id)
        if ri.isError():
            self.Logging('  Error ReadOneInputReg(reg_addr = %d)' % reg_addr)
##            self.Logging('  Read error. code = %d' % ri.exception_code)
            return (False, None)
        
        self.Logging('  reg_addr: %d, value: %d' % (reg_addr, ri.registers[0]))
        return (True, ri.registers)

    def ReadMiltipleInputRegs(self, unit_id, reg_addr, regs_count):
        self.Logging('ReadMiltipleInputRegs(reg_addr = %d, regs_count = %d)' % (reg_addr, regs_count))
        if not self.client.is_socket_open():
            self.Logging('  Socket not open!')
            return (False, None)
# address: int, count: int = 1, slave: int = 0, **kwargs: any
        ri = self.client.read_input_registers(address=reg_addr, count=regs_count, slave = unit_id)
        if ri.isError():
            self.Logging('  Error ReadMiltipleInputRegs(reg_addr = %d)' % reg_addr)
##            self.Logging('  Read error. code = %d' % ri.exception_code)
            return (False, None)

        self.Logging('  reg_addr: %d, value: %s' % (reg_addr, ri.registers))
        return (True, ri.registers)

    def __repr__(self):
        res = '\n' + self.__class__.__name__
##        res += '\nIP = ' + str(self.ip)
##        res += '\nport = ' + str(self.port)
##        res += '\nunit_id = ' + str(unit_id)
        res += '\nlog_enable = ' + str(self.log_enable)
        return res


def main():

    ID_ELECTRO_METER = 1
    ID_EVSE = 15
    
    
    print(MbClient)
    modbus = cModbusClient(_port = 'COM11', _baudrate = 19200)
    print(dir(modbus))
    modbus.LoggingSwitch(True)
    print(modbus)
    modbus.Connect()

    print('## ------------- Test read EVSE registers ------------------')
    result, value = modbus.ReadOneCoil(ID_EVSE,0)
    print(f'EVSE ReadOneCoil: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleCoils(ID_EVSE,0, 10)
    print(f'EVSE ReadMultipleCoils: result = {result}, value = {value}')

    result, value = modbus.ReadOneInput(ID_EVSE, 0)
    print(f'EVSE ReadOneInput: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleInputs(ID_EVSE, 0, 10)
    print(f'EVSE ReadMultipleInputs: result = {result}, value = {value}')    

    result, value = modbus.ReadOneHoldingReg(ID_EVSE, 0)
    print(f'EVSE ReadOneHoldingReg: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_EVSE,0, 10)
    print(f'EVSE ReadMultipleHoldingRegs: result = {result}, value = {value}')

    result, value = modbus.ReadOneInputReg(ID_EVSE, 0)
    print(f'EVSE ReadOneInputReg: result = {result}, value = {value}')

    result, value = modbus.ReadMiltipleInputRegs(ID_EVSE,0, 10)
    print(f'EVSE ReadMiltipleInputRegs: result = {result}, value = {value}')

    print('## --------- Test read Electro meter registers ------------')
    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4353, 3)
    print(f'Адрес счетчика: result = {result}, value = {value}')

    result, value = modbus.ReadOneHoldingReg(ID_ELECTRO_METER, 4352)
    print(f'Статус связи: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4353, 3)
    print(f'Адрес счетчика: result = {result}, value = {value}')

    result, value = modbus.ReadOneHoldingReg(ID_ELECTRO_METER,4356)
    print(f'Не используется: result = {result}, value = {value}')

    result, value = modbus.ReadOneHoldingReg(ID_ELECTRO_METER,4357)
    print(f'Ст.-часы, мл.-минуты: result = {result}, value = {value}')

    result, value = modbus.ReadOneHoldingReg(ID_ELECTRO_METER,4358)
    print(f'мл.-секунды: result = {result}, value = {value}')

    result, value = modbus.ReadOneHoldingReg(ID_ELECTRO_METER,4359)
    print(f'Ст.-месяц, мл.-год: result = {result}, value = {value}')

    result, value = modbus.ReadOneHoldingReg(ID_ELECTRO_METER,4360)
    print(f'Ст.-день недели, мл.-число: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4361, 2)
    print(f'Суммарная прямая активная мощность: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4363, 2)
    print(f'Активная мощность фазы А: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4365, 2)
    print(f'Активная мощность фазы B: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4367, 2)
    print(f'Активная мощность фазы C: result = {result}, value = {value}')


    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4369, 2)
    print(f'Ток фазы А: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4371, 2)
    print(f'Ток фазы B: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4373, 2)
    print(f'Ток фазы C: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4375, 2)
    print(f'Напряжение АN: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4377, 2)
    print(f'Напряжение BN: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4379, 2)
    print(f'Напряжение CN: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4381, 2)
    print(f'Частота: result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4383, 2)
    print(f'Энергия активная (потреблен.): result = {result}, value = {value}')

    result, value = modbus.ReadMultipleHoldingRegs(ID_ELECTRO_METER,4385, 2)
    print(f'Энергия активная (отпущен.): result = {result}, value = {value}')

    modbus.Disconnect()

if __name__ == '__main__':
    main()
