from django.contrib import admin
from .models import Operation


# Register your models here.

class OperationAdmin(admin.ModelAdmin):
    list_display = ('x_value', 'y_value', 'op', 'result', 'user')
    list_filter = ('op', 'user')
    raw_id_fields = ('user',)

admin.site.register(Operation, OperationAdmin)