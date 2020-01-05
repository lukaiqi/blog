import xadmin
from .models import Sensor


class SensorAdmin(object):
    list_display = ['temperature', 'humidity', "illumination", 'pressure', 'altitude', 'add_time']


xadmin.site.register(Sensor, SensorAdmin)
