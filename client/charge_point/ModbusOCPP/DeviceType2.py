from . import DeviceBase
from . import Type2Regisers


class cDeviceType2(DeviceBase.cDeviceBase):

    def __init__(self,on_modbus_data_update_cb) -> None:
        super().__init__(on_modbus_data_update_cb)
        self.AddDiRegs(Type2Regisers.DiscreteInputsRegisters)
        self.AddDoRegs(Type2Regisers.DiscreteOutputRegisters)
        self.AddIrRegs(Type2Regisers.InputRegisters)
        self.AddHrRegs(Type2Regisers.HoldingRegisters)
        self.PrintAllRegs()

    def ReadAllRegisters(self) -> bool:
        result_dict = self.GetAllRegistersAsDict()
        prev_mode =  Type2Regisers.EVSE_MODE.current_val

        if super().ReadAllRegisters() == True:
            if prev_mode != Type2Regisers.EVSE_MODE.current_val:
                result_dict = self.GetAllRegistersAsDict()
                result_dict['EVSE_MODE_IS_CHANGED'] = True

        if result_dict:
            self.on_modbus_data_update_cb(result_dict)

        return True

    def UnlockConnector(self) -> bool:
        print(f"{__name__} set_unlock_connector()┐")

        result = self.WriteDoRegValue(Type2Regisers.DO_LOCK, False)

        return result

    def SetChargeEnable(self, value: bool) -> bool:
        return self.WriteDoRegValue(Type2Regisers.DO_CHARGE_ENABLE, value=value)
    
    def GetDeviceCurrentMode(self) -> int:
        mode = self.GetAllRegistersAsDict().get(Type2Regisers.EVSE_MODE.name)
        if mode == None:
            mode = 0
        return mode
