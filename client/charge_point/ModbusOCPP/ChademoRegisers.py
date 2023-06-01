# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0],'...'))
from . import ModbusRegisersHelper as mbrh
# import ModbusOCPP.ModbusRegisersHelper as mbrh



UINT_ID_EVSE_CHADEMO = 0x02

# discrete outputs
EVSE_CHADEMO_CHARGE_PERMIT  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'charge_permit',  0, mbrh.type_bool) # (сигнал разрешения заряда)
EVSE_CHADEMO_RESET_ERROR    = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'reset_error',    1, mbrh.type_bool) # (сигнал сброса аварии в тестовом режиме)
EVSE_CHADEMO_LOGGING_ENABLE = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'logging_enable', 2, mbrh.type_bool) #  (команда вкл/выкл логирования UART)
EVSE_CHADEMO_CP_ON          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'cp_on',          3, mbrh.type_bool) #  (команда вкл/выкл CP в тестовом режиме)
EVSE_CHADEMO_CP3_ON         = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'cp3_on',         4, mbrh.type_bool) #  (команда вкл/выкл CP3 в тестовом режиме)
EVSE_CHADEMO_K1_ON          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'k1_on',          5, mbrh.type_bool) #  (команда вкл/выкл K1 в тестовом режиме)
EVSE_CHADEMO_LED_YELLO_ON   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'led_yello_on',   6, mbrh.type_bool) #  (команда вкл/выкл LED_YELLO в тестовом режиме)
EVSE_CHADEMO_LED_BLUE_ON    = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'led_blue_on',    7, mbrh.type_bool) #  (команда вкл/выкл LED_BLUE в тестовом режиме)
EVSE_CHADEMO_LED_RED_ON     = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'led_red_on',     8, mbrh.type_bool) #  (команда вкл/выкл LED_RED в тестовом режиме)
EVSE_CHADEMO_K12_ON         = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'k12_on',         9, mbrh.type_bool) #  (команда вкл/выкл контактора в тестовом режиме)
EVSE_CHADEMO_LOCK_ON        = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'lock_on',       10, mbrh.type_bool) #  (команда управления блокировкой замка в тестовом режиме)
EVSE_CHADEMO_CONVETER_1_ON  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'conveter_1_on', 11, mbrh.type_bool) #  (команда вкл/выкл преобразователя №1 в тестовом режиме)
EVSE_CHADEMO_CONVETER_2_ON  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'conveter_2_on', 12, mbrh.type_bool) #  (команда вкл/выкл преобразователя №2  (в тестовом режиме)

# Holding Registers
EVSE_CHADEMO_TEST_MODE_ON                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'TEST_MODE_ON',                   0, mbrh.type_uint16) # включение тестового режима устройства (запись в регистр спец кода)
EVSE_CHADEMO_SET_POWER_IN_TEST_MODE         = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'SET_POWER_IN_TEST_MODE',         1, mbrh.type_uint16) # установка мощности ЗС в тестовом режиме
EVSE_CHADEMO_SET_CONVERTER_1_OUTPUT_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'SET_CONVERTER_1_OUTPUT_VOLTAGE', 2, mbrh.type_float) # установка напряжения 1-го конвертера(в тестовом режиме)
EVSE_CHADEMO_SET_CONVERTER_1_OUTPUT_CURRENT = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'SET_CONVERTER_1_OUTPUT_CURRENT', 4, mbrh.type_uint16) # установка тока 1-го конвертера (в тестовом режиме)
EVSE_CHADEMO_SET_CONVERTER_2_OUTPUT_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'SET_CONVERTER_2_OUTPUT_VOLTAGE', 5, mbrh.type_float) # установка напряжения 2-го конвертера (в тестовом режиме)
EVSE_CHADEMO_SET_CONVERTER_2_OUTPUT_CURRENT = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'SET_CONVERTER_2_OUTPUT_CURRENT', 7, mbrh.type_uint16) # установка тока 2-го конвертера (в тестовом режиме)


# Input registers
EVSE_CHADEMO_SW_VER               = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'EVSE_CHADEMO_SW_VER',               0, mbrh.type_uint16) # версия ПО
EVSE_CHADEMO_TIME_SINCE_SWITCH_ON = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'EVSE_CHADEMO_TIME_SINCE_SWITCH_ON', 1, mbrh.type_uint32) # время с момента включения, сек
EVSE_CHADEMO_MODE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'EVSE_CHADEMO_MODE',                 3, mbrh.type_uint16) # режим работы устройства
EVSE_CHADEMO_ERROR_REGISTER       = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'EVSE_CHADEMO_ERROR_REGISTER',       4, mbrh.type_uint32) # регистр ошибок зарядного контроллера
EVSE_CHADEMO_DISCRETE_INPUTS      = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'EVSE_CHADEMO_DISCRETE_INPUTS',      6, mbrh.type_uint32) # регистр дискретных сигналов
EVSE_CHADEMO_EVSE_POWER           = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'EVSE_CHADEMO_EVSE_POWER',           8, mbrh.type_uint16)

EVSE_CHADEMO_ID_100_MAXIMUM_BATTERY_VOLTAGE                  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_100_MAXIMUM_BATTERY_VOLTAGE',                   9, mbrh.type_uint16)
EVSE_CHADEMO_ID_100_CHARGED_RATE_REFERENCE_CONSTANT          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_100_CHARGED_RATE_REFERENCE_CONSTANT',          10, mbrh.type_uint16)
EVSE_CHADEMO_ID_101_MAXIMUM_CHARGING_TIME_BY_10S             = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_101_MAXIMUM_CHARGING_TIME_BY_10S',             11, mbrh.type_uint16)
EVSE_CHADEMO_ID_101_MAXIMUM_CHARGING_TIME_BY_MINUTE          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_101_MAXIMUM_CHARGING_TIME_BY_MINUTE',          12, mbrh.type_uint16)
EVSE_CHADEMO_ID_101_ESTIMATED_CHARGING_TIME_BY_MINUTE        = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_101_ESTIMATED_CHARGING_TIME_BY_MINUTE',        13, mbrh.type_uint16)
EVSE_CHADEMO_ID_101_TOTAL_CAPACITY_OF_BATTERY_DECLARED_VALUE = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_101_TOTAL_CAPACITY_OF_BATTERY_DECLARED_VALUE', 14, mbrh.type_uint16)
EVSE_CHADEMO_ID_102_CHADEMO_CONTROL_PROTOCOL_NUMBER          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_102_CHADEMO_CONTROL_PROTOCOL_NUMBER',          15, mbrh.type_uint16)
EVSE_CHADEMO_ID_102_TARGET_BATTERY_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_102_TARGET_BATTERY_VOLTAGE',                   16, mbrh.type_uint16)
EVSE_CHADEMO_ID_102_CHARGING_CURRENT_REQUEST                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_102_CHARGING_CURRENT_REQUEST',                 17, mbrh.type_uint16)
EVSE_CHADEMO_ID_102_FAULT_FLAG                               = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_102_FAULT_FLAG',                               18, mbrh.type_uint16)
EVSE_CHADEMO_ID_102_STATUS_FLAG                              = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_102_STATUS_FLAG',                              19, mbrh.type_uint16)
EVSE_CHADEMO_ID_102_CHARGED_RATE                             = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_102_CHARGED_RATE',                             20, mbrh.type_uint16)

EVSE_CHADEMO_ID_108_IDENTIFIER_OF_SUPPORT_FOR_EV_CONTACTOR_WELDING_DETECTION = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_108_IDENTIFIER_OF_SUPPORT_FOR_EV_CONTACTOR_WELDING_DETECTION', 21, mbrh.type_uint16)
EVSE_CHADEMO_ID_108_AVAILABLE_OUTPUT_VOLTAGE          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_108_AVAILABLE_OUTPUT_VOLTAGE',          22, mbrh.type_uint16)
EVSE_CHADEMO_ID_108_AVAILABLE_OUTPUT_CURRENT          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_108_AVAILABLE_OUTPUT_CURRENT',          23, mbrh.type_uint16)
EVSE_CHADEMO_ID_108_THRESHOLD_VOLTAGE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_108_THRESHOLD_VOLTAGE',                 24, mbrh.type_uint16)
EVSE_CHADEMO_ID_109_CHADEMO_CONTROL_PROTOCOL_NUMBER   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_109_CHADEMO_CONTROL_PROTOCOL_NUMBER',   25, mbrh.type_uint16)
EVSE_CHADEMO_ID_109_PRESENT_OUTPUT_VOLTAGE            = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_109_PRESENT_OUTPUT_VOLTAGE',            26, mbrh.type_uint16)
EVSE_CHADEMO_ID_109_PRESENT_CHARGING_CURRENT          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_109_PRESENT_CHARGING_CURRENT',          27, mbrh.type_uint16)
EVSE_CHADEMO_ID_109_STATUS_FAULT_FLAG                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_109_STATUS_FAULT_FLAG',                 28, mbrh.type_uint16)
EVSE_CHADEMO_ID_109_REMAINING_CHARGING_TIME_BY_10S    = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_109_REMAINING_CHARGING_TIME_BY_10S',    29, mbrh.type_uint16)
EVSE_CHADEMO_ID_109_REMAINING_CHARGING_TIME_BY_MINUTE = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'ID_109_REMAINING_CHARGING_TIME_BY_MINUTE', 30, mbrh.type_uint16)

EVSE_CONVERTER_1_VOLTAGE                              = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_VOLTAGE',                              31, mbrh.type_float) #  uint32_t ;
EVSE_CONVERTER_1_CURRENT                              = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_CURRENT',                              33, mbrh.type_float)  # module_current; #  uint32_t ;
EVSE_CONVERTER_1_CURRENT_LIMIT_POINT                  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_CURRENT_LIMIT_POINT',                  35, mbrh.type_float)  # module_current_limit_point; #  uint32_t ;
EVSE_CONVERTER_1_DC_BOARD_TEMPERATURE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_DC_BOARD_TEMPERATURE',                 37, mbrh.type_float)  # module_dc_board_temperature; #  uint32_t ;
EVSE_CONVERTER_1_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE', 39, mbrh.type_float)  # module_input_phase_voltage_dc_input_voltage; #  uint32_t ;
EVSE_CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS',       41, mbrh.type_float)  # module_pfco_voltage_positive_half_bus; #  uint32_t ;
EVSE_CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS',       43, mbrh.type_float)  # module_pfco_voltage_negative_half_bus; #  uint32_t ;
EVSE_CONVERTER_1_PANEL_AMBIENT_TEMPERATURE            = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_PANEL_AMBIENT_TEMPERATURE',            45, mbrh.type_float)  # module_panel_ambient_temperature; #  uint32_t ;
EVSE_CONVERTER_1_AC_PHASE_A_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_AC_PHASE_A_VOLTAGE',                   47, mbrh.type_float)  # module_ac_phase_a_voltage; #  uint32_t ;
EVSE_CONVERTER_1_AC_PHASE_B_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_AC_PHASE_B_VOLTAGE',                   49, mbrh.type_float)  # module_ac_phase_b_voltage; #  uint32_t ;
EVSE_CONVERTER_1_AC_PHASE_C_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_AC_PHASE_C_VOLTAGE',                   51, mbrh.type_float)  # module_ac_phase_c_voltage; #  uint32_t ;
EVSE_CONVERTER_1_PFC_BOARD_TEMPERATURE                = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_PFC_BOARD_TEMPERATURE',                53, mbrh.type_float)  # module_pfc_board_temperature; #  uint32_t ;
EVSE_CONVERTER_1_RATED_OUTPUT_POWER                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_RATED_OUTPUT_POWER',                   55, mbrh.type_float)  # module_rated_output_power; #  uint32_t ;
EVSE_CONVERTER_1_RATED_OUTPUT_CURRENT                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_RATED_OUTPUT_CURRENT',                 57, mbrh.type_float)  # module_rated_output_current; #  uint32_t ;
EVSE_CONVERTER_1_CURRENT_ALARM_STATUS                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_CURRENT_ALARM_STATUS',                 59, mbrh.type_uint32)  # current_alarm_status.uint32; #  uint32_t ; # регистр дискретных сигналов ошибок и статусов
EVSE_CONVERTER_1_DIP_SWITCH_ADDRESS                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_DIP_SWITCH_ADDRESS',                   61, mbrh.type_uint32)  # dip_switch_address; #  uint32_t ;
EVSE_CONVERTER_1_INPUT_POWER                          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_INPUT_POWER',                          63, mbrh.type_uint32)  # input_power; #  uint32_t ;
EVSE_CONVERTER_1_CURRENT_SET_ALTITUDE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_CURRENT_SET_ALTITUDE',                 65, mbrh.type_uint32)  # current_set_altitude; #  uint32_t ;
EVSE_CONVERTER_1_CURRENT_INPUT_WORKING_MODE           = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_WORKING_MODE',                         67, mbrh.type_uint32)  # current_module_input_working_mode; #  uint32_t ;
EVSE_CONVERTER_1_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9', 69, mbrh.type_uint32)  # node_serial_no_low_bytes_id_number_9; #  uint32_t ;
EVSE_CONVERTER_1_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER',  71, mbrh.type_uint32)  # node_serial_no_high_bytes_id_number; #  uint32_t ;
EVSE_CONVERTER_1_DCDC_VERSION                         = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_DCDC_VERSION',                         73, mbrh.type_uint32)  # dcdc_version; #  uint32_t ;
EVSE_CONVERTER_1_PFC_VERSION                          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_1_PFC_VERSION',                          75, mbrh.type_uint32)  # pfc_version; #  uint32_t ;

EVSE_CONVERTER_2_VOLTAGE                              = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_VOLTAGE',                              77, mbrh.type_float) #  uint32_t ;
EVSE_CONVERTER_2_CURRENT                              = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_CURRENT',                              79, mbrh.type_float)  # module_current; #  uint32_t ;
EVSE_CONVERTER_2_CURRENT_LIMIT_POINT                  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_CURRENT_LIMIT_POINT',                  81, mbrh.type_float)  # module_current_limit_point; #  uint32_t ;
EVSE_CONVERTER_2_DC_BOARD_TEMPERATURE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_DC_BOARD_TEMPERATURE',                 83, mbrh.type_float)  # module_dc_board_temperature; #  uint32_t ;
EVSE_CONVERTER_2_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE', 85, mbrh.type_float)  # module_input_phase_voltage_dc_input_voltage; #  uint32_t ;
EVSE_CONVERTER_2_PFCO_VOLTAGE_POSITIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_PFCO_VOLTAGE_POSITIVE_HALF_BUS',       87, mbrh.type_float)  # module_pfco_voltage_positive_half_bus; #  uint32_t ;
EVSE_CONVERTER_2_PFCO_VOLTAGE_NEGATIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_PFCO_VOLTAGE_NEGATIVE_HALF_BUS',       89, mbrh.type_float)  # module_pfco_voltage_negative_half_bus; #  uint32_t ;
EVSE_CONVERTER_2_PANEL_AMBIENT_TEMPERATURE            = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_PANEL_AMBIENT_TEMPERATURE',            91, mbrh.type_float)  # module_panel_ambient_temperature; #  uint32_t ;
EVSE_CONVERTER_2_AC_PHASE_A_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_AC_PHASE_A_VOLTAGE',                   93, mbrh.type_float)  # module_ac_phase_a_voltage; #  uint32_t ;
EVSE_CONVERTER_2_AC_PHASE_B_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_AC_PHASE_B_VOLTAGE',                   95, mbrh.type_float)  # module_ac_phase_b_voltage; #  uint32_t ;
EVSE_CONVERTER_2_AC_PHASE_C_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_AC_PHASE_C_VOLTAGE',                   97, mbrh.type_float)  # module_ac_phase_c_voltage; #  uint32_t ;
EVSE_CONVERTER_2_PFC_BOARD_TEMPERATURE                = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_PFC_BOARD_TEMPERATURE',                99, mbrh.type_float)  # module_pfc_board_temperature; #  uint32_t ;
EVSE_CONVERTER_2_RATED_OUTPUT_POWER                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_RATED_OUTPUT_POWER',                   101, mbrh.type_float)  # module_rated_output_power; #  uint32_t ;
EVSE_CONVERTER_2_RATED_OUTPUT_CURRENT                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_RATED_OUTPUT_CURRENT',                 103, mbrh.type_float)  # module_rated_output_current; #  uint32_t ;
EVSE_CONVERTER_2_CURRENT_ALARM_STATUS                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_CURRENT_ALARM_STATUS',                 105, mbrh.type_uint32)  # current_alarm_status.uint32; #  uint32_t ; # регистр дискретных сигналов ошибок и статусов
EVSE_CONVERTER_2_DIP_SWITCH_ADDRESS                   = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_DIP_SWITCH_ADDRESS',                   107, mbrh.type_uint32)  # dip_switch_address; #  uint32_t ;
EVSE_CONVERTER_2_INPUT_POWER                          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_INPUT_POWER',                          109, mbrh.type_uint32)  # input_power; #  uint32_t ;
EVSE_CONVERTER_2_CURRENT_SET_ALTITUDE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_CURRENT_SET_ALTITUDE',                 111, mbrh.type_uint32)  # current_set_altitude; #  uint32_t ;
EVSE_CONVERTER_2_CURRENT_INPUT_WORKING_MODE           = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_WORKING_MODE',                         113, mbrh.type_uint32)  # current_module_input_working_mode; #  uint32_t ;
EVSE_CONVERTER_2_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9 = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9', 115, mbrh.type_uint32)  # node_serial_no_low_bytes_id_number_9; #  uint32_t ;
EVSE_CONVERTER_2_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER  = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER',  117, mbrh.type_uint32)  # node_serial_no_high_bytes_id_number; #  uint32_t ;
EVSE_CONVERTER_2_DCDC_VERSION                         = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_DCDC_VERSION',                         119, mbrh.type_uint32)  # dcdc_version; #  uint32_t ;
EVSE_CONVERTER_2_PFC_VERSION                          = mbrh.cRegisterDescription(UINT_ID_EVSE_CHADEMO, 'CONVERTER_2_PFC_VERSION',                          121, mbrh.type_uint32)  # pfc_version; #  uint32_t ;

##------------------------------------------------------------------------------
DiscreteOutputRegisters = [

                  ]
##------------------------------------------------------------------------------
DiscreteInputsRegisters = [

                  ]
##------------------------------------------------------------------------------
HoldingRegisters = [

                  ]
##------------------------------------------------------------------------------
## описание регистров
InputRegisters = [

    EVSE_CHADEMO_SW_VER,
    EVSE_CHADEMO_TIME_SINCE_SWITCH_ON,
    EVSE_CHADEMO_MODE,
    EVSE_CHADEMO_ERROR_REGISTER,
    EVSE_CHADEMO_DISCRETE_INPUTS,
    EVSE_CHADEMO_EVSE_POWER,

    EVSE_CHADEMO_ID_100_MAXIMUM_BATTERY_VOLTAGE,
    EVSE_CHADEMO_ID_100_CHARGED_RATE_REFERENCE_CONSTANT,
    EVSE_CHADEMO_ID_101_MAXIMUM_CHARGING_TIME_BY_10S,
    EVSE_CHADEMO_ID_101_MAXIMUM_CHARGING_TIME_BY_MINUTE,
    EVSE_CHADEMO_ID_101_ESTIMATED_CHARGING_TIME_BY_MINUTE,
    EVSE_CHADEMO_ID_101_TOTAL_CAPACITY_OF_BATTERY_DECLARED_VALUE,
    EVSE_CHADEMO_ID_102_CHADEMO_CONTROL_PROTOCOL_NUMBER,
    EVSE_CHADEMO_ID_102_TARGET_BATTERY_VOLTAGE,
    EVSE_CHADEMO_ID_102_CHARGING_CURRENT_REQUEST,
    EVSE_CHADEMO_ID_102_FAULT_FLAG,
    EVSE_CHADEMO_ID_102_STATUS_FLAG,
    EVSE_CHADEMO_ID_102_CHARGED_RATE,

    EVSE_CHADEMO_ID_108_IDENTIFIER_OF_SUPPORT_FOR_EV_CONTACTOR_WELDING_DETECTION,
    EVSE_CHADEMO_ID_108_AVAILABLE_OUTPUT_VOLTAGE,
    EVSE_CHADEMO_ID_108_AVAILABLE_OUTPUT_CURRENT,
    EVSE_CHADEMO_ID_108_THRESHOLD_VOLTAGE,
    EVSE_CHADEMO_ID_109_CHADEMO_CONTROL_PROTOCOL_NUMBER,
    EVSE_CHADEMO_ID_109_PRESENT_OUTPUT_VOLTAGE,
    EVSE_CHADEMO_ID_109_PRESENT_CHARGING_CURRENT,
    EVSE_CHADEMO_ID_109_STATUS_FAULT_FLAG,
    EVSE_CHADEMO_ID_109_REMAINING_CHARGING_TIME_BY_10S,
    EVSE_CHADEMO_ID_109_REMAINING_CHARGING_TIME_BY_MINUTE,

    EVSE_CONVERTER_1_VOLTAGE,
    EVSE_CONVERTER_1_CURRENT,
    EVSE_CONVERTER_1_CURRENT_LIMIT_POINT,
    EVSE_CONVERTER_1_DC_BOARD_TEMPERATURE,
    EVSE_CONVERTER_1_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE,
    EVSE_CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS,
    EVSE_CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS,
    EVSE_CONVERTER_1_PANEL_AMBIENT_TEMPERATURE,
    EVSE_CONVERTER_1_AC_PHASE_A_VOLTAGE,
    EVSE_CONVERTER_1_AC_PHASE_B_VOLTAGE,
    EVSE_CONVERTER_1_AC_PHASE_C_VOLTAGE,
    EVSE_CONVERTER_1_PFC_BOARD_TEMPERATURE,
    EVSE_CONVERTER_1_RATED_OUTPUT_POWER,
    EVSE_CONVERTER_1_RATED_OUTPUT_CURRENT,
    EVSE_CONVERTER_1_CURRENT_ALARM_STATUS,
    EVSE_CONVERTER_1_DIP_SWITCH_ADDRESS,
    EVSE_CONVERTER_1_INPUT_POWER,
    EVSE_CONVERTER_1_CURRENT_SET_ALTITUDE,
    EVSE_CONVERTER_1_CURRENT_INPUT_WORKING_MODE,
    EVSE_CONVERTER_1_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9,
    EVSE_CONVERTER_1_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER,
    EVSE_CONVERTER_1_DCDC_VERSION,
    EVSE_CONVERTER_1_PFC_VERSION,

    EVSE_CONVERTER_2_VOLTAGE,
    EVSE_CONVERTER_2_CURRENT,
    EVSE_CONVERTER_2_CURRENT_LIMIT_POINT,
    EVSE_CONVERTER_2_DC_BOARD_TEMPERATURE,
    EVSE_CONVERTER_2_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE,
    EVSE_CONVERTER_2_PFCO_VOLTAGE_POSITIVE_HALF_BUS,
    EVSE_CONVERTER_2_PFCO_VOLTAGE_NEGATIVE_HALF_BUS,
    EVSE_CONVERTER_2_PANEL_AMBIENT_TEMPERATURE,
    EVSE_CONVERTER_2_AC_PHASE_A_VOLTAGE,
    EVSE_CONVERTER_2_AC_PHASE_B_VOLTAGE,
    EVSE_CONVERTER_2_AC_PHASE_C_VOLTAGE,
    EVSE_CONVERTER_2_PFC_BOARD_TEMPERATURE,
    EVSE_CONVERTER_2_RATED_OUTPUT_POWER,
    EVSE_CONVERTER_2_RATED_OUTPUT_CURRENT,
    EVSE_CONVERTER_2_CURRENT_ALARM_STATUS,
    EVSE_CONVERTER_2_DIP_SWITCH_ADDRESS,
    EVSE_CONVERTER_2_INPUT_POWER,
    EVSE_CONVERTER_2_CURRENT_SET_ALTITUDE,
    EVSE_CONVERTER_2_CURRENT_INPUT_WORKING_MODE,
    EVSE_CONVERTER_2_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9,
    EVSE_CONVERTER_2_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER,
    EVSE_CONVERTER_2_DCDC_VERSION,
    EVSE_CONVERTER_2_PFC_VERSION,
                  ]
##------------------------------------------------------------------------------
def main():
    pass

##------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
