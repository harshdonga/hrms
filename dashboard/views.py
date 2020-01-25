import json
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ipaddr import client_ip
from .models import Timesheet

def res(request):
    rn = datetime.now()
    obj = Timesheet(emp_id = 1, start_time = rn)
    obj.save()
    print(obj.timesheet_id)
    request.session['timesheet_id'] = obj.timesheet_id
    data = {}
    data['result'] = 'Request made for time in'
    return HttpResponse(json.dumps(data), content_type="application/json")

def res2(request):
    rn = datetime.now()
    obj = Timesheet.objects.get(timesheet_id = request.session['timesheet_id'])
    obj.end_time = rn
    obj.save()
    data = {}
    data['result'] = 'Request made for time out'
    return HttpResponse(json.dumps(data), content_type="application/json")    


def xxx(request):
    ipaddr = client_ip(request)
    return ipaddr

def login(request):
    print('-'*20)
    print(dir(request.session))
    return redirect('/dashboard')


@login_required(login_url = '/login')
def dashboard(request):
    ipaddr = xxx(request)
    return render(request, 'dashboard/dashboard.html', {'ipaddr':ipaddr})

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
