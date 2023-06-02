import json
import random
from datetime import datetime
from typing import TYPE_CHECKING, Union

import ocpp.v16.enums as enums
from ocpp.v16 import call

from charge_point.ModbusOCPP import DevicesDispetcher
from charge_point.ModbusOCPP.DeviceChademo import cDeviceChademo
from charge_point.ModbusOCPP.DeviceType2 import cDeviceType2
from charge_point.ModbusOCPP.DeviceHMI import cDeviceHMI

from . import Type2Regisers as Typ2Regs
from charge_point.ModbusOCPP.DeviceElectroMeter import cDeviceElectroMeter
from charge_point.ModbusOCPP import ElectroMeterRegisers as ElMeterRegs
from charge_point.ModbusOCPP import HMI_Regisers
from charge_point.ModbusOCPP import ModbusDict as md

from .DeviceGb_T import cDeviceGbT
from . import GB_T_Regisers as GbTRegs

#from backend
if TYPE_CHECKING:
    from charge_point.v16.ChargePoint16 import ChargePointV16
    from charge_point.v16.connector_v16 import ConnectorV16


class Modbus:
    def __init__(self, modbus_param):
        self.from_micro = md.from_micro
        self.cp: Union['ChargePointV16', None] = None
        self.emulate_mode = modbus_param[0]
        self.SERIAL_PORT = modbus_param[1]
        self.BAUD = modbus_param[2]

    def set_cp(self, cp: 'ChargePointV16'):
        self.cp : 'ChargePointV16' = cp

        self.hmi = None
        # self.gb_t = None
        self.evse_dispetcher = DevicesDispetcher.cDeviceDispetcher(self.SERIAL_PORT, self.BAUD)

        self.type2 = cDeviceType2(self.on_type2_data_update)
        self.evse_dispetcher.AddDeviceForPolling(self.type2)

        self.chademo = cDeviceChademo(self.on_chademo_data_update)
        self.evse_dispetcher.AddDeviceForPolling(self.chademo)

        self.electro_meter = cDeviceElectroMeter(self.on_electro_meter_data_update)
        self.evse_dispetcher.AddDeviceForPolling(self.electro_meter)

        self.gb_t = cDeviceGbT(self.on_gb_t_data_update)
        self.evse_dispetcher.AddDeviceForPolling(self.gb_t)

        self.hmi = cDeviceHMI(self.on_hmi_data_update)
        self.evse_dispetcher.AddDeviceForPolling(self.hmi)

        self.devices = {
            # TODO: Почему на STEVE коннектор только 2 для UNLOCK
            1: self.type2,
            2: self.chademo,
            3: self.gb_t,
        }

        if self.emulate_mode:
            pass
        else:
            self.evse_dispetcher.RunPollingDevices()

        self.transaction_id_cnt = 0

    def set_connectors(self, connectors: list['ConnectorV16']):
        self.connectors = connectors
        print(f'mmm {__name__} {self.connectors}')

    def print_state(self):
        print(self.__dict__)

    def get_value(self, connector_id, key):
        print(f'get_value {connector_id=}, {key=}')
        return self.from_micro.get(connector_id).get(key)

    def get_meter_values_payload(self,
                                 connector_id: int = 0) -> list[dict]:
        """
        TODO: перенести все эти ключи в ocpp? всё равно там их распоковыю.
        Или же тут их отдавать правильным словарем
        """
        keys = [md.POWER_ACTIVE_IMPORT,
                md.CURRENT_IMPORT,
                md.VOLTAGE,
                md.SOC]

        result = []
        for key in keys:
            result.append({'timestamp': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z",
                           'sampledValue': [
                               {'value': str(self.from_micro.get(connector_id).get(key)),
                                'measurand': key}]})
        return result

    # def to_enum(self,
    #             enum: Enum,
    #             value: int):
    #     return list(enum[value])

    def write_by_data(self, reg, reg_name, value):
        print(f'{__name__}.py write_by_data:\n\t└ {reg=}\n\t└ {reg_name=}\n\t└ {value=}')

        self.type2.set_coil(reg["unit_id"], reg["addr"], value)
        self.type2.set_holding()


    def write_change_availability(self,
                                  availability_type: enums.AvailabilityType,
                                  connector_id: int):
        device = self.devices[connector_id]
        
        if availability_type == enums.AvailabilityType.operative:
            Availability = True
        elif availability_type == enums.AvailabilityType.inoperative:
            Availability = False

        

    def write_unlock_connector(self,
                               connector_id: int):
        device = self.devices[connector_id]

        if device.UnlockConnector() == True:
            status = enums.UnlockStatus.unlocked.value
        else:
            status = enums.UnlockStatus.unlock_failed.value
        print(f"{__name__} write_unlock_connector: {device=}; status: {status}")
        return status

    def write_charge_enable(self, 
                            connector_id: int,
                            value: bool):
        device = self.devices[connector_id]
        print(f"{__name__} write_charge_enable\n\t└{device=}")

        result = device.SetChargeEnable(value)

        if result:
            status = enums.RemoteStartStopStatus.accepted.value
        else:
            status = enums.RemoteStartStopStatus.rejected.value

        return status



    def write_reset(self, reset_type: enums.ResetType):
        if reset_type == enums.ResetType.soft:
            # print('soft restart')
            pass
        elif reset_type == enums.ResetType.hard:
            # print('hard restart')
            pass

    def write_availability_status(self,
                                  payload: call.ChangeAvailabilityPayload,
                                  connector_id: int):
        print(payload, connector_id)
        pass

    def callback_start_transaction(self, connector_id: int):
        return
        self.cp.send_start_transaction_sync(connector_id)

    def callback_handle_charging_request(self, connector_id: int):
        return
        self.cp.handle_charging_request_sync(connector_id)

    def callback_stop_transaction(self, connector_id: int):
        return
        self.cp.send_stop_transaction(connector_id)

    def callback_status_notification(self, connector_id: int):
        return
        if self.cp:
            self.cp.send_status_notification_sync(connector_id)

    def on_modbus_data_update(self, modbus_data: dict[str, int]):
        self.Connector0_DataFill(modbus_data)
        self.on_type2_data_update(modbus_data)
        self.on_chademo_data_update(modbus_data)
        self.on_electro_meter_data_update(modbus_data)

    def Connector0_DataFill(self, modbus_data: dict[str, int]):

        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.POWER_ACTIVE_IMPORT] = str(random.randint(100,200))
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CHARGE_POINT_MODEL]  = 'MODEL_NSTU' # 'CHAdeMO'
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.SOC]                 = str(modbus_data['ID_102_CHARGED_RATE']) # уровень заряда
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CURRENT_IMPORT]      = str(modbus_data['ID_109_PRESENT_CHARGING_CURRENT'])
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.VOLTAGE]             = str(modbus_data['ID_109_PRESENT_OUTPUT_VOLTAGE'])

        # mode = modbus_data['EVSE_CHADEMO_MODE']
        # charge_point_status = enums.ChargePointStatus.unavailable
        # if mode == 0: #   EVSE_STATE_NONE = 0,
        #     charge_point_status = enums.ChargePointStatus.unavailable

        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CHARGE_POINT_STATUS] = charge_point_status

        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CHARGE_POINT_ERROR_CODE]    = enums.ChargePointErrorCode.noError # : ocpp.v16.enums.ChargePointErrorCode.noError.value,
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.AVAILABILITY_TYPE]          = enums.AvailabilityType.operative # : ocpp.v16.enums.AvailabilityType.operative.value,
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CHANGE_AVAILABILITY_STATUS] = enums.AvailabilityStatus.accepted # : ocpp.v16.enums.AvailabilityStatus.accepted.value,
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.ID_TAG]                     = '1'
        # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.TRANSACTION_ID]             = str(self.transaction_id_cnt)
        self.transaction_id_cnt += 1

    def on_type2_data_update(self, modbus_data: dict[str, int]):
        if len(modbus_data) == 0:
            return

        modbus_mode = modbus_data.get(Typ2Regs.EVSE_MODE.name)
        if modbus_data.get('EVSE_MODE_IS_CHANGED'):
            # modbus_mode = modbus_data.get(Typ2Regs.EVSE_MODE.name)

            ocpp_status = enums.ChargePointStatus.unavailable
            if modbus_mode == 0: # EVSE_STATE_NONE         = 0,
                ocpp_status = enums.ChargePointStatus.available
            if modbus_mode == 1: # EVSE_STATE_NOT_CONNECT  = 1,
                ocpp_status = enums.ChargePointStatus.available
            if modbus_mode == 2: # EVSE_STATE_CONNECT      = 2,
                ocpp_status = enums.ChargePointStatus.preparing
            if modbus_mode == 3: # EVSE_STATE_PWM_ON       = 3,
                ocpp_status = enums.ChargePointStatus.preparing
            if modbus_mode == 4: # EVSE_STATE_EV_S2_ON     = 4,
                ocpp_status = enums.ChargePointStatus.preparing
                # self.callback_handle_charging_request(1) # TODO переделать это костыль
            if modbus_mode == 5: # EVSE_STATE_CONTACTOR_ON = 5,
                ocpp_status = enums.ChargePointStatus.charging
            if modbus_mode == 6: # EVSE_STATE_ERROR        = 6,
                ocpp_status = enums.ChargePointStatus.faulted
            if modbus_mode == 7: # EVSE_STATE_TEST         = 7
                ocpp_status = enums.ChargePointStatus.unavailable

            md.from_micro[md.CONNECTOR_1][md.CHARGE_POINT_STATUS] = ocpp_status

            print(f'type2_modbus_mode: {modbus_data.get(Typ2Regs.EVSE_MODE.name)}')
            print(f'type2_ocpp_status: {ocpp_status}')

            self.callback_status_notification(1)

        md.from_micro[md.CONNECTOR_1][md.POWER_ACTIVE_IMPORT] = str(modbus_data.get(Typ2Regs.KEY_EVSE_POWER))
        md.from_micro[md.CONNECTOR_1][md.CHARGE_POINT_MODEL]  = 'MODEL_TYPE_2'
        md.from_micro[md.CONNECTOR_1][md.SOC]                 = str(0) # уровень заряда
        md.from_micro[md.CONNECTOR_1][md.CURRENT_IMPORT]      = str(0)
        md.from_micro[md.CONNECTOR_1][md.VOLTAGE]             = str(0)


        md.from_micro[md.CONNECTOR_1][md.CHARGE_POINT_ERROR_CODE]    = enums.ChargePointErrorCode.noError # : ocpp.v16.enums.ChargePointErrorCode.noError.value,
        md.from_micro[md.CONNECTOR_1][md.AVAILABILITY_TYPE]          = enums.AvailabilityType.operative # : ocpp.v16.enums.AvailabilityType.operative.value,
        md.from_micro[md.CONNECTOR_1][md.CHANGE_AVAILABILITY_STATUS] = enums.AvailabilityStatus.accepted # : ocpp.v16.enums.AvailabilityStatus.accepted.value,
        md.from_micro[md.CONNECTOR_1][md.ID_TAG]                     = '1'
        md.from_micro[md.CONNECTOR_1][md.TRANSACTION_ID]             = str(self.transaction_id_cnt)
        self.transaction_id_cnt += 1

        hmi_params = {}
        if modbus_mode == 5: # зарядка
            hmi_params[cDeviceHMI.KEY_PARAM_STATUS]  = 0
            hmi_params[cDeviceHMI.KEY_PARAM_START_STOP] = 1
        else: # доступен
            hmi_params[cDeviceHMI.KEY_PARAM_STATUS]  = 2
            hmi_params[cDeviceHMI.KEY_PARAM_START_STOP] = 0
        
        self.hmi.SetType2Params(hmi_params)


    def on_chademo_data_update(self, modbus_data: dict[str, int]):
        """Обновляет значения регистров в словаре from_micro по полученным modbus_data
        """
        if len(modbus_data) == 0:
            return

        md.from_micro[md.CONNECTOR_2][md.POWER_ACTIVE_IMPORT] = str(modbus_data['EVSE_CHADEMO_EVSE_POWER'])
        md.from_micro[md.CONNECTOR_2][md.CHARGE_POINT_MODEL]  = 'MODEL_CHAdeMO'
        md.from_micro[md.CONNECTOR_2][md.SOC]                 = str(modbus_data['ID_102_CHARGED_RATE']) # уровень заряда
        md.from_micro[md.CONNECTOR_2][md.CURRENT_IMPORT]      = str(modbus_data['ID_109_PRESENT_CHARGING_CURRENT'])
        md.from_micro[md.CONNECTOR_2][md.VOLTAGE]             = str(modbus_data['ID_109_PRESENT_OUTPUT_VOLTAGE'])

        mode = modbus_data['EVSE_CHADEMO_MODE']
        charge_point_status = enums.ChargePointStatus.unavailable
        if mode == 0: #   EVSE_STATE_NONE = 0,
            charge_point_status = enums.ChargePointStatus.unavailable
        elif mode == 1: #   EVSE_STATE_NOT_CONNECT,
            charge_point_status = enums.ChargePointStatus.available
        elif mode == 2: #   EVSE_STATE_CONNECT,
            charge_point_status = enums.ChargePointStatus.preparing
        elif mode == 3: #   EVSE_STATE_CP_ON,
            charge_point_status = enums.ChargePointStatus.preparing
        elif mode == 4: #   EVSE_STATE_CAN_BEGIN,
            charge_point_status = enums.ChargePointStatus.preparing
        elif mode == 5: #   EVSE_STATE_CP2_ON
            charge_point_status = enums.ChargePointStatus.preparing
        elif mode == 6: #   EVSE_STATE_CHARGING
            charge_point_status = enums.ChargePointStatus.charging
        elif mode == 7: #   EVSE_STATE_WAIT_CP2_OFF
            charge_point_status = enums.ChargePointStatus.finishing
        elif mode == 8: #   EVSE_STATE_WAIT_VEHICLE_STATUS
            charge_point_status = enums.ChargePointStatus.finishing
        elif mode == 9: #   EVSE_STATE_CP3_ON
            charge_point_status = enums.ChargePointStatus.finishing
        elif mode == 10: #  EVSE_STATE_CONTACTOR_ON
            charge_point_status = enums.ChargePointStatus.finishing
        elif mode == 11: #  EVSE_STATE_ERROR
            charge_point_status = enums.ChargePointStatus.faulted
        elif mode == 12: #  EVSE_STATE_TEST
            charge_point_status = enums.ChargePointStatus.unavailable

        md.from_micro[md.CONNECTOR_2][md.CHARGE_POINT_STATUS] = charge_point_status
        md.from_micro[md.CONNECTOR_2][md.CHARGE_POINT_ERROR_CODE]    = enums.ChargePointErrorCode.noError # : ocpp.v16.enums.ChargePointErrorCode.noError.value,
        md.from_micro[md.CONNECTOR_2][md.AVAILABILITY_TYPE]          = enums.AvailabilityType.operative # : ocpp.v16.enums.AvailabilityType.operative.value,
        md.from_micro[md.CONNECTOR_2][md.CHANGE_AVAILABILITY_STATUS] = enums.AvailabilityStatus.accepted # : ocpp.v16.enums.AvailabilityStatus.accepted.value,
        md.from_micro[md.CONNECTOR_2][md.ID_TAG]                     = 'id_tag_' + str(random.randint(1, 10))   #TODO: убрать рандом
        md.from_micro[md.CONNECTOR_2][md.TRANSACTION_ID]             = str(self.transaction_id_cnt)
        self.transaction_id_cnt += 1

        if md.from_micro[md.CONNECTOR_2][md.CHARGE_POINT_STATUS] != charge_point_status:
            md.from_micro[md.CONNECTOR_2][md.CHARGE_POINT_STATUS] = charge_point_status
            self.callback_status_notification(md.CONNECTOR_2)


    def on_electro_meter_data_update(self, modbus_data: dict[str, int]):
        if len(modbus_data) == 0:
            # md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.POWER_ACTIVE_IMPORT] = str(random.randint(100,200))
            return
        
            # CHARGE_POINT_MODEL: 'FMA',
            # CHARGE_POINT_VENDOR: 'NSTU',

        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.POWER_ACTIVE_IMPORT] = str(modbus_data[ElMeterRegs.KEY_SUMM_ACTIVE_POWER])
        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.SOC] = str(0)   # SOC: 78,
        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CURRENT_IMPORT] = str(modbus_data[ElMeterRegs.KEY_CURRENT_A])
        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.VOLTAGE] = str(modbus_data[ElMeterRegs.KEY_VOLTAGE_AN])
        self.connectors[0].power_value_from_micro= str(modbus_data[ElMeterRegs.KEY_VOLTAGE_AN])
         # = str(modbus_data.get(ElMeterRegs.KEY_VOLTAGE_AN))


        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CHARGE_POINT_STATUS]     = enums.ChargePointStatus.available
        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CHARGE_POINT_ERROR_CODE] = enums.ChargePointErrorCode.noError

        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.AVAILABILITY_TYPE] = enums.AvailabilityType.operative
        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.CHANGE_AVAILABILITY_STATUS] = enums.AvailabilityStatus.accepted

        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.ID_TAG] = '123'
        md.from_micro[md.CONNECTOR_0_CHARGE_POINT][md.TRANSACTION_ID] = self.transaction_id_cnt
        self.transaction_id_cnt += 1

        # if self.cp:
        #     self.cp.send_meter_values_sync(0)
        
        hmi_params = {}
        VOLTAGE = int(modbus_data[ElMeterRegs.KEY_VOLTAGE_AN])
        CURRENT = int(modbus_data[ElMeterRegs.KEY_CURRENT_A])
        POWER   = int(modbus_data[ElMeterRegs.KEY_SUMM_ACTIVE_POWER])

        hmi_params[cDeviceHMI.KEY_PARAM_VOLTAGE] = VOLTAGE
        hmi_params[cDeviceHMI.KEY_PARAM_CURRENT] = CURRENT
        hmi_params[cDeviceHMI.KEY_PARAM_POWER]   = POWER
        
        self.hmi.SetType2Params(hmi_params)

    def on_gb_t_data_update(self, modbus_data: dict[str, int]):
        if len(modbus_data) == 0:
            return

        hmi_params = {}

        VOLTAGE = int(modbus_data.get(GbTRegs.EVSE_CONVERTER_1_VOLTAGE.name))
        CURRENT = int(modbus_data.get(GbTRegs.EVSE_CONVERTER_1_CURRENT.name))
        POWER   = int(modbus_data.get(GbTRegs.EVSE_CONVERTER_1_INPUT_POWER.name))

        hmi_params[cDeviceHMI.KEY_PARAM_VOLTAGE] = VOLTAGE
        hmi_params[cDeviceHMI.KEY_PARAM_CURRENT] = CURRENT
        hmi_params[cDeviceHMI.KEY_PARAM_POWER]   = POWER

        modbus_mode = modbus_data.get(GbTRegs.EVSE_GB_T_MODE.name)
        if modbus_mode >= 3 and modbus_mode <= 8: # зарядка
            hmi_params[cDeviceHMI.KEY_PARAM_STATUS]  = 0
            hmi_params[cDeviceHMI.KEY_PARAM_START_STOP] = 1
        else: # доступен
            hmi_params[cDeviceHMI.KEY_PARAM_STATUS]  = 2
            hmi_params[cDeviceHMI.KEY_PARAM_START_STOP] = 0

        self.hmi.SetGbtParams(hmi_params)

    def on_hmi_data_update(self, modbus_data: dict[str, int]):
        if len(modbus_data) > 0:
            type2_start_stop_cmd   = modbus_data.get(cDeviceHMI.KEY_EVT_START_STOP_CMD_TYPE2)
            chademo_start_stop_cmd = modbus_data.get(cDeviceHMI.KEY_EVT_START_STOP_CMD_CHADEMO)
            gb_t_start_stop_cmd    = modbus_data.get(cDeviceHMI.KEY_EVT_START_STOP_CMD_GB_T)

            # if type2_start_stop_cmd != None:
            #     self.type2.SetChargeEnable(type2_start_stop_cmd == 1)
            if chademo_start_stop_cmd != None:
                pass
            if gb_t_start_stop_cmd != None:
                self.gb_t.SetChargeEnable(gb_t_start_stop_cmd == 1)

            type2_mode = self.type2.GetDeviceCurrentMode()
            if (type2_mode == 0) or (type2_mode == 1): # EVSE_STATE_NOT_CONNECT
                self.hmi.SetType2Params( {cDeviceHMI.KEY_PARAM_START_STOP_STATUS : 0} ) # кнопка недоступна
            elif type2_mode == 2: # EVSE_STATE_CONNECT
                self.hmi.SetType2Params( {cDeviceHMI.KEY_PARAM_START_STOP_STATUS : 1} ) # доступен СТАРТ
                if type2_start_stop_cmd == 1:
                    # self.type2.SetChargeEnable(1)
                    self.callback_handle_charging_request(1)
            else: # ЗАРЯДКА
                self.hmi.SetType2Params( {cDeviceHMI.KEY_PARAM_START_STOP_STATUS : 2} ) # доступен СТОП
                if type2_start_stop_cmd == 2:
                    # self.type2.SetChargeEnable(0)
                    self.callback_handle_charging_request(1)

            gb_t_mode = self.gb_t.GetDeviceCurrentMode()
            if (gb_t_mode == 0) or (gb_t_mode == 1): # EVSE_STATE_NONE, EVSE_STATE_NOT_CONNECT
                self.hmi.SetGbtParams( {cDeviceHMI.KEY_PARAM_START_STOP_STATUS : 0} ) # кнопка недоступна
            elif gb_t_mode == 2: # EVSE_STATE_CONNECT
                self.hmi.SetGbtParams( {cDeviceHMI.KEY_PARAM_START_STOP_STATUS : 1} ) # доступен СТАРТ
                if gb_t_start_stop_cmd == 1:
                    self.callback_handle_charging_request(2)
            else: # EVSE_STATE_CHARGING
                self.hmi.SetGbtParams( {cDeviceHMI.KEY_PARAM_START_STOP_STATUS : 2} ) # доступен СТОП
                if gb_t_start_stop_cmd == 2:
                    self.callback_handle_charging_request(2)

def main():
    mb = Modbus()
    mb.set_cp(None)
    
    import time
    while True:
        time.sleep(1.0)

if __name__ == '__main__':
    main()