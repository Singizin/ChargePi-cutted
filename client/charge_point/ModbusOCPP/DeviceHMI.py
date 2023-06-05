import ocpp.v16.enums

from . import DeviceBase
from . import HMI_Regisers


class cDeviceHMI(DeviceBase.cDeviceBase):
    KEY_EVT_START_STOP_CMD_TYPE2   = 'EVT_START_STOP_CMD_TYPE2'
    KEY_EVT_START_STOP_CMD_CHADEMO = 'EVT_START_STOP_CMD_CHADEMO'
    KEY_EVT_START_STOP_CMD_GB_T    = 'EVT_START_STOP_CMD_GB_T'

    KEY_PARAM_STATUS  = 'PARAM_STATUS'
    KEY_PARAM_START_STOP_STATUS = 'START_STOP_STATUS'
    KEY_PARAM_START_STOP = 'START_STOP'
    KEY_PARAM_VOLTAGE = 'PARAM_VOLTAGE'
    KEY_PARAM_CURRENT = 'PARAM_CURRENT'
    KEY_PARAM_POWER   = 'PARAM_POWER'
    

    def __init__(self, on_modbus_data_update_cb) -> None:
        super().__init__(on_modbus_data_update_cb)
        self.AddDiRegs(HMI_Regisers.DiscreteInputsRegisters)
        self.AddDoRegs(HMI_Regisers.DiscreteOutputRegisters)
        self.AddIrRegs(HMI_Regisers.InputRegisters)
        self.AddHrRegs(HMI_Regisers.HoldingRegisters)
        self.PrintAllRegs()
        self.InitRegisters()

        self.Type2_Params   = {}
        self.CHAdeMO_Params = {}
        self.GB_T_Params    = {}

    def InitRegisters(self): # TODO нужно переписать так как изменился метод self.WriteHoldingRegValue
        for reg in HMI_Regisers.HoldingRegisters:
            self.WriteHoldingRegValue(reg, 0)

    def SetType2Params(self, type2_params: dict[str, int]):
        # self.Type2_Params.copy(type2_params)
        for key in type2_params.keys():
            self.Type2_Params[key] = type2_params[key]

    def SetGbtParams(self, gb_t_params: dict[str, int]):
        for key in gb_t_params.keys():
            self.GB_T_Params[key] = gb_t_params[key]

    def ReadAllRegisters(self) -> bool:

        result_dict = {}

        start_stop_type2_prev_val = HMI_Regisers.START_STOP_CMD_TYPE2.current_val
        start_stop_chademo_prev_val = HMI_Regisers.START_STOP_CMD_CHADEMO.current_val
        start_stop_gb_t_prev_val = HMI_Regisers.START_STOP_CMD_GB_T.current_val
        get_regs_result = super().ReadAllRegisters()
        
        if get_regs_result == True:
            if start_stop_type2_prev_val != HMI_Regisers.START_STOP_CMD_TYPE2.current_val:
                result_dict[cDeviceHMI.KEY_EVT_START_STOP_CMD_TYPE2] = HMI_Regisers.START_STOP_CMD_TYPE2.current_val

            if start_stop_chademo_prev_val != HMI_Regisers.START_STOP_CMD_CHADEMO.current_val:
                result_dict[cDeviceHMI.KEY_EVT_START_STOP_CMD_CHADEMO] = HMI_Regisers.START_STOP_CMD_CHADEMO.current_val

            if start_stop_gb_t_prev_val != HMI_Regisers.START_STOP_CMD_GB_T.current_val:
                result_dict[cDeviceHMI.KEY_EVT_START_STOP_CMD_GB_T] = HMI_Regisers.START_STOP_CMD_GB_T.current_val

        if result_dict.keys():
            self.on_modbus_data_update_cb(result_dict)

        # запись параметров Type2
        if self.Type2_Params.keys():
            status  = self.Type2_Params.get(cDeviceHMI.KEY_PARAM_STATUS)
            start_stop_status_t2  = self.Type2_Params.get(cDeviceHMI.KEY_PARAM_START_STOP_STATUS)
            voltage = self.Type2_Params.get(cDeviceHMI.KEY_PARAM_VOLTAGE)
            current = self.Type2_Params.get(cDeviceHMI.KEY_PARAM_CURRENT)
            power   = self.Type2_Params.get(cDeviceHMI.KEY_PARAM_POWER)

            if status != None:
                self.WriteHoldingRegValue(HMI_Regisers.AVAIL_STATUS_TYPE2, status)
            if start_stop_status_t2 != None:
                self.WriteHoldingRegValue(HMI_Regisers.START_STOP_STATUS_TYPE2, start_stop_status_t2)
            if voltage != None:
                self.WriteHoldingRegValue(HMI_Regisers.VOLTAGE_TYPE2, voltage)
            if current != None:
                self.WriteHoldingRegValue(HMI_Regisers.CURRENT_TYPE2, current)
            if power != None:
                self.WriteHoldingRegValue(HMI_Regisers.POWER_KWH_TYPE2, power)
        # запись параметров GB/T
        if self.GB_T_Params.keys():
            status  = self.GB_T_Params.get(cDeviceHMI.KEY_PARAM_STATUS)
            start_stop_status_gbt = self.GB_T_Params.get(cDeviceHMI.KEY_PARAM_START_STOP_STATUS)
            voltage = self.GB_T_Params.get(cDeviceHMI.KEY_PARAM_VOLTAGE)
            current = self.GB_T_Params.get(cDeviceHMI.KEY_PARAM_CURRENT)
            power   = self.GB_T_Params.get(cDeviceHMI.KEY_PARAM_POWER)

            if status != None:
                self.WriteHoldingRegValue(HMI_Regisers.AVAIL_STATUS_GB_T, status)
            if start_stop_status_gbt != None:
                self.WriteHoldingRegValue(HMI_Regisers.START_STOP_STATUS_GB_T, start_stop_status_gbt)
            if voltage != None:
                self.WriteHoldingRegValue(HMI_Regisers.VOLTAGE_GB_T, voltage)
            if current != None:
                self.WriteHoldingRegValue(HMI_Regisers.CURRENT_GB_T, current)
            if power != None:
                self.WriteHoldingRegValue(HMI_Regisers.POWER_KWH_GB_T, power)

        return get_regs_result
    