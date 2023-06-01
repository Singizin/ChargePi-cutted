import ocpp.v16.enums

CONNECTOR_0_CHARGE_POINT = 0
CONNECTOR_1 = 1
CONNECTOR_2 = 2
CONNECTOR_3 = 3

# 6.3. BootNotification.req Строка <= 20 символов
_ = ocpp.v16.call.BootNotificationPayload
CHARGE_POINT_MODEL = 'chargePointModel'
CHARGE_POINT_VENDOR = 'chargePointVendor'
# 6.4. BootNotification.conf

# 6.31. MeterValues.req
_, _ = ocpp.v16.call.MeterValuesPayload, \
       ocpp.v16.enums.Measurand
POWER_ACTIVE_IMPORT = 'Power.Active.Import'  # текущее показание по потребленной энергии Wh
SOC = 'SoC'  # уровень заряда электромобиля
CURRENT_IMPORT = 'Current.Import'  # текущий ток
VOLTAGE = 'Voltage'  # текущее напряжение
METER_VALUE = POWER_ACTIVE_IMPORT, SOC, CURRENT_IMPORT, VOLTAGE

# 4.9. Status Notification, там таблица состояний
# 6.47. StatusNotification.req
_, _, _ = ocpp.v16.call.StatusNotificationPayload, \
          ocpp.v16.enums.ChargePointStatus, \
          ocpp.v16.enums.ChargePointErrorCode
CHARGE_POINT_STATUS = 'charge_point_status'
CHARGE_POINT_ERROR_CODE = 'charge_point_error_code'

# 6.7. ChangeAvailability.req, 7.4. AvailabilityType
_, _ = ocpp.v16.call.ChangeAvailabilityPayload, \
       ocpp.v16.enums.AvailabilityType
AVAILABILITY_TYPE = 'availability_status'

# 7.3. AvailabilityStatus
_ = ocpp.v16.enums.AvailabilityStatus
CHANGE_AVAILABILITY_STATUS = 'change_availability_status'

# 4.10 StartTransaction
ID_TAG = 'idTag' # идентификатор RFID карты
TRANSACTION_ID = 'transactionId'

# 4.8 StartTransaction


# UnlockConnector
_, _ = ocpp.v16.call_result.UnlockStatus,\
       ocpp.v16.enums.UnlockStatus
CHANGE_UNLOCK_STATUS = 'change_unlock_status'

# RemoteStart / Stop Transaction
_ = ocpp.v16.enums.RemoteStartStopStatus
REMOTE_START_STOP_STATUS = 'remote_start_stop_status'

from_micro = {
    CONNECTOR_0_CHARGE_POINT:
        {

            CHARGE_POINT_MODEL: 'FMA',
            CHARGE_POINT_VENDOR: 'NSTU',

            POWER_ACTIVE_IMPORT: 123,
            SOC: 78,
            CURRENT_IMPORT: 20,
            VOLTAGE: 220,

            CHARGE_POINT_STATUS: ocpp.v16.enums.ChargePointStatus.available.value,
            CHARGE_POINT_ERROR_CODE: ocpp.v16.enums.ChargePointErrorCode.noError.value,

            AVAILABILITY_TYPE: ocpp.v16.enums.AvailabilityType.operative.value,
            CHANGE_AVAILABILITY_STATUS: ocpp.v16.enums.AvailabilityStatus.accepted.value,

            ID_TAG: 'zero',
            TRANSACTION_ID: 12345
        },
    CONNECTOR_1:
        {

            CHARGE_POINT_MODEL: 'FMA1',
            CHARGE_POINT_VENDOR: 'NSTU',

            POWER_ACTIVE_IMPORT: 123,
            SOC: 78,
            CURRENT_IMPORT: 20,
            VOLTAGE: 220,

            CHARGE_POINT_STATUS: ocpp.v16.enums.ChargePointStatus.available.value,
            CHARGE_POINT_ERROR_CODE: ocpp.v16.enums.ChargePointErrorCode.noError.value,

            AVAILABILITY_TYPE: ocpp.v16.enums.AvailabilityType.operative.value,
            CHANGE_AVAILABILITY_STATUS: ocpp.v16.enums.AvailabilityStatus.accepted.value,

            ID_TAG: 'first',
            TRANSACTION_ID: 12345,

            CHANGE_UNLOCK_STATUS: ocpp.v16.enums.UnlockStatus.notSupported.value,

            REMOTE_START_STOP_STATUS: ocpp.v16.enums.RemoteStartStopStatus.accepted.value
        },
    CONNECTOR_2:
        {

            CHARGE_POINT_MODEL: 'FMA2',
            CHARGE_POINT_VENDOR: 'NSTU',

            POWER_ACTIVE_IMPORT: 123,
            SOC: 78,
            CURRENT_IMPORT: 20,
            VOLTAGE: 220,

            CHARGE_POINT_STATUS: ocpp.v16.enums.ChargePointStatus.available.value,
            CHARGE_POINT_ERROR_CODE: ocpp.v16.enums.ChargePointErrorCode.noError.value,

            AVAILABILITY_TYPE: ocpp.v16.enums.AvailabilityType.operative.value,
            CHANGE_AVAILABILITY_STATUS: ocpp.v16.enums.AvailabilityStatus.accepted.value,

            ID_TAG: '123',
            TRANSACTION_ID: 12345,

            CHANGE_UNLOCK_STATUS: ocpp.v16.enums.UnlockStatus.notSupported.value,

            REMOTE_START_STOP_STATUS: ocpp.v16.enums.RemoteStartStopStatus.accepted.value
        },
    CONNECTOR_3:
        {

            CHARGE_POINT_MODEL: 'FMA3',
            CHARGE_POINT_VENDOR: 'NSTU',

            POWER_ACTIVE_IMPORT: 123,
            SOC: 78,
            CURRENT_IMPORT: 20,
            VOLTAGE: 220,

            CHARGE_POINT_STATUS: ocpp.v16.enums.ChargePointStatus.available.value,
            CHARGE_POINT_ERROR_CODE: ocpp.v16.enums.ChargePointErrorCode.noError.value,

            AVAILABILITY_TYPE: ocpp.v16.enums.AvailabilityType.operative.value,
            CHANGE_AVAILABILITY_STATUS: ocpp.v16.enums.AvailabilityStatus.accepted.value,

            ID_TAG: '123',
            TRANSACTION_ID: 12345,

            CHANGE_UNLOCK_STATUS: ocpp.v16.enums.UnlockStatus.notSupported.value,

            REMOTE_START_STOP_STATUS: ocpp.v16.enums.RemoteStartStopStatus.accepted.value
        }

}

