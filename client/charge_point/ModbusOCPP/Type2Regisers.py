from . import ModbusRegisersHelper as mbrh

UINT_ID_EVSE_TYPE_2 = 0x0F

# discrete outputs
KEY_DO_CHARGE_ENABLE   = 'EVSE DO_CHARGE_ENABLE'
KEY_DO_LOGGING_ENABLE  = 'DO_LOGGING_ENABLE'
KEY_DO_FAN_SW_ON       = 'DO_FAN_SW_ON'
KEY_DO_CONTACTOR_SW_ON = 'DO_CONTACTOR_SW_ON'
KEY_DO_LOCK            = 'DO_LOCK'
KEY_DO_PWM_ENABLE      = 'DO_PWM_ENABLE'
KEY_DO_ERROR_RESET     = 'DO_ERROR_RESET'

DO_CHARGE_ENABLE   = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_DO_CHARGE_ENABLE,      0, mbrh.type_bool)
DO_LOGGING_ENABLE  = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_DO_LOGGING_ENABLE,     1, mbrh.type_bool)
DO_FAN_SW_ON       = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_DO_FAN_SW_ON,          2, mbrh.type_bool)
DO_CONTACTOR_SW_ON = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_DO_CONTACTOR_SW_ON,    3, mbrh.type_bool)   # щелкнуть контактор 1/0
DO_LOCK            = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_DO_LOCK,               4, mbrh.type_bool)
DO_PWM_ENABLE      = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_DO_PWM_ENABLE,         5, mbrh.type_bool)
DO_ERROR_RESET     = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_DO_ERROR_RESET,        6, mbrh.type_bool)


# Holding Registers
KEY_EVSE_TEST_MODE               = 'EVSE test switch code'
KEY_EVSE_POWER                   = 'EVSE Power'
KEY_EVSE_PWM                     = 'EVSE PWM'
KEY_EVSE_CP_DISCONNECT_VOLTAGE   = 'EVSE CP_DISCONNECT_VOLTAGE'
KEY_EVSE_CP_CONNECT_VOLTAGE      = 'EVSE CP_CONNECT_VOLTAGE'
KEY_EVSE_CP_S2_ON_VOLTAGE        = 'EVSE CP_S2_ON_VOLTAGE'
KEY_EVSE_CP_S2_ON_VS_FAN_VOLTAGE = 'EVSE CP_S2_ON_VS_FAN_VOLTAGE'
KEY_EVSE_CP_VOLT_DEVIATION       = 'EVSE CP_VOLT_DEVIATION'

EVSE_TEST_MODE               = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_TEST_MODE,               0, mbrh.type_uint16)    # 0x1234
EVSE_POWER                   = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_POWER,                   1, mbrh.type_uint16)
EVSE_PWM                     = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_PWM,                     2, mbrh.type_uint16)
EVSE_CP_DISCONNECT_VOLTAGE   = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_CP_DISCONNECT_VOLTAGE,   3, mbrh.type_uint16)
EVSE_CP_CONNECT_VOLTAGE      = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_CP_CONNECT_VOLTAGE,      4, mbrh.type_uint16)
EVSE_CP_S2_ON_VOLTAGE        = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_CP_S2_ON_VOLTAGE,        5, mbrh.type_uint16)
EVSE_CP_S2_ON_VS_FAN_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_CP_S2_ON_VS_FAN_VOLTAGE, 6, mbrh.type_uint16)
EVSE_CP_VOLT_DEVIATION       = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, KEY_EVSE_CP_VOLT_DEVIATION,       7, mbrh.type_uint16)

# Input registers
SW_VER               = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, 'SW_VER',               0, mbrh.type_uint16)
TIME_SINCE_SWITCH_ON = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, 'TIME_SINCE_SWITCH_ON', 1, mbrh.type_uint32)
CP_VOLTAGE           = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, 'CP_VOLTAGE',           3, mbrh.type_uint16)
PP_VOLTAGE           = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, 'PP_VOLTAGE',           4, mbrh.type_uint16)
EVSE_MODE            = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, 'EVSE_MODE',            5, mbrh.type_uint16)
ERROR_REGISTER       = mbrh.cRegisterDescription(UINT_ID_EVSE_TYPE_2, 'ERROR_REGISTER',       6, mbrh.type_uint32)

##------------------------------------------------------------------------------
DiscreteOutputRegisters = [
    DO_CHARGE_ENABLE,
    DO_LOGGING_ENABLE,
    DO_FAN_SW_ON,
    DO_CONTACTOR_SW_ON,
    DO_LOCK,
    DO_PWM_ENABLE,
    DO_ERROR_RESET
                  ]
##------------------------------------------------------------------------------
DiscreteInputsRegisters = [

                  ]
##------------------------------------------------------------------------------
HoldingRegisters = [
    EVSE_TEST_MODE,
    EVSE_POWER,
    EVSE_PWM,
    EVSE_CP_DISCONNECT_VOLTAGE,
    EVSE_CP_CONNECT_VOLTAGE,
    EVSE_CP_S2_ON_VOLTAGE,
    EVSE_CP_S2_ON_VS_FAN_VOLTAGE,
    EVSE_CP_VOLT_DEVIATION
                  ]
##------------------------------------------------------------------------------
## описание регистров
InputRegisters = [
                    SW_VER,
                    TIME_SINCE_SWITCH_ON,
                    CP_VOLTAGE,
                    PP_VOLTAGE,
                    EVSE_MODE,
                    ERROR_REGISTER,
                  ]
##------------------------------------------------------------------------------
def main():
    pass

##------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
