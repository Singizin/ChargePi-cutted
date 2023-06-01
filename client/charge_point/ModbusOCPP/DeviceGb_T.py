from . import DeviceBase
from . import GB_T_Regisers


class cDeviceGbT(DeviceBase.cDeviceBase):

    def __init__(self, on_modbus_data_update_cb) -> None:
        super().__init__(on_modbus_data_update_cb)
        self.AddDiRegs(GB_T_Regisers.DiscreteInputsRegisters)
        self.AddDoRegs(GB_T_Regisers.DiscreteOutputRegisters)
        self.AddIrRegs(GB_T_Regisers.InputRegisters)
        self.AddHrRegs(GB_T_Regisers.HoldingRegisters)
        self.PrintAllRegs()

    def SetChargeEnable(self, value: bool) -> bool:
        return self.WriteDoRegValue(GB_T_Regisers.EVSE_GB_T_CHARGE_PERMIT, value=value)

    def UnlockConnector(self) -> bool:
        print(f"{__name__} set_unlock_connector()┐")
        result = self.WriteDoRegValue(GB_T_Regisers.EVSE_GB_T_LOCK_ON, False)
        return result

    def GetDeviceCurrentMode(self) -> int:
        mode = self.GetAllRegistersAsDict().get(GB_T_Regisers.EVSE_GB_T_MODE.name)
        if mode == None:
            mode = 0
        return mode