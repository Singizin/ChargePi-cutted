import charge_point.ModbusOCPP.ModbusRegisersHelper as mbrh

UINT_ID_EL_COUNTER = 0x01

# discrete outputs


# Holding Registers


# Input registers


##------------------------------------------------------------------------------
DiscreteOutputRegisters = [

                  ]
##------------------------------------------------------------------------------
DiscreteInputsRegisters = [

                  ]
##------------------------------------------------------------------------------
KEY_LINK_STATUS        = 'LINK_STATUS' # 'Статус связи '
KEY_ADDR               = 'ADDR' #  'Адрес счетчика '
KEY_NOT_USE            = 'NOT_USE' #  'Не используется '
KEY_HR_MIN             = 'HR_MIN' #  'Ст.-часы, мл.-минуты '
KEY_SEC                = 'SEC' #  'мл.-секунды '
KEY_DAY_WEEK_DAY_MONTH = 'DAY_WEEK_DAY_MONTH' #  'Ст.-день недели, мл.-число '
KEY_MONTH_YEAR         = 'MONTH_YEAR' #  'Ст.-месяц, мл.-год '
KEY_SUMM_ACTIVE_POWER  = 'SUMM_ACTIVE_POWER' #  'Суммарная прямая активная мощность '
KEY_ACTIVE_POWER_A     = 'ACTIVE_POWER_A' #  'Активная мощность фазы А '
KEY_ACTIVE_POWER_B     = 'ACTIVE_POWER_B' #  'Активная мощность фазы B '
KEY_ACTIVE_POWER_C     = 'ACTIVE_POWER_C' #  'Активная мощность фазы C '
KEY_CURRENT_A          = 'CURRENT_A' #  'Ток фазы А '
KEY_CURRENT_B          = 'CURRENT_B' #  'Ток фазы B '
KEY_CURRENT_C          = 'CURRENT_C' #  'Ток фазы C '
KEY_VOLTAGE_AN         = 'VOLTAGE_AN' #  'Напряжение АN '
KEY_VOLTAGE_BN         = 'VOLTAGE_BN' #  'Напряжение BN '
KEY_VOLTAGE_CN         = 'VOLTAGE_CN' #  'Напряжение CN '
KEY_FREQUENCY          = 'FREQUENCY' #  'Частота '
KEY_ENERGY_CONSUMED    = 'ENERGY_CONSUMED' #  'Энергия (потреблен.) '
KEY_RELEASED_ENERGY    = 'RELEASED_ENERGY' #  'Энергия (отпущен.) '

KEY_LINK_STATUS_2        = 'LINK_STATUS_2' # 'Статус связи '
KEY_ADDR_2               = 'ADDR_2' #  'Адрес счетчика '
KEY_NOT_USE_2            = 'NOT_USE_2' #  'Не используется '
KEY_HR_MIN_2             = 'HR_MIN_2' #  'Ст.-часы, мл.-минуты '
KEY_SEC_2                = 'SEC_2' #  'мл.-секунды '
KEY_DAY_WEEK_DAY_MONTH_2 = 'DAY_WEEK_DAY_MONTH_2' #  'Ст.-день недели, мл.-число '
KEY_MONTH_YEAR_2         = 'MONTH_YEAR_2' #  'Ст.-месяц, мл.-год '
KEY_SUMM_ACTIVE_POWER_2  = 'SUMM_ACTIVE_POWER_2' #  'Суммарная прямая активная мощность '
KEY_ACTIVE_POWER_A_2     = 'ACTIVE_POWER_A_2' #  'Активная мощность фазы А '
KEY_ACTIVE_POWER_B_2     = 'ACTIVE_POWER_B_2' #  'Активная мощность фазы B '
KEY_ACTIVE_POWER_C_2     = 'ACTIVE_POWER_C_2' #  'Активная мощность фазы C '
KEY_CURRENT_A_2          = 'CURRENT_A_2' #  'Ток фазы А '
KEY_CURRENT_B_2          = 'CURRENT_B_2' #  'Ток фазы B '
KEY_CURRENT_C_2          = 'CURRENT_C_2' #  'Ток фазы C '
KEY_VOLTAGE_AN_2         = 'VOLTAGE_AN_2' #  'Напряжение АN '
KEY_VOLTAGE_BN_2         = 'VOLTAGE_BN_2' #  'Напряжение BN '
KEY_VOLTAGE_CN_2         = 'VOLTAGE_CN_2' #  'Напряжение CN '
KEY_FREQUENCY_2          = 'FREQUENCY_2' #  'Частота '
KEY_ENERGY_CONSUMED_2    = 'ENERGY_CONSUMED_2' #  'Энергия (потреблен.) '
KEY_RELEASED_ENERGY_2    = 'RELEASED_ENERGY_2' #  'Энергия (отпущен.) '

HoldingRegisters = [
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_LINK_STATUS,        4352, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ADDR,               4353, mbrh.type_uint16), # 3 регистра
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_NOT_USE,            4356, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_HR_MIN,             4357, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_SEC,                4358, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_DAY_WEEK_DAY_MONTH, 4359, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_MONTH_YEAR,         4360, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_SUMM_ACTIVE_POWER,  4361, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ACTIVE_POWER_A,     4363, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ACTIVE_POWER_B,     4365, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ACTIVE_POWER_C,     4367, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_CURRENT_A,          4369, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_CURRENT_B,          4371, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_CURRENT_C,          4373, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_VOLTAGE_AN,         4375, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_VOLTAGE_BN,         4377, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_VOLTAGE_CN,         4379, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_FREQUENCY,          4381, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ENERGY_CONSUMED,    4383, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_RELEASED_ENERGY,    4385, mbrh.type_float),

    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_LINK_STATUS_2,        4480, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ADDR_2,               4481, mbrh.type_uint16), # 3 регистра
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_NOT_USE_2,            4483, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_HR_MIN_2,             4484, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_SEC_2,                4485, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_DAY_WEEK_DAY_MONTH_2, 4486, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_MONTH_YEAR_2,         4487, mbrh.type_uint16),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_SUMM_ACTIVE_POWER_2,  4488, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ACTIVE_POWER_A_2,     4490, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ACTIVE_POWER_B_2,     4492, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ACTIVE_POWER_C_2,     4494, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_CURRENT_A_2,          4496, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_CURRENT_B_2,          4498, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_CURRENT_C_2,          4500, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_VOLTAGE_AN_2,         4502, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_VOLTAGE_BN_2,         4504, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_VOLTAGE_CN_2,         4506, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_FREQUENCY_2,          4508, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_ENERGY_CONSUMED_2,    4510, mbrh.type_float),
    mbrh.cRegisterDescription(UINT_ID_EL_COUNTER, KEY_RELEASED_ENERGY_2,    4512, mbrh.type_float),
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
