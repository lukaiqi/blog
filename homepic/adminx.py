import xadmin
from .models import Homepic


# Register your models here.
class HomepicAdmin(object):
    list_display = ['id','url', 'add_time']


xadmin.site.register(Homepic, HomepicAdmin)
