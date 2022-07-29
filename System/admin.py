from django.contrib import admin
from import_export.admin import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Upload2)
class Upload2Admin(ImportExportModelAdmin):
    list_display=('batch','sdiv','cnum','roll_no','Sname','Ph_no')


admin.site.register(Upload)
admin.site.register(faculty)
admin.site.register(attendance)