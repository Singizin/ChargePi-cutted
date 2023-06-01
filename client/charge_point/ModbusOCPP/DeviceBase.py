import operator
from . import ModbusRegisersHelper
from . import ModbusRTU



class cDeviceBase:
    CONN_LOST_CNT_MAX = 10
    MAX_COUNT_REQ_REGS = 124 # максимальное кол-во регистров читаемых за один раз

    def __init__(self, on_modbus_data_update_cb) -> None:
        self.write_holding_list = []
        self.write_do_list = []
        self.connection_lost = False
        self.conncection_lost_cnt = cDeviceBase.CONN_LOST_CNT_MAX
        self.di_regs = None
        self.do_regs = None
        self.ir_regs = None
        self.hr_regs = None
        self.on_modbus_data_update_cb = on_modbus_data_update_cb
        self.modbus_port = None

    # метод для переопределения в потомках
    def SetChargeEnable(self, value: bool) -> bool:
        return False
    # метод для переопределения в потомках
    def UnlockConnector(self) -> bool:
        return False

    def AddModbusPort(self, modbus_port: ModbusRTU.cModbusClient):
        self.modbus_port = modbus_port

    def GetTightRegisters(registers_list: list[ModbusRegisersHelper.cRegisterDescription]):
        ''' возвращает списки регистров, идущие друг за другом '''

        soreted_registers_list = sorted(registers_list, key=operator.attrgetter('addr'))

        result = []
        regs_tight_list = []
        for ir in soreted_registers_list:

            if len(regs_tight_list) == 0:
                next_addr = ir.addr + ir.reg_len
                regs_tight_list.append(ir)
                continue

            if ir.addr == next_addr:
                regs_tight_list.append(ir)
                next_addr = ir.addr + ir.reg_len
            else: # разделение если регистры идут не друг за другом
                result.append(regs_tight_list.copy())
                regs_tight_list.clear()
            # разделение списка по максиальному количеству запрашиваемых по Modbus байт
            min, max, size = cDeviceBase.GetMaxMinSizeOfRegsList(regs_tight_list)
            if size >= cDeviceBase.MAX_COUNT_REQ_REGS:
                result.append(regs_tight_list.copy())
                regs_tight_list.clear()

        result.append(regs_tight_list.copy())

        return result

    def GetMaxMinSizeOfRegsList(registers_list: list[ModbusRegisersHelper.cRegisterDescription]):
        if len(registers_list) == 0:
            return 0,0,0
        min = registers_list[0].addr
        max = min
        size = 0
        for reg in registers_list:
            size += reg.reg_len
            if reg.addr < min:
                min = reg.addr
            if reg.addr > max:
                max = reg.addr
        # print(f'min:{min}, max:{max}, diff:{size_bytes}')
        return (min, max, size)

    def GetRegistersAsDict(self, regs: list[ModbusRegisersHelper.cRegisterDescription]) -> dict[str,int]:
        regs_dict = {}
        if regs:
            for reg in regs:
                regs_dict[reg.name] = reg.current_val
        return regs_dict
    def GetAllRegistersAsDict(self) -> dict[str,int]:
        regs_dict = {}
        regs_dict.update(self.GetRegistersAsDict(self.di_regs))
        regs_dict.update(self.GetRegistersAsDict(self.do_regs))
        regs_dict.update(self.GetRegistersAsDict(self.ir_regs))
        regs_dict.update(self.GetRegistersAsDict(self.hr_regs))
        return regs_dict

    def AddDiRegs(self, di_regs: list[ModbusRegisersHelper.cRegisterDescription]):
        self.di_regs = di_regs
    def GetDiRegs(self) -> list[ModbusRegisersHelper.cRegisterDescription]:
        return self.di_regs

    def AddDoRegs(self, do_regs: list[ModbusRegisersHelper.cRegisterDescription]):
        self.do_regs = do_regs
        self.do_tight_reglist = cDeviceBase.GetTightRegisters(self.do_regs)
    def GetDoRegs(self) -> list[ModbusRegisersHelper.cRegisterDescription]:
        return self.do_regs

    def AddIrRegs(self, ir_regs: list[ModbusRegisersHelper.cRegisterDescription]):
        self.ir_regs = ir_regs
        self.ir_tight_reglist = cDeviceBase.GetTightRegisters(self.ir_regs)
    def GetIrRegs(self) -> list[ModbusRegisersHelper.cRegisterDescription]:
        return self.ir_regs

    def AddHrRegs(self, hr_regs: list[ModbusRegisersHelper.cRegisterDescription]):
        self.hr_regs = hr_regs
        self.hr_tight_reglist = cDeviceBase.GetTightRegisters(self.hr_regs)
    def GetHrRegs(self) -> list[ModbusRegisersHelper.cRegisterDescription]:
        return self.hr_regs

    def ReadDiRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
        di_regs = self.GetDiRegs()
        for r in di_regs:
            result, data = port.ReadOneInput(r.unit_id, r.addr, 2)
            if result == False:
                return False
        return True

    def WriteDoRegValue(self, do_reg: ModbusRegisersHelper.cRegisterDescription, value: bool) -> bool:
        ''' добавляет coil(DO) регистр в очередь на запись '''
        if self.modbus_port == None:
            return False
        if self.connection_lost == True:
            return False

        if value == True:
            do_reg.current_val = 1
        else:
            do_reg.current_val = 0
        self.write_do_list.append(do_reg)

        return True

    def ReadDoRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
        return self.ReadAllTightDoRegisters(port)
        # do_regs = self.GetDoRegs()
        # for r in do_regs:
        #     res, data = port.ReadOneCoil(r.unit_id, r.addr)
        #     if res == False:
        #         return False
        # return True
    def ReadAllTightDoRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
        ''' читает ргистры пачкой одним запросом '''
        for tr in self.do_tight_reglist:
            start_addr, last_addr, size = cDeviceBase.GetMaxMinSizeOfRegsList(tr)
            if size != 0:
                data_received, data = port.ReadMultipleCoils(tr[0].unit_id, start_addr, size)
                data_index = 0
                if data_received == True:
                    for r in tr:
                        if r.data_type == ModbusRegisersHelper.type_uint16:
                            r.current_val = data[data_index]
                        elif r.data_type == ModbusRegisersHelper.type_uint32:
                            r.current_val = (data[data_index+1]<<16) | data[data_index]
                        elif r.data_type == ModbusRegisersHelper.type_float:
                            r.current_val = ModbusRegisersHelper.cRegistersBase.ConvertRegsToFloat( [data[data_index], data[data_index+1]] )
                        data_index += r.reg_len
                else:
                    return False
        return True

    def ReadInputRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
        return self.ReadAllTightInputRegisters(port)
        # ir_regs = self.GetIrRegs()
        # for r in ir_regs:
        #     port.ReadMiltipleInputRegs(r.unit_id, r.addr, 2)
    def ReadAllTightInputRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
        ''' читает ргистры пачкой одним запросом '''
        for tr in self.ir_tight_reglist:
            start_addr, last_addr, size = cDeviceBase.GetMaxMinSizeOfRegsList(tr)
            if size != 0:
                data_received, data = port.ReadMiltipleInputRegs(tr[0].unit_id, start_addr, size)
                data_index = 0
                if data_received == True:
                    for r in tr:
                        if r.data_type == ModbusRegisersHelper.type_uint16:
                            r.current_val = data[data_index]
                        elif r.data_type == ModbusRegisersHelper.type_uint32:
                            r.current_val = (data[data_index+1]<<16) | data[data_index]
                        elif r.data_type == ModbusRegisersHelper.type_float:
                            r.current_val = ModbusRegisersHelper.cRegistersBase.ConvertRegsToFloat( [data[data_index], data[data_index+1]] )
                        data_index += r.reg_len
                else:
                    return False
        return True

    def WriteHoldingRegValue(self, holding_reg: ModbusRegisersHelper.cRegisterDescription, value: int) -> bool:
        ''' добавляет holding регистр в очередь на запись '''
        if self.modbus_port == None:
            return False
        if self.connection_lost == True:
            return False

        holding_reg.current_val = value
        self.write_holding_list.append(holding_reg)

        return True

    def ReadHoldingRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
        return self.ReadAllTightHoldingRegisters(port)
        # hr_regs = self.GetHrRegs()
        # for r in hr_regs:
        #     port.ReadMultipleHoldingRegs(r.unit_id, r.addr, 2)
    def ReadAllTightHoldingRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
        ''' читает ргистры пачкой одним запросом '''
        for tr in self.hr_tight_reglist:
            start_addr, last_addr, size = cDeviceBase.GetMaxMinSizeOfRegsList(tr)
            if size != 0:
                data_received, data = port.ReadMultipleHoldingRegs(tr[0].unit_id, start_addr, size)
                data_index = 0
                if data_received == True:
                    for r in tr:
                        if r.data_type == ModbusRegisersHelper.type_uint16:
                            r.current_val = data[data_index]
                        elif r.data_type == ModbusRegisersHelper.type_uint32:
                            r.current_val = (data[data_index+1]<<16) | data[data_index]
                        elif r.data_type == ModbusRegisersHelper.type_float:
                            r.current_val = ModbusRegisersHelper.cRegistersBase.ConvertRegsToFloat( [data[data_index], data[data_index+1]] )
                        data_index += r.reg_len
                else:
                    return False
        return True

    # def ReadAllRegisters(self, port: ModbusRTU.cModbusClient) -> bool:
    def ReadAllRegisters(self) -> bool:
        port = self.modbus_port
        if port == None:
            return False
        if port.IsConnected() == False:
            return False
        if self.connection_lost == True:
            if self.conncection_lost_cnt > 0:
                self.conncection_lost_cnt -= 1
                return False
            else:
                self.conncection_lost_cnt = cDeviceBase.CONN_LOST_CNT_MAX

        while len(self.write_holding_list) > 0:
            reg = self.write_holding_list.pop()
            port.WriteOneHoldingReg(unit_id=reg.unit_id, reg_addr=reg.addr, value=reg.current_val)

        while len(self.write_do_list) > 0:
            reg = self.write_do_list.pop()
            port.WriteOneCoil(unit_id=reg.unit_id, reg_addr=reg.addr, value=reg.current_val)

        di_read_res = self.ReadDiRegisters(port)
        # do_read_res = self.ReadDoRegisters(port) # дискретные выходы в контроллерах не читаются
        ir_read_res = self.ReadInputRegisters(port)
        hr_read_res = self.ReadHoldingRegisters(port)

        # self.connection_lost = not (di_read_res &  ir_read_res & hr_read_res)
        self.connection_lost = (not di_read_res) & (not ir_read_res) & (not hr_read_res)
        if self.connection_lost == True:
            pass

        if di_read_res == True:
            regs_dict = {}
            # print(f'{__name__}.py ReadAllRegisters(DI)┐')
            for reg in self.di_regs:
                # print(f'\t└{reg.name=} {reg.addr=} {reg.current_val=}')
                regs_dict[reg.name] = reg.current_val
            self.on_modbus_data_update_cb(regs_dict)
        if ir_read_res == True:
            regs_dict = {}
            # print(f'{__name__}.py ReadAllRegisters(IR)┐')
            for reg in self.ir_regs:
                # print(f'\t└{reg.name=} {reg.addr=} {reg.current_val=}')
                regs_dict[reg.name] = reg.current_val
            self.on_modbus_data_update_cb(regs_dict)
        if hr_read_res == True:
            regs_dict = {}
            # print(f'{__name__}.py ReadAllRegisters(HR)┐')
            for reg in self.hr_regs:
                # print(f'\t└{reg.name=} {reg.addr=} {reg.current_val=}')
                regs_dict[reg.name] = reg.current_val
            self.on_modbus_data_update_cb(regs_dict)

        return not self.connection_lost


    def PrintAllRegs(self):
        cDeviceBase.PrintRegisters(self.di_regs)
        cDeviceBase.PrintRegisters(self.do_regs)
        cDeviceBase.PrintRegisters(self.ir_regs)
        cDeviceBase.PrintRegisters(self.hr_regs)

    def PrintRegisters(regs: list[ModbusRegisersHelper.cRegisterDescription]):
        for r in regs:
            # print(r)
            pass