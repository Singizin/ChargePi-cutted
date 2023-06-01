from . import DeviceBase
from . import ChademoRegisers


class cDeviceChademo(DeviceBase.cDeviceBase):

    def __init__(self, on_modbus_data_update_cb) -> None:
        super().__init__(on_modbus_data_update_cb)
        self.AddDiRegs(ChademoRegisers.DiscreteInputsRegisters)
        self.AddDoRegs(ChademoRegisers.DiscreteOutputRegisters)
        self.AddIrRegs(ChademoRegisers.InputRegisters)
        self.AddHrRegs(ChademoRegisers.HoldingRegisters)
        self.PrintAllRegs()

    def SetChargeEnable(self, value: bool) -> bool:
        return self.WriteDoRegValue(ChademoRegisers.EVSE_CHADEMO_CHARGE_PERMIT, value=value)

    def UnlockConnector(self) -> bool:
        print(f"{__name__} set_unlock_connector()┐")
        result = self.WriteDoRegValue(ChademoRegisers.EVSE_CHADEMO_LOCK_ON, False)
        return result
