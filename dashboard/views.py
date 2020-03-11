import json
import smtplib
from django.db.models import Count
from datetime import datetime, timedelta, date
from calendar import monthrange
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from ipaddr import client_ip
from .models import Timesheet, EmployeePersonal, EmployeeProfessional, Login, Leave


###---helpers---###

def get_employee(request):
    emp_id = request.session['emp_id']
    employee = EmployeeProfessional.objects.get(emp_id = emp_id)
    return employee

def xxx(request):
    ipaddr = client_ip(request)
    return ipaddr

###---helpers---###


def res(request):
    rn = datetime.now()
    emp_id = request.session['emp_id']
    obj = Timesheet(emp_id = emp_id, start_time = rn)
    obj.save()
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


def home(request):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
       return redirect('dashboard')
    else:     
        return render(request, 'dashboard/login.html')


def login(request):
    session = request.session
    emp_email = request.POST['email']
    emp_pass = request.POST['password']
    IP = ['127.0.0.1']  #IP's here
    try:
        employee = EmployeeProfessional.objects.get(emp_email= emp_email)
        print('user exists')
        if employee.emp_pass == emp_pass:
            print('Password Matched!')
            name = employee.name['first'] + " " + employee.name['last']
            session['emp_id'] = employee.emp_id
            session['username'] = name
            emp_id = employee.emp_id
            ipaddr = xxx(request)
            last_login = datetime.now()
            if str(ipaddr) not in IP:
                return redirect('logout')
            else:
                l = Login(ip_addr=ipaddr, last_login=last_login, emp_id = emp_id)
                l.save()
                print("saved login info") 
                return redirect('dashboard')
        else:
            print('Sorry, Wrong Password')
            return redirect('home')
    except:
        print('Sorry, no user')
        return redirect('home')


def logout(request):
    session = request.session
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        del session['emp_id']
        del session['username']
    return redirect('home')


def dashboard(request):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        ipaddr = xxx(request)
        request.session['ip'] = ipaddr
        username = request.session['username']
        return render(request, 'dashboard/dashboard.html', {'ipaddr':ipaddr, 'username':username})
    else:
        return redirect('home')


def upload_file(request):
    file_objects = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['doc']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        employee = get_employee(request)
        file_objects = employee.files
        if file_objects:
            file_objects['objects'].append({'file_name':str(uploaded_file), 'file_url': str(fs.url(filename))})
            employee.files = file_objects
            employee.save()
        else:
            file_objects = {}
            file_objects['objects'] = []  
            file_objects['objects'].append({'file_name':str(uploaded_file), 'file_url': str(fs.url(filename))})
            employee.files = file_objects
            employee.save()
        return redirect('file_manager')


def file_manager(request):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        employee = get_employee(request)
        file_objects = employee.files
        if file_objects:
            files = file_objects['objects']
        else:
            files = {}
        return render(request, 'dashboard/files.html', {'files':files})
    else:
        return redirect('home')

def leave_query(request):
    head_count = 0
    if request.method == 'POST':
        start_date_string = request.POST['start_date']
        end_date_string = request.POST['end_date']
        start_date = date(*map(int, start_date_string.split('-')))
        end_date = date(*map(int, end_date_string.split('-')))
        tot_days = str(end_date - start_date).split(',')[0]
        no_of_days = int(tot_days.split()[0])


        employee = get_employee(request)

        total_employees = len(list(EmployeeProfessional.objects.filter(department = employee.department)))
        max_leave = int(total_employees/2)
        print('total employees in dept : ' + str(total_employees))
        print('max emp to go on leave: ' + str(max_leave))

        try:
            leaves = Leave.objects.filter(department = employee.department)
            leave_list = list(leaves)
            for x in leave_list:
                if x.emp_id == employee.emp_id and x.start_date < start_date < x.end_date:
                    print("Already you on leave")    ###########  UI  ###########
                    return redirect('events')
            
            for x in leave_list:
                if x.emp_id is not employee.emp_id and x.start_date < start_date < x.end_date:
                    head_count = head_count + 1
            
            print('head count of people actually on leave: '+ str(head_count))

            if head_count >= max_leave:
                # check_for_later()
                print("Can't grant leave, maintain minimum employee limit")
                return redirect('events')

            if employee.total_leaves >= no_of_days:
                print('Leave Granted')
                employee.total_leaves = employee.total_leaves - no_of_days
                l = Leave(emp_id = employee.emp_id, number_of_days = no_of_days, start_date = start_date, end_date = end_date)
                l.save()
                employee.save()
        except:
            print("Can't Fetch Right now, try later!")
    return redirect('events')


def events(request):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        return render(request, 'dashboard/events.html')
    else:
        return redirect('home')


def employees(request):
    employees = EmployeeProfessional.objects.all()
    leaves = Leave.objects.filter(start_date__lte=date.today(),end_date__gte=date.today())
    leave_list = [i.emp_id for i in leaves]
    return render(request, 'dashboard/employees.html', {'employees': employees, 'leave_list':leave_list})


def profile(request, id):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        professional = EmployeeProfessional.objects.get(emp_id = id)
        personal = EmployeePersonal.objects.get(emp_id = id)
        return render(request, 'dashboard/profile.html', {'professional':professional, 'personal':personal})
    else:
        return redirect('home')    

def mail(request):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        return render(request, 'dashboard/mail.html')
    else:
        return redirect('home')    

def send_mail(request):
    try:
        to = request.POST['to']
        subject = request.POST['subject']
        message = request.POST['message']
    except:
        print('Did not parse')
    email = get_employee(request).emp_email
    print(email)
    message = subject + message
    try:
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(email, '')
        smtpobj.sendmail(email, to, message)
        smtpobj.quit()
    except:
        print('Mail sending error')
    return redirect('email')

def departments(request):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        distinct = EmployeeProfessional.objects.all()
        depts= {}
        for i in distinct:
            if i.department not in depts:
                depts[i.department] = []
                depts[i.department].append(i)
            else:
                depts[i.department].append(i)
        print(depts)
        return render(request, 'dashboard/departments.html', {'depts' : depts})
    else:
        return redirect('home')    

def projects(request):
    if request.session.has_key('emp_id') and request.session.has_key('username'):
        p = EmployeeProfessional.objects.values('projects')
        emp = EmployeeProfessional.objects.exclude(projects__isnull = True)
        print(p)
        return render(request, 'dashboard/page_under_development.html')
    else:
        return redirect('home')    



def chat(request):
    return render(request, 'dashboard/page_under_development.html')

def holidays(request):
    return render(request, 'dashboard/page_under_development.html')

def leaves(request):
    return render(request, 'dashboard/page_under_development.html')

def attendance(request):
    return render(request, 'dashboard/page_under_development.html')


def designations(request):
    return render(request, 'dashboard/page_under_development.html')

def timesheet(request):
    return render(request, 'dashboard/page_under_development.html')

def overtime(request):
    return render(request, 'dashboard/page_under_development.html')

def clients(request):
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

def assets(request):
    return render(request, 'dashboard/page_under_development.html')

def jobs(request):
    return render(request, 'dashboard/page_under_development.html')

def applicants(request):
    return render(request, 'dashboard/page_under_development.html')
