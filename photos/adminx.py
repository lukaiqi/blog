import xadmin
from .models import Photo


class PhotoAdmin(object):
    list_display = ['url', "add_time"]


xadmin.site.register(Photo, PhotoAdmin)
