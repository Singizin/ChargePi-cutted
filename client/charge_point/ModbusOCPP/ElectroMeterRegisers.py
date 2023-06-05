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
