from django.shortcuts import render
from django.http import HttpResponse
from ipaddr import client_ip


def xxx(request):
    ipaddr = client_ip(request)
    return ipaddr

def admin_dashboard(request):
    ipaddr = xxx(request)
    return render(request, 'dashboard/admin_dashboard.html', {'ipaddr':ipaddr})

def employee_dashboard(request):
    return render(request, 'dashboard/page_under_development.html')

def chat(request):
    return render(request, 'dashboard/page_under_development.html')

def events(request):
    return render(request, 'dashboard/page_under_development.html')

def file_manager(request):
    return render(request, 'dashboard/page_under_development.html')

def employees(request):
    return render(request, 'dashboard/page_under_development.html')

def holidays(request):
    return render(request, 'dashboard/page_under_development.html')

def leaves(request):
    return render(request, 'dashboard/page_under_development.html')

def attendance(request):
    return render(request, 'dashboard/page_under_development.html')

def departments(request):
    return render(request, 'dashboard/page_under_development.html')

def designations(request):
    return render(request, 'dashboard/page_under_development.html')

def timesheet(request):
    return render(request, 'dashboard/page_under_development.html')

def overtime(request):
    return render(request, 'dashboard/page_under_development.html')

def clients(request):
    return render(request, 'dashboard/page_under_development.html')

def projects(request):
    return render(request, 'dashboard/page_under_development.html')

def tasks(request):
    return render(request, 'dashboard/page_under_development.html')

def leads(request):
    return render(request, 'dashboard/page_under_development.html')

def estimates(request):
    return render(request, 'dashboard/page_under_development.html')

def invoices(request):
    return render(request, 'dashboard/page_under_development.html')

def payments(request):
    return render(request, 'dashboard/page_under_development.html')

def expenses(request):
    return render(request, 'dashboard/page_under_development.html')

def taxes(request):
    return render(request, 'dashboard/page_under_development.html')

def salary(request):
    return render(request, 'dashboard/page_under_development.html')

def payslip(request):
    return render(request, 'dashboard/page_under_development.html')

def payroll(request):
    return render(request, 'dashboard/page_under_development.html')

def expense_reports(request):
    return render(request, 'dashboard/page_under_development.html')

def invoice_reports(request):
    return render(request, 'dashboard/page_under_development.html')

def performance(request):
    return render(request, 'dashboard/page_under_development.html')

def performance_appraisal(request):
    return render(request, 'dashboard/page_under_development.html')

def goals(request):
    return render(request, 'dashboard/page_under_development.html')

def training_list(request):
    return render(request, 'dashboard/page_under_development.html')

def trainers(request):
    return render(request, 'dashboard/page_under_development.html')

def promotion(request):
    return render(request, 'dashboard/page_under_development.html')

def resignation(request):
    return render(request, 'dashboard/page_under_development.html')

def termination(request):
    return render(request, 'dashboard/page_under_development.html')

def assets(request):
    return render(request, 'dashboard/page_under_development.html')

def jobs(request):
    return render(request, 'dashboard/page_under_development.html')

def applicants(request):
    return render(request, 'dashboard/page_under_development.html')
