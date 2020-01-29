from django.db import models
from django.contrib.postgres.fields import JSONField


class EmployeePersonal(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = JSONField()
    birth_date = models.DateField(blank=True, null=True)
    contact_no = models.BigIntegerField(blank=True, null=True)
    emergency = JSONField()
    education = JSONField()
    links = JSONField()
    emp_email = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_personal'


class EmployeeProfessional(models.Model):
    emp = models.ForeignKey(EmployeePersonal, models.DO_NOTHING, primary_key=True)
    emp_pass = models.CharField(max_length=256, blank=True, null=True)
    name = JSONField()
    date_of_joining = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    parent = JSONField()
    child = JSONField()
    activity = JSONField()
    position = models.CharField(max_length=50, blank=True, null=True)
    emp_email = models.CharField(max_length=75, blank=True, null=True)
    files = JSONField()

    class Meta:
        managed = False
        db_table = 'employee_professional'


class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(EmployeeProfessional, models.DO_NOTHING, blank=True, null=True)
    name = JSONField()
    number_of_days = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave'


class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    ip_addr = models.GenericIPAddressField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    emp = models.ForeignKey(EmployeeProfessional, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class PayInfo(models.Model):
    emp = models.ForeignKey(EmployeeProfessional, models.DO_NOTHING, primary_key=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    bank_ac_no = models.BigIntegerField(blank=True, null=True)
    pf_uan = models.BigIntegerField(blank=True, null=True)
    pan_no = models.CharField(max_length=10, blank=True, null=True)
    esi_no = models.CharField(max_length=20, blank=True, null=True)
    gross_pay = models.SmallIntegerField(blank=True, null=True)
    net_pay = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_info'


class Timesheet(models.Model):
    timesheet_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(EmployeeProfessional, models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timesheet'
