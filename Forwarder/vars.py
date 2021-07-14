from Forwarder.vardb import *

class dbvars():
    def __init__(self):
        if find_variable('STATUS'):
            self.STATUS = get_variable('STATUS')
        else:
            add_variable('STATUS', 'stopped')
            self.STATUS = 'stopped'

        if find_variable('TIME'):
            self.TIME = get_variable('TIME')
        else:
            add_variable('TIME', '00')
            self.TIME = '00'

        if find_variable('FROM'):
            self.FROM = get_variable('FROM')
        else:
            add_variable('FROM', '0')
            self.FROM = '0'

        if find_variable('TO'):
            self.TO = get_variable('TO')
        else:
            add_variable('TO', '0')
            self.TO = '0'

        if find_variable('FROM_MSG'):
            self.FROM_MSG = get_variable('FROM_MSG')
        else:
            add_variable('FROM_MSG', '0')
            self.FROM_MSG = '0'

        if find_variable('TO_MSG'):
            self.TO_MSG = get_variable('TO_MSG')
        else:
            add_variable('TO_MSG', '0')
            self.TO_MSG = '0'

        if find_variable('LAST'):
            self.LAST = get_variable('LAST')
        else:
            add_variable('LAST', '0')
            self.LAST = '0'

        if find_variable('ALL'):
            self.ALL = get_variable('ALL')
        else:
            add_variable('ALL', '0')
            self.ALL = '0'

        if find_variable('PHOTO'):
            self.PHOTO = get_variable('PHOTO')
        else:
            add_variable('PHOTO', '0')
            self.PHOTO = '0'

        if find_variable('VIDEO'):
            self.VIDEO = get_variable('VIDEO')
        else:
            add_variable('VIDEO', '0')
            self.VIDEO = '0'

        if find_variable('AUDIO'):
            self.AUDIO = get_variable('AUDIO')
        else:
            add_variable('AUDIO', '0')
            self.AUDIO = '0'

        if find_variable('DOCUMENT'):
            self.DOCUMENT = get_variable('DOCUMENT')
        else:
            add_variable('DOCUMENT', '0')
            self.DOCUMENT = '0'

        if find_variable('TEXT'):
            self.TEXT = get_variable('TEXT')
        else:
            add_variable('TEXT', '0')
            self.TEXT = '0'

        if find_variable('TAG'):
            self.TAG = get_variable('TAG')
        else:
            add_variable('TAG', 'copy')
            self.TAG = 'copy'

        if find_variable('COUNT'):
            self.COUNT = get_variable('COUNT')
        else:
            add_variable('COUNT', '0')
            self.COUNT = '0'

    def get(self,var):
        return vars(self)[var]

    def put(self,var,value):
        vars(self)[var] = value
        edit_variable(var,value)

    def temp(self):
        return vars(self)


db = dbvars()