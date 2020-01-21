from django.contrib import admin
from .models import EmployeePersonal, EmployeeProfessional, Leave, Login, PayInfo, Timesheet
from django.contrib.postgres.fields import JSONField
from django_json_widget.widgets import JSONEditorWidget


@admin.register(EmployeePersonal)
class EmployeePersonalAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'name', 'birth_date')
    ordering = ('emp_id',)
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(EmployeeProfessional)
class EmployeeProfessionalAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'name', 'department', 'position', 'date_of_joining')
    ordering = ('emp_id', 'department',)
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('leave_id', 'emp_id', 'name', 'number_of_days', 'start_date')
    ordering = ('start_date',) 
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('login_id', 'emp_id', 'ip_addr', 'last_login')
    ordering = ('last_login',)


@admin.register(PayInfo)
class PayInfoAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'net_pay')
    ordering = ('emp_id',)

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('timesheet_id', 'emp_id', 'start_time', 'end_time')
    ordering = ('emp_id','start_time',)