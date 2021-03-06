from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.home, name = 'home'),
    path('login',views.login, name = 'login'),
    path('logout',views.logout, name = 'logout'),
    path('dashboard',views.dashboard, name = 'dashboard'),
    path('chat',views.chat, name = 'chat'),
    path('events',views.events, name = 'events'),
    path('leave_query', views.leave_query, name = 'leave_query'),
    path('upload_file',views.upload_file, name = 'upload_file'),
    path('file_manager',views.file_manager, name = 'file_manager'),
    path('employees',views.employees, name = 'employees'),
    path('employees/<int:id>', views.profile, name = 'profile'),
    path('mail', views.mail, name = 'mail'),
    path('send_mail', views.send_mail, name = 'send_mail'),
    path('holidays',views.holidays, name = 'holidays'),
    path('leaves',views.leaves, name = 'leaves'),
    path('calendar', views.calendar, name = 'calendar'),
    path('attendance',views.attendance, name = 'attendance'),
    path('departments',views.departments, name = 'departments'),
    path('designations',views.designations, name = 'designations'),
    path('timesheet',views.timesheet, name = 'timesheet'),
    path('overtime',views.overtime, name = 'overtime'),
    path('clients',views.clients, name = 'clients'),
    path('projects',views.projects, name = 'projects'),
    path('tasks',views.tasks, name = 'tasks'),
    path('leads',views.leads, name = 'leads'),
    path('estimates',views.estimates, name = 'estimates'),
    path('invoices',views.invoices, name = 'invoices'),
    path('payments',views.payments, name = 'payments'),
    path('expenses',views.expenses, name = 'expenses'),
    path('taxes',views.taxes, name = 'taxes'),
    path('salary',views.salary, name = 'salary'),
    path('payslip',views.payslip, name = 'payslip'),
    path('payroll',views.payroll, name = 'payroll'),
    path('expense_reports',views.expense_reports, name = 'expense_reports'),
    path('invoice_reports',views.invoice_reports, name = 'invoice_reports'),
    path('performance',views.performance, name = 'performance'),
    path('performance_appraisal',views.performance_appraisal, name = 'performance_appraisal'),
    path('goals',views.goals, name = 'goals'),
    path('training_list',views.training_list, name = 'training_list'),
    path('trainers',views.trainers, name = 'trainers'),
    path('promotion',views.promotion, name = 'promotion'),
    path('resignation',views.resignation, name = 'resignation'),
    path('assets',views.assets, name = 'assets'),
    path('jobs',views.jobs, name = 'jobs'),
    path('applicants',views.applicants, name = 'applicants'),
    path('res', views.res , name = 'res'),
    path('res2', views.res2, name='res2'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)