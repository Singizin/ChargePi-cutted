from . import ModbusRegisersHelper as mbrh

UINT_ID_HMI = 11

# discrete outputs


# Holding Registers
AVAIL_STATUS_TYPE2     = mbrh.cRegisterDescription(UINT_ID_HMI, 'AVAIL_STATUS_TYPE2',     1000, mbrh.type_uint16)
INTERFACE_STATUS_TYPE2 = mbrh.cRegisterDescription(UINT_ID_HMI, 'INTERFACE_STATUS_TYPE2', 1001, mbrh.type_uint16)
START_STOP_STATUS_TYPE2 = mbrh.cRegisterDescription(UINT_ID_HMI, 'START_STOP_STATUS_TYPE2', 1002, mbrh.type_uint16)
RESERV1_TYPE2          = mbrh.cRegisterDescription(UINT_ID_HMI, 'RESERV1_TYPE2',          1003, mbrh.type_uint16)
RESERV2_TYPE2          = mbrh.cRegisterDescription(UINT_ID_HMI, 'RESERV2_TYPE2',          1004, mbrh.type_uint16)
CURRENT_TYPE2          = mbrh.cRegisterDescription(UINT_ID_HMI, 'CURRENT_TYPE2',          1005, mbrh.type_uint16)
VOLTAGE_TYPE2          = mbrh.cRegisterDescription(UINT_ID_HMI, 'VOLTAGE_TYPE2',          1006, mbrh.type_uint16)
SOC_TYPE2              = mbrh.cRegisterDescription(UINT_ID_HMI, 'SOC_TYPE2',              1007, mbrh.type_uint16)
TIME_REMAIN_SEC_TYPE2  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_SEC_TYPE2',  1008, mbrh.type_uint16)
TIME_REMAIN_MIN_TYPE2  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_MIN_TYPE2',  1009, mbrh.type_uint16)
TIME_REMAIN_H_TYPE2    = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_H_TYPE2',    1010, mbrh.type_uint16)
TIME_PASSED_SEC_TYPE2  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_SEC_TYPE2',  1011, mbrh.type_uint16)
TIME_PASSED_MIN_TYPE2  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_MIN_TYPE2',  1012, mbrh.type_uint16)
TIME_PASSED_H_TYPE2    = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_H_TYPE2',    1013, mbrh.type_uint16)
POWER_KWH_TYPE2        = mbrh.cRegisterDescription(UINT_ID_HMI, 'POWER_KWH_TYPE2',        1014, mbrh.type_uint16)
START_STOP_CMD_TYPE2   = mbrh.cRegisterDescription(UINT_ID_HMI, 'START_STOP_CMD_TYPE2',   1015, mbrh.type_uint16)

AVAIL_STATUS_GB_T     = mbrh.cRegisterDescription(UINT_ID_HMI, 'AVAIL_STATUS_GB_T',     1040, mbrh.type_uint16)
INTERFACE_STATUS_GB_T = mbrh.cRegisterDescription(UINT_ID_HMI, 'INTERFACE_STATUS_GB_T', 1041, mbrh.type_uint16)
START_STOP_STATUS_GB_T = mbrh.cRegisterDescription(UINT_ID_HMI, 'START_STOP_STATUS_GB_T', 1042, mbrh.type_uint16)
RESERV1_GB_T          = mbrh.cRegisterDescription(UINT_ID_HMI, 'RESERV1_GB_T',          1043, mbrh.type_uint16)
RESERV2_GB_T          = mbrh.cRegisterDescription(UINT_ID_HMI, 'RESERV2_GB_T',          1044, mbrh.type_uint16)
CURRENT_GB_T          = mbrh.cRegisterDescription(UINT_ID_HMI, 'CURRENT_GB_T',          1045, mbrh.type_uint16)
VOLTAGE_GB_T          = mbrh.cRegisterDescription(UINT_ID_HMI, 'VOLTAGE_GB_T',          1046, mbrh.type_uint16)
SOC_GB_T              = mbrh.cRegisterDescription(UINT_ID_HMI, 'SOC_GB_T',              1047, mbrh.type_uint16)
TIME_REMAIN_SEC_GB_T  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_SEC_GB_T',  1048, mbrh.type_uint16)
TIME_REMAIN_MIN_GB_T  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_MIN_GB_T',  1049, mbrh.type_uint16)
TIME_REMAIN_H_GB_T    = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_H_GB_T',    1050, mbrh.type_uint16)
TIME_PASSED_SEC_GB_T  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_SEC_GB_T',  1051, mbrh.type_uint16)
TIME_PASSED_MIN_GB_T  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_MIN_GB_T',  1052, mbrh.type_uint16)
TIME_PASSED_H_GB_T    = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_H_GB_T',    1053, mbrh.type_uint16)
POWER_KWH_GB_T        = mbrh.cRegisterDescription(UINT_ID_HMI, 'POWER_KWH_GB_T',        1054, mbrh.type_uint16)
START_STOP_CMD_GB_T   = mbrh.cRegisterDescription(UINT_ID_HMI, 'START_STOP_CMD_GB_T',   1055, mbrh.type_uint16)

AVAIL_STATUS_CHADEMO     = mbrh.cRegisterDescription(UINT_ID_HMI, 'AVAIL_STATUS_CHADEMO',     1080, mbrh.type_uint16)
INTERFACE_STATUS_CHADEMO = mbrh.cRegisterDescription(UINT_ID_HMI, 'INTERFACE_STATUS_CHADEMO', 1081, mbrh.type_uint16)
START_STOP_STATUS_CHADEMO = mbrh.cRegisterDescription(UINT_ID_HMI, 'START_STOP_STATUS_CHADEMO', 1082, mbrh.type_uint16)
RESERV1_CHADEMO          = mbrh.cRegisterDescription(UINT_ID_HMI, 'RESERV1_CHADEMO',          1083, mbrh.type_uint16)
RESERV2_CHADEMO          = mbrh.cRegisterDescription(UINT_ID_HMI, 'RESERV2_CHADEMO',          1084, mbrh.type_uint16)
CURRENT_CHADEMO          = mbrh.cRegisterDescription(UINT_ID_HMI, 'CURRENT_CHADEMO',          1085, mbrh.type_uint16)
VOLTAGE_CHADEMO          = mbrh.cRegisterDescription(UINT_ID_HMI, 'VOLTAGE_CHADEMO',          1086, mbrh.type_uint16)
SOC_CHADEMO              = mbrh.cRegisterDescription(UINT_ID_HMI, 'SOC_CHADEMO',              1087, mbrh.type_uint16)
TIME_REMAIN_SEC_CHADEMO  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_SEC_CHADEMO',  1088, mbrh.type_uint16)
TIME_REMAIN_MIN_CHADEMO  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_MIN_CHADEMO',  1089, mbrh.type_uint16)
TIME_REMAIN_H_CHADEMO    = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_REMAIN_H_CHADEMO',    1090, mbrh.type_uint16)
TIME_PASSED_SEC_CHADEMO  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_SEC_CHADEMO',  1091, mbrh.type_uint16)
TIME_PASSED_MIN_CHADEMO  = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_MIN_CHADEMO',  1092, mbrh.type_uint16)
TIME_PASSED_H_CHADEMO    = mbrh.cRegisterDescription(UINT_ID_HMI, 'TIME_PASSED_H_CHADEMO',    1093, mbrh.type_uint16)
POWER_KWH_CHADEMO        = mbrh.cRegisterDescription(UINT_ID_HMI, 'POWER_KWH_CHADEMO',        1094, mbrh.type_uint16)
START_STOP_CMD_CHADEMO   = mbrh.cRegisterDescription(UINT_ID_HMI, 'START_STOP_CMD_CHADEMO',   1095, mbrh.type_uint16)
# Input registers


##------------------------------------------------------------------------------
DiscreteOutputRegisters = [

                  ]
##------------------------------------------------------------------------------
DiscreteInputsRegisters = [

                  ]
##------------------------------------------------------------------------------
HoldingRegisters = [
    AVAIL_STATUS_TYPE2,
    INTERFACE_STATUS_TYPE2,
    START_STOP_STATUS_TYPE2,
    RESERV1_TYPE2,
    RESERV2_TYPE2,
    CURRENT_TYPE2,
    VOLTAGE_TYPE2,
    SOC_TYPE2,
    TIME_REMAIN_SEC_TYPE2,
    TIME_REMAIN_MIN_TYPE2,
    TIME_REMAIN_H_TYPE2,
    TIME_PASSED_SEC_TYPE2,
    TIME_PASSED_MIN_TYPE2,
    TIME_PASSED_H_TYPE2,
    POWER_KWH_TYPE2,
    START_STOP_CMD_TYPE2,

    AVAIL_STATUS_GB_T,
    INTERFACE_STATUS_GB_T,
    START_STOP_STATUS_GB_T,
    RESERV1_GB_T,
    RESERV2_GB_T,
    CURRENT_GB_T,
    VOLTAGE_GB_T,
    SOC_GB_T,
    TIME_REMAIN_SEC_GB_T,
    TIME_REMAIN_MIN_GB_T,
    TIME_REMAIN_H_GB_T,
    TIME_PASSED_SEC_GB_T,
    TIME_PASSED_MIN_GB_T,
    TIME_PASSED_H_GB_T,
    POWER_KWH_GB_T,
    START_STOP_CMD_GB_T,

    AVAIL_STATUS_CHADEMO,
    INTERFACE_STATUS_CHADEMO,
    START_STOP_STATUS_CHADEMO,
    RESERV1_CHADEMO,
    RESERV2_CHADEMO,
    CURRENT_CHADEMO,
    VOLTAGE_CHADEMO,
    SOC_CHADEMO,
    TIME_REMAIN_SEC_CHADEMO,
    TIME_REMAIN_MIN_CHADEMO,
    TIME_REMAIN_H_CHADEMO,
    TIME_PASSED_SEC_CHADEMO,
    TIME_PASSED_MIN_CHADEMO,
    TIME_PASSED_H_CHADEMO,
    POWER_KWH_CHADEMO,
    START_STOP_CMD_CHADEMO,
                  ]
##------------------------------------------------------------------------------
## описание регистров
InputRegisters = [


                  ]
##------------------------------------------------------------------------------
def main():
    pass

##------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
