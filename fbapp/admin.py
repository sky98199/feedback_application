from django.contrib import admin

from .models import FbModel

class FbAdmin(admin.ModelAdmin):
	list_display=('name','cr_dt')
	list_filter=('cr_dt',)
admin.site.register(FbModel,FbAdmin)
