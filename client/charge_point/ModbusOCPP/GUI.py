from tkinter import *
from tkinter import scrolledtext
from ModbusMain import cOcppModbus
import time
from threading import Thread as th

COM_PORT = 'COM14'

class ChademoGUI:
    def __init__(self) -> None:
        self.modbus = None
        self.window = Tk()
        self.window.geometry('700x950')
        self.window.title('Chademo')

        _column = 0
        _row = 0
        # self.label = Label(self.window, text='Label', font = ('Arial', 20))
        self.label = Label(self.window, text = 'Modbus is stop')
        self.label.grid(column = _column, row = _row)

        _row += 1
        self.txt_entry = Entry(self.window, width = 10)
        self.txt_entry.grid(column = _column, row = _row)
        self.txt_entry.insert(0, COM_PORT)
        self.txt_entry.focus()

        _row += 1
        # self.button_start = Button(self.window, text='Start', bg = 'black', fg = 'red', command = self.KlickHandler)
        self.button_start_modbus = Button(self.window, text='Start Modbus', command = self.StartModbus)
        self.button_start_modbus.grid(column = _column, row = _row)
        _row += 1
        self.button_get_data = Button(self.window, text='Get data', command = self.UpdateModbusData)
        self.button_get_data.grid(column = _column, row = _row)
        _row += 1
        self.button_charge_enable = Button(self.window, text='Charge enable', command = self.ChargeEnable)
        self.button_charge_enable.grid(column = _column, row = _row)
        _row += 1
        self.button_charge_disable = Button(self.window, text='Charge disable', command = self.ChargeDisable)
        self.button_charge_disable.grid(column = _column, row = _row)

        _column += 1
        self.multilines = scrolledtext.ScrolledText(self.window, width = 80, height = 75, font = ('Arial', 7))
        self.multilines.grid(column = _column, row = 0, columnspan = 1, rowspan = 100)

        _row = 0
        _column += 1
        self.label_sw_ver = Label(self.window, text = 'SW_VER:')
        self.label_sw_ver.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_time = Label(self.window, text = 'Time:')
        self.label_time.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_work_mode = Label(self.window, text = 'Work Mode:')
        self.label_work_mode.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_err_reg = Label(self.window, text = 'Error reg:')
        self.label_err_reg.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_di_reg = Label(self.window, text = 'Discrete inputs:')
        self.label_di_reg.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_power = Label(self.window, text = 'Power:')
        self.label_power.grid(column = _column, row = _row, sticky = 'w')

        _row += 1
        self.id_100_max_bat_volt = Label(self.window, text = 'ID_100_MAXIMUM_BATTERY_VOLTAGE:')
        self.id_100_max_bat_volt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_100_charger_rate_ref_const = Label(self.window, text = 'ID_100_CHARGED_RATE_REF_CONSTANT:')
        self.id_100_charger_rate_ref_const.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_101_max_charg_time_by_10s = Label(self.window, text = 'ID_101_MAX_CHARGE_TIME_BY_10S:')
        self.id_101_max_charg_time_by_10s.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_101_max_charg_time_by_min = Label(self.window, text = 'ID_101_MAX_CHARGE_TIME_BY_MIN:')
        self.id_101_max_charg_time_by_min.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_101_est_charge_time_by_min = Label(self.window, text = 'ID_101_EST_CHARGE_TIME_BY_MIN:')
        self.id_101_est_charge_time_by_min.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_101_total_cap_batt = Label(self.window, text = 'ID_101_TOTAL_CAP_BATT:')
        self.id_101_total_cap_batt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_102_protocol_num = Label(self.window, text = 'ID_102_PROTOCOL_NUMBER:')
        self.id_102_protocol_num.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_102_targ_batt_volt = Label(self.window, text = 'ID_102_TARG_BATT_VOLT:')
        self.id_102_targ_batt_volt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_102_request_current = Label(self.window, text = 'ID_102_REQUEST_CURRENT:')
        self.id_102_request_current.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_102_fault_flag = Label(self.window, text = 'ID_102_FAULT_FLAG:')
        self.id_102_fault_flag.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_102_status_flag = Label(self.window, text = 'ID_102_STATUS_FLAG:')
        self.id_102_status_flag.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.id_102_charged_rate = Label(self.window, text = 'ID_102_CHARGED_RATE:')
        self.id_102_charged_rate.grid(column = _column, row = _row, sticky = 'w')

        _row += 1 # EVSE_CHADEMO_ID_108_IDENTIFIER_OF_SUPPORT_FOR_EV_CONTACTOR_WELDING_DETECTION
        self.id_108_welding_detection = Label(self.window, text = 'ID_108_WELDING_DETECTION:')
        self.id_108_welding_detection.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_108_AVAILABLE_OUTPUT_VOLTAGE
        self.id_108_avail_output_volt = Label(self.window, text = 'ID_108_AVAIL_OUT_VOLT:')
        self.id_108_avail_output_volt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_108_AVAILABLE_OUTPUT_CURRENT
        self.id_108_avail_output_current = Label(self.window, text = 'ID_108_AVAIL_OUT_CURRENT:')
        self.id_108_avail_output_current.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_108_THRESHOLD_VOLTAGE
        self.id_108_threshold_voltage = Label(self.window, text = 'ID_108_THRESHOLD_VOLT:')
        self.id_108_threshold_voltage.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_109_CHADEMO_CONTROL_PROTOCOL_NUMBER
        self.id_109_protocol_number = Label(self.window, text = 'ID_109_PROTOCOL_NUMBER:')
        self.id_109_protocol_number.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_109_PRESENT_OUTPUT_VOLTAGE
        self.id_109_present_out_volt = Label(self.window, text = 'ID_109_PRES_OUT_VOLT:')
        self.id_109_present_out_volt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_109_PRESENT_CHARGING_CURRENT
        self.id_109_present_charge_current = Label(self.window, text = 'ID_109_PRES_CHARGE_CUR:')
        self.id_109_present_charge_current.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_109_STATUS_FAULT_FLAG
        self.id_109_status_fault_flag = Label(self.window, text = 'ID_109_STATUS_FAULT_FLAG:')
        self.id_109_status_fault_flag.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_109_REMAINING_CHARGING_TIME_BY_10S
        self.id_109_remain_time_by_10s = Label(self.window, text = 'ID_109_REMAIN_TIME_10S:')
        self.id_109_remain_time_by_10s.grid(column = _column, row = _row, sticky = 'w')
        _row += 1 # EVSE_CHADEMO_ID_109_REMAINING_CHARGING_TIME_BY_MINUTE
        self.id_109_remain_time_by_min = Label(self.window, text = 'ID_109_REMAIN_TIME_MIN:')
        self.id_109_remain_time_by_min.grid(column = _column, row = _row, sticky = 'w')

        _column += 1
        _row = 0
        self.label_converter_1_voltage = Label(self.window, text = 'CONVERTER_1_VOLTAGE:')
        self.label_converter_1_voltage.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_current = Label(self.window, text = 'CONVERTER_1_CURRENT:')
        self.label_converter_1_current.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_current_limit_point = Label(self.window, text = 'CONVERTER_1_CURRENT_LIMIT_POINT:')
        self.label_converter_1_current_limit_point.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_dc_board_temp = Label(self.window, text = 'CONVERTER_1_DC_BOARD_TEMPERATURE:')
        self.label_converter_1_dc_board_temp.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_input_phase_voltage = Label(self.window, text = 'CONVERTER_1_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE:')
        self.label_converter_1_input_phase_voltage.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_pfso_pos_half_bus = Label(self.window, text = 'CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS:')
        self.label_converter_1_pfso_pos_half_bus.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_pfso_neg_half_bus = Label(self.window, text = 'CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS:')
        self.label_converter_1_pfso_neg_half_bus.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_panel_ambient_temp = Label(self.window, text = 'CONVERTER_1_PANEL_AMBIENT_TEMPERATURE:')
        self.label_converter_1_panel_ambient_temp.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_phase_a_volt = Label(self.window, text = 'CONVERTER_1_AC_PHASE_A_VOLTAGE:')
        self.label_converter_1_phase_a_volt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_phase_b_volt = Label(self.window, text = 'CONVERTER_1_AC_PHASE_B_VOLTAGE:')
        self.label_converter_1_phase_b_volt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_phase_c_volt = Label(self.window, text = 'CONVERTER_1_AC_PHASE_C_VOLTAGE:')
        self.label_converter_1_phase_c_volt.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_pfc_board_temp = Label(self.window, text = 'CONVERTER_1_PFC_BOARD_TEMPERATURE:')
        self.label_converter_1_pfc_board_temp.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_rated_out_pwr = Label(self.window, text = 'CONVERTER_1_RATED_OUTPUT_POWER:')
        self.label_converter_1_rated_out_pwr.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_rated_out_cur = Label(self.window, text = 'CONVERTER_1_RATED_OUTPUT_CURRENT:')
        self.label_converter_1_rated_out_cur.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_alarm_status = Label(self.window, text = 'CONVERTER_1_CURRENT_ALARM_STATUS:')
        self.label_converter_1_alarm_status.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_dip_address = Label(self.window, text = 'CONVERTER_1_DIP_SWITCH_ADDRESS:')
        self.label_converter_1_dip_address.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_input_pwr = Label(self.window, text = 'CONVERTER_1_INPUT_POWER:')
        self.label_converter_1_input_pwr.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_altitude = Label(self.window, text = 'CONVERTER_1_CURRENT_SET_ALTITUDE:')
        self.label_converter_1_altitude.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_working_mode = Label(self.window, text = 'CONVERTER_1_WORKING_MODE:')
        self.label_converter_1_working_mode.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_serial_low = Label(self.window, text = 'CONVERTER_1_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9:')
        self.label_converter_1_serial_low.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_serial_hi = Label(self.window, text = 'CONVERTER_1_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER:')
        self.label_converter_1_serial_hi.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_dcdc_version = Label(self.window, text = 'CONVERTER_1_DCDC_VERSION:')
        self.label_converter_1_dcdc_version.grid(column = _column, row = _row, sticky = 'w')
        _row += 1
        self.label_converter_1_pfc_version = Label(self.window, text = 'CONVERTER_1_PFC_VERSION:')
        self.label_converter_1_pfc_version.grid(column = _column, row = _row, sticky = 'w')


    def Show(self):
        self.window.mainloop()

    def StartModbus(self):
        self.modbus = cOcppModbus(PORT = self.txt_entry.get())
        
        self.txt_entry.configure(state='disable')
        self.modbus.RunPolling()
        self.label.configure(text = 'Modbus is run')
        self.update_th = th(target = self.GetDataThread, daemon = True)
        self.update_thread_enable = True
        self.update_th.start()

    def GetDataThread(self):
        while self.update_thread_enable:
            time.sleep(0.5)
            self.UpdateModbusData()

    def UpdateModbusData(self):
        if self.modbus:
            self.multilines.delete(1.0, END)
            regs = self.modbus.GetAllRegistersAsDict()

            text = hex(regs['EVSE_CHADEMO_SW_VER'])
            self.label_sw_ver.configure(text = f'SW_VER: {text}')
            text = regs['EVSE_CHADEMO_TIME_SINCE_SWITCH_ON']
            self.label_time.configure(text = f'Time: {text} ms')
            text = regs['EVSE_CHADEMO_MODE']
            self.label_work_mode.configure(text = f'Work Mode: {text}')
            text = bin(regs['EVSE_CHADEMO_ERROR_REGISTER'])
            self.label_err_reg.configure(text = f'Error reg: {text}')
            text = bin(regs['EVSE_CHADEMO_DISCRETE_INPUTS'])
            self.label_di_reg.configure(text = f'Discrete inputs: {text}')
            text = regs['EVSE_CHADEMO_EVSE_POWER']
            self.label_power.configure(text = f'Power: {text} W')

            text = regs['ID_100_MAXIMUM_BATTERY_VOLTAGE']
            self.id_100_max_bat_volt.configure(text = f'ID_100_MAXIMUM_BATTERY_VOLTAGE: {text} V')
            text = regs['ID_100_CHARGED_RATE_REFERENCE_CONSTANT']
            self.id_100_charger_rate_ref_const.configure(text = f'ID_100_CHARGED_RATE_REF_CONSTANT: {text}')
            text = regs['ID_101_MAXIMUM_CHARGING_TIME_BY_10S']
            self.id_101_max_charg_time_by_10s.configure(text = f'ID_101_MAX_CHARGE_TIME_BY_10S: {text} x10s')
            text = regs['ID_101_MAXIMUM_CHARGING_TIME_BY_MINUTE']
            self.id_101_max_charg_time_by_min.configure(text = f'ID_101_MAX_CHARGE_TIME_BY_MIN: {text} min')
            text = regs['ID_101_ESTIMATED_CHARGING_TIME_BY_MINUTE']
            self.id_101_est_charge_time_by_min.configure(text = f'ID_101_EST_CHARGE_TIME_BY_MIN: {text} min')
            text = regs['ID_101_TOTAL_CAPACITY_OF_BATTERY_DECLARED_VALUE']
            self.id_101_total_cap_batt.configure(text = f'ID_101_TOTAL_CAP_BATT: {text}')
            text = regs['ID_102_CHADEMO_CONTROL_PROTOCOL_NUMBER']
            self.id_102_protocol_num.configure(text = f'ID_102_PROTOCOL_NUMBER: {text}')
            text = regs['ID_102_TARGET_BATTERY_VOLTAGE']
            self.id_102_targ_batt_volt.configure(text = f'ID_102_TARG_BATT_VOLT: {text} V')
            text = regs['ID_102_CHARGING_CURRENT_REQUEST']
            self.id_102_request_current.configure(text = f'ID_102_REQUEST_CURRENT: {text} A')
            text = bin(regs['ID_102_FAULT_FLAG'])
            self.id_102_fault_flag.configure(text = f'ID_102_FAULT_FLAG: {text}')
            text = bin(regs['ID_102_STATUS_FLAG'])
            self.id_102_status_flag.configure(text = f'ID_102_STATUS_FLAG: {text}')
            text = regs['ID_102_CHARGED_RATE']
            self.id_102_charged_rate.configure(text = f'ID_102_CHARGED_RATE: {text} %')

            text = regs['ID_108_IDENTIFIER_OF_SUPPORT_FOR_EV_CONTACTOR_WELDING_DETECTION']
            self.id_108_welding_detection.configure(text = f'ID_108_WELDING_DETECTION: {text}')
            text = regs['ID_108_AVAILABLE_OUTPUT_VOLTAGE']
            self.id_108_avail_output_volt.configure(text = f'ID_108_AVAIL_OUT_VOLT: {text} V')
            text = regs['ID_108_AVAILABLE_OUTPUT_CURRENT']
            self.id_108_avail_output_current.configure(text = f'ID_108_AVAIL_OUT_CURRENT: {text} A')
            text = regs['ID_108_THRESHOLD_VOLTAGE']
            self.id_108_threshold_voltage.configure(text = f'ID_108_THRESHOLD_VOLT: {text} V')
            text = regs['ID_109_CHADEMO_CONTROL_PROTOCOL_NUMBER']
            self.id_109_protocol_number.configure(text = f'ID_109_PROTOCOL_NUMBER: {text}')
            text = regs['ID_109_PRESENT_OUTPUT_VOLTAGE']
            self.id_109_present_out_volt.configure(text = f'ID_109_PRES_OUT_VOLT: {text} V')
            text = regs['ID_109_PRESENT_CHARGING_CURRENT']
            self.id_109_present_charge_current.configure(text = f'ID_109_PRES_CHARGE_CUR: {text}')
            text = bin(regs['ID_109_STATUS_FAULT_FLAG']) #hex(int(regs['ID_109_STATUS_FAULT_FLAG']))
            self.id_109_status_fault_flag.configure(text = f'ID_109_STATUS_FAULT_FLAG: {text}')
            text = regs['ID_109_REMAINING_CHARGING_TIME_BY_10S']
            self.id_109_remain_time_by_10s.configure(text = f'ID_109_REMAIN_TIME_10S: {text} x10s')
            text = regs['ID_109_REMAINING_CHARGING_TIME_BY_MINUTE']
            self.id_109_remain_time_by_min.configure(text = f'ID_109_REMAIN_TIME_MIN: {text} min')

            text = regs['CONVERTER_1_VOLTAGE']
            self.label_converter_1_voltage.configure(text = f'CONVERTER_1_VOLTAGE: {text} V')
            text = regs['CONVERTER_1_CURRENT']
            self.label_converter_1_current.configure(text = f'CONVERTER_1_CURRENT: {text} A')
            text = regs['CONVERTER_1_CURRENT_LIMIT_POINT']
            self.label_converter_1_current_limit_point.configure(text = f'CONVERTER_1_CURRENT_LIMIT_POINT: {text}')
            text = regs['CONVERTER_1_DC_BOARD_TEMPERATURE']
            self.label_converter_1_dc_board_temp.configure(text = f'CONVERTER_1_DC_BOARD_TEMPERATURE: {text} C')
            text = regs['CONVERTER_1_INPUT_PHASE_VOLTAGE_DC_INPUT_VOLTAGE']
            self.label_converter_1_input_phase_voltage.configure(text = f'CONVERTER_1_DC_INPUT_VOLTAGE: {text} V')
            text = regs['CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS']
            self.label_converter_1_pfso_pos_half_bus.configure(text = f'CONVERTER_1_PFCO_VOLTAGE_POSITIVE_HALF_BUS: {text} V')
            text = regs['CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS']
            self.label_converter_1_pfso_neg_half_bus.configure(text = f'CONVERTER_1_PFCO_VOLTAGE_NEGATIVE_HALF_BUS: {text} V')
            text = regs['CONVERTER_1_PANEL_AMBIENT_TEMPERATURE']
            self.label_converter_1_panel_ambient_temp.configure(text = f'CONVERTER_1_PANEL_AMBIENT_TEMP: {text} C')
            text = regs['CONVERTER_1_AC_PHASE_A_VOLTAGE']
            self.label_converter_1_phase_a_volt.configure(text = f'CONVERTER_1_AC_PHASE_A_VOLTAGE: {text} V')
            text = regs['CONVERTER_1_AC_PHASE_B_VOLTAGE']
            self.label_converter_1_phase_b_volt.configure(text = f'CONVERTER_1_AC_PHASE_B_VOLTAGE: {text} V')
            text = regs['CONVERTER_1_AC_PHASE_C_VOLTAGE']
            self.label_converter_1_phase_c_volt.configure(text = f'CONVERTER_1_AC_PHASE_C_VOLTAGE: {text} V')
            text = regs['CONVERTER_1_PFC_BOARD_TEMPERATURE']
            self.label_converter_1_pfc_board_temp.configure(text = f'CONVERTER_1_PFC_BOARD_TEMP: {text} C')
            text = regs['CONVERTER_1_RATED_OUTPUT_POWER']
            self.label_converter_1_rated_out_pwr.configure(text = f'CONVERTER_1_RATED_OUTPUT_POWER: {text} W')
            text = regs['CONVERTER_1_RATED_OUTPUT_CURRENT']
            self.label_converter_1_rated_out_cur.configure(text = f'CONVERTER_1_RATED_OUTPUT_CURRENT: {text} A')
            text = bin(regs['CONVERTER_1_CURRENT_ALARM_STATUS'])
            self.label_converter_1_alarm_status.configure(text = f'CONVERTER_1_ALARM_STATUS: {text}')
            text = regs['CONVERTER_1_DIP_SWITCH_ADDRESS']
            self.label_converter_1_dip_address.configure(text = f'CONVERTER_1_DIP_ADDRESS: {text}')
            text = regs['CONVERTER_1_INPUT_POWER']
            self.label_converter_1_input_pwr.configure(text = f'CONVERTER_1_INPUT_POWER: {text} W')
            text = regs['CONVERTER_1_CURRENT_SET_ALTITUDE']
            self.label_converter_1_altitude.configure(text = f'CONVERTER_1_ALTITUDE: {text} m')
            text = regs['CONVERTER_1_WORKING_MODE']
            self.label_converter_1_working_mode.configure(text = f'CONVERTER_1_WORKING_MODE: {text}')
            text = hex(regs['CONVERTER_1_NODE_SERIAL_NO_LOW_BYTES_ID_NUMBER_9'])
            self.label_converter_1_serial_low.configure(text = f'CONVERTER_1_SERIAL_NO_LOW_BYTES: {text}')
            text = hex(regs['CONVERTER_1_NODE_SERIAL_NO_HIGH_BYTES_ID_NUMBER'])
            self.label_converter_1_serial_hi.configure(text = f'CONVERTER_1_SERIAL_NO_HIGH_BYTES: {text}')
            text = hex(regs['CONVERTER_1_DCDC_VERSION'])
            self.label_converter_1_dcdc_version.configure(text = f'CONVERTER_1_DCDC_VERSION: {text}')
            text = hex(regs['CONVERTER_1_PFC_VERSION'])
            self.label_converter_1_pfc_version.configure(text = f'CONVERTER_1_PFC_VERSION: {text}')

            text = ''
            for key in regs.keys():
                text += f'{key}: {regs[key]}\n' # str(key) + '\n'
            self.multilines.insert(INSERT, text)
            

    def ChargeEnable(self):
        if self.modbus:
            self.modbus.SetChargeEnable(True)
    def ChargeDisable(self):
        if self.modbus:
            self.modbus.SetChargeEnable(False)

def main():
    gui = ChademoGUI()
    gui.Show()

    print('exit')

if __name__ == '__main__':
    main()