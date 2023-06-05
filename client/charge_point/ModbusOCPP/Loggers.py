import datetime
import json

## -----------------------------------------------------------------------------
class cLoggerBase:
    def __init__(self):
        self.log_enable = False
        print('logger:' + self.__class__.__name__ + '.__init__()')
    
    def LoggingSwitch(self, enable):
        self.log_enable = True

    def GetFileName(self):
        dt = datetime.datetime.now()
        f_name = self.__class__.__name__ + '_' + dt.strftime("%d.%m.%Y_%H") + '.log'
        return f_name

    def LogToFile(self, text):
        log_file_name = self.GetFileName()
        log_file = open(log_file_name, 'a')
        log_file.write(text + '\r')
        log_file.close()

    def Logging(self, text):
        pass
## -----------------------------------------------------------------------------
class cDebugLogger(cLoggerBase):

    def __init__(self):
        super().__init__()

    def Logging(self, text):
        if self.log_enable == True:
            timestamp = datetime.datetime.now().strftime('[%d.%m.%YT%H.%M.%S.%f]: ')
            log_string = timestamp + self.__class__.__name__ + '.' + text
            print(log_string)
            self.LogToFile(log_string)
## -----------------------------------------------------------------------------
class cJsonLogger(cLoggerBase):
    def __init__(self):
        super().__init__()

    def Logging(self, data_dict):
        if self.log_enable == False:
            return
        if type(data_dict) is not dict:
            print('Error:' + self.__class__.__name__, '.Logging(data_dict): data_dict is not dict')
            return
        timestamp = datetime.datetime.now().strftime('[%d.%m.%YT%H.%M.%S.%f]')
        data_dict['TIME_STUMP'] = timestamp
        log_string = json.dumps(data_dict, ensure_ascii = False)
        self.LogToFile(log_string)
## -----------------------------------------------------------------------------

def main():
    dl = cDebugLogger()

    dl.LogToFile('test function LogToFile()')

    print('test function GetFileName():', dl.GetFileName())
    dl.Logging('self.log_enable = False')
    dl.LoggingSwitch(True)
    dl.Logging('test function Logging()')

    jl = cJsonLogger()
    jl.LoggingSwitch(True)
    jl.Logging('e')
    jl.Logging({'value1:':5, 'value2:':6})

## -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
