from . import DeviceBase
from . import ElectroMeterRegisers

class cDeviceElectroMeter(DeviceBase.cDeviceBase):

    def __init__(self, on_modbus_data_update_cb) -> None:
        super().__init__(on_modbus_data_update_cb)
        self.AddDiRegs(ElectroMeterRegisers.DiscreteInputsRegisters)
        self.AddDoRegs(ElectroMeterRegisers.DiscreteOutputRegisters)
        self.AddIrRegs(ElectroMeterRegisers.InputRegisters)
        self.AddHrRegs(ElectroMeterRegisers.HoldingRegisters)
        self.PrintAllRegs()