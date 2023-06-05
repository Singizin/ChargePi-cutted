import charge_point.ModbusOCPP.ModbusRegisersHelper as mbrh

UINT_ID_EVSE_GB_T = 0x03

# discrete outputs
EVSE_GB_T_CHARGE_PERMIT = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'EVSE_GB_T_CHARGE_PERMIT', 0, mbrh.type_bool)
EVSE_GB_T_LOCK_ON       = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'lock_on',       10, mbrh.type_bool) #  (команда управления блокировкой замка в тестовом режиме True - блокирует / False - разблокирует)
# Holding Registers


# Input registers
input_index = 0
EVSE_CHADEMO_SW_VER               = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'EVSE_GB_T_SW_VER',               input_index, mbrh.type_uint16) # версия ПО
input_index += 1
EVSE_CHADEMO_TIME_SINCE_SWITCH_ON = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'EVSE_GB_T_TIME_SINCE_SWITCH_ON', input_index, mbrh.type_uint32) # время с момента включения, сек
input_index += 2
EVSE_GB_T_MODE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'EVSE_GB_T_MODE',                 input_index, mbrh.type_uint16) # режим работы устройства
input_index += 1
EVSE_CHADEMO_ERROR_REGISTER       = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'EVSE_GB_T_ERROR_REGISTER',       input_index, mbrh.type_uint32) # регистр ошибок зарядного контроллера
input_index += 2
EVSE_CHADEMO_DISCRETE_INPUTS      = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'EVSE_GB_T_DISCRETE_INPUTS',      input_index, mbrh.type_uint32) # регистр дискретных сигналов
input_index += 2
EVSE_CHADEMO_EVSE_POWER           = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'EVSE_GB_T_EVSE_POWER',           input_index, mbrh.type_uint16)
input_index += 1
CONNECTOR_STATE      = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'connector_state', input_index, mbrh.type_uint16)
input_index += 1
DETECT_POINT_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'detect_point_voltage', input_index, mbrh.type_uint16)
input_index += 1
U_OUT_VOLTAGE        = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'u_out_voltage', input_index, mbrh.type_uint16)
input_index += 1

CHM_BYTE1 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'chm_byte1', input_index, mbrh.type_uint16)
input_index += 1
CHM_BYTE2 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'chm_byte2', input_index, mbrh.type_uint16)
input_index += 1
CHM_BYTE3 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'chm_byte3', input_index, mbrh.type_uint16)
input_index += 1

CRM_IDENT_RESULT      = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'crm_ident_result',      input_index, mbrh.type_uint16)
input_index += 1
CRM_CHARGE_DEVNUMBER_HI = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'crm_ChargeDevNumberHi', input_index, mbrh.type_uint16)
input_index += 1
CRM_CHARGE_DEVNUMBER_LO = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'crm_ChargeDevNumberLo', input_index, mbrh.type_uint16)
input_index += 1
CRM_REGION_CODE_0     = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'crm_region_code_0',     input_index, mbrh.type_uint16)
input_index += 1
CRM_REGION_CODE_1     = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'crm_region_code_1',     input_index, mbrh.type_uint16)
input_index += 1
CRM_REGION_CODE_2     = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'crm_region_code_2',     input_index, mbrh.type_uint16)
input_index += 1

CTS_SECOND = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cts_second', input_index, mbrh.type_uint16)
input_index += 1
CTS_MINUTE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cts_minute', input_index, mbrh.type_uint16)
input_index += 1
CTS_HOUR   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cts_hour',   input_index, mbrh.type_uint16)
input_index += 1
CTS_DAY    = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cts_day',    input_index, mbrh.type_uint16)
input_index += 1
CTS_MONTH  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cts_month',  input_index, mbrh.type_uint16)
input_index += 1
CTS_YEAR   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cts_year',   input_index, mbrh.type_uint16)
input_index += 1

MAX_EVSE_VOLT    = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'MaxEVSEVolt',    input_index, mbrh.type_uint16)
input_index += 1
MIN_EVSE_VOLT    = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'MinEVSEVolt',    input_index, mbrh.type_uint16)
input_index += 1
MAX_EVSE_CURRENT = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'MaxEVSECurrent', input_index, mbrh.type_uint16)
input_index += 1
MIN_EVSE_CURRENT = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'MinEVSECurrent', input_index, mbrh.type_uint16)
input_index += 1

CRO_EVSE_READY_TO_CHARGE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CRO_evse_ready_to_charge', input_index, mbrh.type_uint16)
input_index += 1

CCS_OUTPUT_VOLTAGE           = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'ccs_output_voltage',           input_index, mbrh.type_uint16)
input_index += 1
CCS_OUTPUT_CURRENT           = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'ccs_output_current',           input_index, mbrh.type_uint16)
input_index += 1
CCS_CUMULATIVE_CHARGING_TIME = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'ccs_cumulative_charging_time', input_index, mbrh.type_uint16)
input_index += 1
CCS_CHARGING_PERMIT_JUDGMENT = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'ccs_charging_permit_judgment', input_index, mbrh.type_uint16)
input_index += 1

CST_REASON_OF_CHARGER_DISCONTINUING_CHARGING         = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cst_reason_of_charger_discontinuing_charging',         input_index, mbrh.type_uint16)
input_index += 1
CST_FAILURE_REASON_OF_CHARGER_DISCONTINUING_CHARGING = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cst_failure_reason_of_charger_discontinuing_charging', input_index, mbrh.type_uint16)
input_index += 1
CST_ERROR_REASON_OF_CHARGER_DISCONTINUING_CHARGING   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cst_error_reason_of_charger_discontinuing_charging',   input_index, mbrh.type_uint16)
input_index += 1

CSD_CUMULATIVE_CHARGING_TIME_MIN = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'csd_cumulative_charging_time_min', input_index, mbrh.type_uint16)
input_index += 1
CSD_TOTAL_OUTPUT_ENERGY_VALUE    = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'csd_total_output_energy_value',    input_index, mbrh.type_uint16)
input_index += 1
CSD_CHARGER_NUMBER               = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'csd_charger_Number',               input_index, mbrh.type_uint16)
input_index += 1

CEM_BYTE_1 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cem_byte_1', input_index, mbrh.type_uint16)
input_index += 1
CEM_BYTE_2 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cem_byte_2', input_index, mbrh.type_uint16)
input_index += 1
CEM_BYTE_3 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cem_byte_3', input_index, mbrh.type_uint16)
input_index += 1
CEM_BYTE_4 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'cem_byte_4', input_index, mbrh.type_uint16)
input_index += 1

CHARGE_STATE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'charge_state', input_index, mbrh.type_uint16)
input_index += 1
BHM_MAXCHARGE_VOLTAGE                        = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bhm_maxcharge_voltage', input_index, mbrh.type_uint16)
input_index += 1

BRM_BMS_COMMUNICATION_PROTOCOL_NO            = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'brm_bms_communication_protocol_no',            input_index, mbrh.type_uint16)
input_index += 1
BRM_BATTERY_TYPE                             = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'brm_battery_type',                             input_index, mbrh.type_uint16)
input_index += 1
BRM_RATED_CAPACITY_OF_VEHICLE_BATTERY_SYSTEM = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'brm_rated_capacity_of_vehicle_battery_system', input_index, mbrh.type_uint16)
input_index += 1
BRM_RATED_VOLTAGE_OF_VEHICLE_BATTERY_SYSTEM  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'brm_rated_voltage_of_vehicle_battery_system',  input_index, mbrh.type_uint16)
input_index += 1

BCP_BATTERY_CELL_MAX_ALLOWABLE_CHARGING_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcp_battery_cell_max_allowable_charging_voltage', input_index, mbrh.type_uint16)
input_index += 1
BCP_MAX_ALLOWABLE_CHARGING_CURRENT              = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcp_max_allowable_charging_current',              input_index, mbrh.type_uint16)
input_index += 1
BCP_BATTERY_NOMINAL_TOTAL_ENERGY                = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcp_battery_nominal_total_energy',                input_index, mbrh.type_uint16)
input_index += 1
BCP_MAX_ALLOWABLE_CHARGING_VOLTAGE              = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcp_max_allowable_charging_voltage',              input_index, mbrh.type_uint16)
input_index += 1
BCP_MAX_ALLOWABLE_TEMPERATURE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcp_max_allowable_temperature',                   input_index, mbrh.type_uint16)
input_index += 1
BCP_BATTERY_SOC                                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcp_battery_soc',                                 input_index, mbrh.type_uint16)
input_index += 1
BCP_BATTERY_IMMEDIATE_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcp_battery_immediate_voltage',                   input_index, mbrh.type_uint16)
input_index += 1

BRO_EV_READY_TO_CHARGE         = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bro_ev_ready_to_charge',         input_index, mbrh.type_uint16)
input_index += 1

BCL_REQUIRED_CHARGE_VOLTAGE    = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcl_required_charge_voltage',    input_index, mbrh.type_uint16)
input_index += 1
BCL_CHARGE_CURRENT_CONSUMPTION = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcl_charge_current_consumption', input_index, mbrh.type_uint16)
input_index += 1
BCL_CHARGE_MODE                = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcl_charge_mode',                input_index, mbrh.type_uint16)
input_index += 1

BCS_CHARGING_VOLTAGE_MEASUREMENT                      = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcs_charging_voltage_measurement',      input_index, mbrh.type_uint16)
input_index += 1
BCS_CHARGE_CURRENT_MEASUREMENT                        = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcs_charge_current_measurement',        input_index, mbrh.type_uint16)
input_index += 1
BCS_MAXIMUM_BATTERY_CELL_VOLTAGE_AND_ITS_GROUP_NUMBER = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcs_maximum_battery_cell_voltage_and_its_group_number', input_index, mbrh.type_uint16)
input_index += 1
BCS_IMMEDIATE_SOC                                     = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcs_immediate_soc',                     input_index, mbrh.type_uint16)
input_index += 1
BCS_ESTIMATED_REMAINING_CHARGING_TIME                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bcs_estimated_remaining_charging_time', input_index, mbrh.type_uint16)
input_index += 1

BSM_IDENTIFIER_NUMBER_OF_THE_MAXIMUM_BATTERY_CELL_VOLTAGE        = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsm_identifier_number_of_the_max_batt_cell_voltage',    input_index, mbrh.type_uint16)
input_index += 1
BSM_BATTERY_MAXIMUM_TEMPERATURE                                  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsm_battery_maximum_temperature',                       input_index, mbrh.type_uint16)
input_index += 1
BSM_IDENTIFIER_NUMBER_OF_THE_MAXIMUM_TEMPERATURE_DETECTION_POINT = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsm_identifier_number_of_the_max_temp_detection_point', input_index, mbrh.type_uint16)
input_index += 1
BSM_BATTERY_MINIMUM_TEMPERATURE                                  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsm_battery_minimum_temperature',                       input_index, mbrh.type_uint16)
input_index += 1
BSM_IDENTIFIER_NUMBER_OF_THE_MINIMUM_TEMPERATURE_DETECTION_POINT = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsm_identifier_num_of_the_min_temp_detection_point',    input_index, mbrh.type_uint16)
input_index += 1
BSM_BYTE_6 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsm_byte_6', input_index, mbrh.type_uint16)
input_index += 1
BSM_BYTE_7 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsm_byte_7', input_index, mbrh.type_uint16)
input_index += 1

BSD_SOC_AT_ABORT_TIME        = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsd_soc_at_abort_time',        input_index, mbrh.type_uint16)
input_index += 1
BSD_BATTERY_CELL_MIN_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsd_battery_cell_min_voltage', input_index, mbrh.type_uint16)
input_index += 1
BSD_BATTERY_CELL_MAX_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsd_battery_cell_max_voltage', input_index, mbrh.type_uint16)
input_index += 1
BSD_BATTERY_MIN_TEMP         = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsd_battery_min_temp',         input_index, mbrh.type_uint16)
input_index += 1
BSD_BATTERY_MAX_TEMP         = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'bsd_battery_max_temp',         input_index, mbrh.type_uint16)
input_index += 1

#input_index = 77
EVSE_CONVERTER_1_VOLTAGE                              = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_VOLTAGE',                              input_index, mbrh.type_float) #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_CURRENT                              = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_CURRENT',                              input_index, mbrh.type_float)  # module_current; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_CURRENT_LIMIT_POINT                  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_CURRENT_LIMIT_POINT',                  input_index, mbrh.type_float)  # module_current_limit_point; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_DC_BOARD_TEMPERATURE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_DC_BOARD_TEMPERATURE',                 input_index, mbrh.type_float)  # module_dc_board_temperature; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE', input_index, mbrh.type_float)  # module_input_phase_voltage_dc_input_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS',       input_index, mbrh.type_float)  # module_pfco_voltage_positive_half_bus; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS',       input_index, mbrh.type_float)  # module_pfco_voltage_negative_half_bus; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_PANEL_AMBIENT_TEMPERATURE            = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_PANEL_AMBIENT_TEMPERATURE',            input_index, mbrh.type_float)  # module_panel_ambient_temperature; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_AC_PHASE_A_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_AC_PHASE_A_VOLTAGE',                   input_index, mbrh.type_float)  # module_ac_phase_a_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_AC_PHASE_B_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_AC_PHASE_B_VOLTAGE',                   input_index, mbrh.type_float)  # module_ac_phase_b_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_AC_PHASE_C_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_AC_PHASE_C_VOLTAGE',                   input_index, mbrh.type_float)  # module_ac_phase_c_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_PFC_BOARD_TEMPERATURE                = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_PFC_BOARD_TEMPERATURE',                input_index, mbrh.type_float)  # module_pfc_board_temperature; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_RATED_OUTPUT_POWER                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_RATED_OUTPUT_POWER',                   input_index, mbrh.type_float)  # module_rated_output_power; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_RATED_OUTPUT_CURRENT                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_RATED_OUTPUT_CURRENT',                 input_index, mbrh.type_float)  # module_rated_output_current; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_CURRENT_ALARM_STATUS                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_CURRENT_ALARM_STATUS',                 input_index, mbrh.type_uint32)  # current_alarm_status.uint32; #  uint32_t ; # регистр дискретных сигналов ошибок и статусов
input_index += 2
EVSE_CONVERTER_1_DIP_SWITCH_ADDRESS                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_DIP_SWITCH_ADDRESS',                   input_index, mbrh.type_uint32)  # dip_switch_address; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_INPUT_POWER                          = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_INPUT_POWER',                          input_index, mbrh.type_uint32)  # input_power; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_CURRENT_SET_ALTITUDE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_CURRENT_SET_ALTITUDE',                 input_index, mbrh.type_uint32)  # current_set_altitude; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_CURRENT_INPUT_WORKING_MODE           = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_WORKING_MODE',                         input_index, mbrh.type_uint32)  # current_module_input_working_mode; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9', input_index, mbrh.type_uint32)  # node_serial_no_low_bytes_id_number_9; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER',  input_index, mbrh.type_uint32)  # node_serial_no_high_bytes_id_number; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_DCDC_VERSION                         = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_DCDC_VERSION',                         input_index, mbrh.type_uint32)  # dcdc_version; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_1_PFC_VERSION                          = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_1_PFC_VERSION',                          input_index, mbrh.type_uint32)  # pfc_version; #  uint32_t ;

input_index += 2
EVSE_CONVERTER_2_VOLTAGE                              = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_VOLTAGE',                              input_index, mbrh.type_float) #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_CURRENT                              = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_CURRENT',                              input_index, mbrh.type_float)  # module_current; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_CURRENT_LIMIT_POINT                  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_CURRENT_LIMIT_POINT',                  input_index, mbrh.type_float)  # module_current_limit_point; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_DC_BOARD_TEMPERATURE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_DC_BOARD_TEMPERATURE',                 input_index, mbrh.type_float)  # module_dc_board_temperature; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE', input_index, mbrh.type_float)  # module_input_phase_voltage_dc_input_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_PFCO_VOLTAGE_POSITIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_PFCO_VOLTAGE_POSITIVE_HALF_BUS',       input_index, mbrh.type_float)  # module_pfco_voltage_positive_half_bus; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_PFCO_VOLTAGE_NEGATIVE_HALF_BUS       = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_PFCO_VOLTAGE_NEGATIVE_HALF_BUS',       input_index, mbrh.type_float)  # module_pfco_voltage_negative_half_bus; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_PANEL_AMBIENT_TEMPERATURE            = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_PANEL_AMBIENT_TEMPERATURE',            input_index, mbrh.type_float)  # module_panel_ambient_temperature; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_AC_PHASE_A_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_AC_PHASE_A_VOLTAGE',                   input_index, mbrh.type_float)  # module_ac_phase_a_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_AC_PHASE_B_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_AC_PHASE_B_VOLTAGE',                   input_index, mbrh.type_float)  # module_ac_phase_b_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_AC_PHASE_C_VOLTAGE                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_AC_PHASE_C_VOLTAGE',                   input_index, mbrh.type_float)  # module_ac_phase_c_voltage; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_PFC_BOARD_TEMPERATURE                = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_PFC_BOARD_TEMPERATURE',                input_index, mbrh.type_float)  # module_pfc_board_temperature; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_RATED_OUTPUT_POWER                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_RATED_OUTPUT_POWER',                   input_index, mbrh.type_float)  # module_rated_output_power; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_RATED_OUTPUT_CURRENT                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_RATED_OUTPUT_CURRENT',                 input_index, mbrh.type_float)  # module_rated_output_current; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_CURRENT_ALARM_STATUS                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_CURRENT_ALARM_STATUS',                 input_index, mbrh.type_uint32)  # current_alarm_status.uint32; #  uint32_t ; # регистр дискретных сигналов ошибок и статусов
input_index += 2
EVSE_CONVERTER_2_DIP_SWITCH_ADDRESS                   = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_DIP_SWITCH_ADDRESS',                   input_index, mbrh.type_uint32)  # dip_switch_address; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_INPUT_POWER                          = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_INPUT_POWER',                          input_index, mbrh.type_uint32)  # input_power; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_CURRENT_SET_ALTITUDE                 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_CURRENT_SET_ALTITUDE',                 input_index, mbrh.type_uint32)  # current_set_altitude; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_CURRENT_INPUT_WORKING_MODE           = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_WORKING_MODE',                         input_index, mbrh.type_uint32)  # current_module_input_working_mode; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9 = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9', input_index, mbrh.type_uint32)  # node_serial_no_low_bytes_id_number_9; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER  = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER',  input_index, mbrh.type_uint32)  # node_serial_no_high_bytes_id_number; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_DCDC_VERSION                         = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_DCDC_VERSION',                         input_index, mbrh.type_uint32)  # dcdc_version; #  uint32_t ;
input_index += 2
EVSE_CONVERTER_2_PFC_VERSION                          = mbrh.cRegisterDescription(UINT_ID_EVSE_GB_T, 'CONVERTER_2_PFC_VERSION',                          input_index, mbrh.type_uint32)  # pfc_version; #  uint32_t ;

##------------------------------------------------------------------------------
DiscreteOutputRegisters = [
    EVSE_GB_T_CHARGE_PERMIT
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
    EVSE_GB_T_MODE,
    EVSE_CHADEMO_ERROR_REGISTER,
    EVSE_CHADEMO_DISCRETE_INPUTS,
    EVSE_CHADEMO_EVSE_POWER,

    CONNECTOR_STATE,
    DETECT_POINT_VOLTAGE,
    U_OUT_VOLTAGE,

    CHM_BYTE1,
    CHM_BYTE2,
    CHM_BYTE3,

    CRM_IDENT_RESULT,
    CRM_CHARGE_DEVNUMBER_HI,
    CRM_CHARGE_DEVNUMBER_LO,
    CRM_REGION_CODE_0,
    CRM_REGION_CODE_1,
    CRM_REGION_CODE_2,

    CTS_SECOND,
    CTS_MINUTE,
    CTS_HOUR,
    CTS_DAY,
    CTS_MONTH,
    CTS_YEAR,

    MAX_EVSE_VOLT,
    MIN_EVSE_VOLT,
    MAX_EVSE_CURRENT,
    MIN_EVSE_CURRENT,

    CRO_EVSE_READY_TO_CHARGE,

    CCS_OUTPUT_VOLTAGE,
    CCS_OUTPUT_CURRENT,
    CCS_CUMULATIVE_CHARGING_TIME,
    CCS_CHARGING_PERMIT_JUDGMENT,

    CST_REASON_OF_CHARGER_DISCONTINUING_CHARGING,
    CST_FAILURE_REASON_OF_CHARGER_DISCONTINUING_CHARGING,
    CST_ERROR_REASON_OF_CHARGER_DISCONTINUING_CHARGING,

    CSD_CUMULATIVE_CHARGING_TIME_MIN,
    CSD_TOTAL_OUTPUT_ENERGY_VALUE,
    CSD_CHARGER_NUMBER,

    CEM_BYTE_1,
    CEM_BYTE_2,
    CEM_BYTE_3,
    CEM_BYTE_4,

    CHARGE_STATE,

    BHM_MAXCHARGE_VOLTAGE,

    BRM_BMS_COMMUNICATION_PROTOCOL_NO,
    BRM_BATTERY_TYPE,
    BRM_RATED_CAPACITY_OF_VEHICLE_BATTERY_SYSTEM,
    BRM_RATED_VOLTAGE_OF_VEHICLE_BATTERY_SYSTEM,

    BCP_BATTERY_CELL_MAX_ALLOWABLE_CHARGING_VOLTAGE,
    BCP_MAX_ALLOWABLE_CHARGING_CURRENT,
    BCP_BATTERY_NOMINAL_TOTAL_ENERGY,
    BCP_MAX_ALLOWABLE_CHARGING_VOLTAGE,
    BCP_MAX_ALLOWABLE_TEMPERATURE,
    BCP_BATTERY_SOC,
    BCP_BATTERY_IMMEDIATE_VOLTAGE,

    BRO_EV_READY_TO_CHARGE,

    BCL_REQUIRED_CHARGE_VOLTAGE,
    BCL_CHARGE_CURRENT_CONSUMPTION,
    BCL_CHARGE_MODE,

    BCS_CHARGING_VOLTAGE_MEASUREMENT,
    BCS_CHARGE_CURRENT_MEASUREMENT,
    BCS_MAXIMUM_BATTERY_CELL_VOLTAGE_AND_ITS_GROUP_NUMBER,
    BCS_IMMEDIATE_SOC,
    BCS_ESTIMATED_REMAINING_CHARGING_TIME,

    BSM_IDENTIFIER_NUMBER_OF_THE_MAXIMUM_BATTERY_CELL_VOLTAGE,
    BSM_BATTERY_MAXIMUM_TEMPERATURE,
    BSM_IDENTIFIER_NUMBER_OF_THE_MAXIMUM_TEMPERATURE_DETECTION_POINT,
    BSM_BATTERY_MINIMUM_TEMPERATURE,
    BSM_IDENTIFIER_NUMBER_OF_THE_MINIMUM_TEMPERATURE_DETECTION_POINT,
    BSM_BYTE_6,
    BSM_BYTE_7,

    BSD_SOC_AT_ABORT_TIME,
    BSD_BATTERY_CELL_MIN_VOLTAGE,
    BSD_BATTERY_CELL_MAX_VOLTAGE,
    BSD_BATTERY_MIN_TEMP,
    BSD_BATTERY_MAX_TEMP,

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
