from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib.auth import authenticate, load_backend, login, logout



class Admin_login(View):
    def post(self,request):
        if request.method == 'POST':
            username = request.POST['aname']
            password = request.POST['psswd']   
            user = authenticate(username=username, password=password) 
            print("AAYA1")
            try:
                # if user.is_staff:
                    login(request, user)
                    return redirect('home')    # Redirect to a success page.   
                # else:
                #     # message = messages.error(request, 'Sorry you are not an admin')
                #     message= "Sorry you are not authoirized to login as admin Stay In your Limits !!"
                #     return render(request, 'admin_login.html',{'message':message})
  
            except Exception as e: 
                # message = messages.error(request, 'Invalid Username or Password')
                message = "Invalid Username or Password"
                return render(request, 'admin_login.html',{'message':message})
                       
    def get(self,request):
        return render(request,'admin_login.html')


class Logout(View): 
    def get(self,request):
        logout(request)
        return redirect('/')
        



class Home(View):
    
    def get(self,request):
        if request.user.is_authenticated:   
            user = request.user
            print("HAHAHAHAHAHHAAH",user) 
            usr = Employee.objects.filter(email=user).first()
            print("USDDDD",usr)
            return render(request,'home.html',{'user':user,'emp':usr})
        else:
            return render(request,'admin_login.html')


def product_list(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            product = Product.objects.get(id=id)

            product.name = request.POST.get('name')
            # product.date = request.POST.get('date')
            product.version = request.POST.get('version')
            product.release = request.POST.get('release')
            product.save()
            print("KEEEMA Paratha")
            return redirect('product_list')
        except Exception as e:
            print("KAAABBABB",e)
    products = Product.objects.all()
    return render(request, 'product_list.html',{'products': products})

def product(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        date = request.POST.get('date')
        version = request.POST.get('version')
        release = request.POST.get('release')
        Product.objects.create(name=name, date=date, version=version, release=release)
        return redirect('product_list')
    # product = Product.objects.get(pk=pk)
    return render(request, 'product_add.html')
    # return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        version = request.POST.get('version')
        Product.objects.create(name=name, date=date, version=version)
        return redirect('product_list')
    return render(request, 'product_create.html')

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.date = request.POST.get('date')
        product.version = request.POST.get('version')
        product.save()
        return redirect('product_detail', pk=pk)
    return render(request, 'product_update.html', {'product': product})

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')


def employee_list(request):
    if request.method == 'POST':
        # try:
        print("request.POST.get('area_id')",request.POST.get('emp_id'),request.POST.get('name'))
        emp_id = request.POST.get('emp_id')
        obj = Employee.objects.get(emp_id=emp_id)
    
        print('looooooooooooooooo',obj)
        obj.user_level = request.POST.get('user_level')
        print('USER LEVEL UPDATED')
        obj.save()
        return redirect('employee_list')
    
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        print("LAAAALALALALA")
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_level = request.POST.get('user_level')
        password = request.POST.get('password')
        level = request.POST.get('level')
        user = User.objects.create_user(first_name=name,username=email,password=password,email=email)
        Employee.objects.create(name=name, email=email, user_level=user_level,password=password,level=level)
        user = authenticate(username=email, password=password)
        login(request, user)
                        
        print("LAAAALALALALA")

        return redirect('employee_list')
    return render(request, 'employee_create.html')

def employee_update(request):
    
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        employee = Employee.objects.get(emp_id=emp_id)
        print("^^^^^^^",employee)
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.user_level = request.POST.get('user_level')
        employee.level = request.POST.get('level')
        employee.save()
        return redirect('employee_list')
    return render(request, 'employee_update.html', {'employee': employee})

def employee_delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('employee_list')



def bug_list(request):
    bugs = Bugs.objects.all()
    return render(request, 'bug_list.html', {'bugs': bugs})

def bug_detail(request, pk):
    bug = Bugs.objects.get(pk=pk)
    return render(request, 'bug_detail.html', {'bug': bug})

def bug_create(request):
    if request.method == 'POST':
        print('looooooooooooooooo',request.POST)
        program = request.POST.get('program')
        report_type = request.POST.get('report_type')
        problem_summary = request.POST.get('problem_summary')
        problem = request.POST.get('problem')
        suggested_fix = request.POST.get('suggested_fix')
        reproducible = request.POST.get('reproducible',1)
        report_by = Employee.objects.get(name=request.POST.get('report_by'))
        date = request.POST.get('date')
        functional_area = request.POST.get('functional_area')
        assigned_to = Employee.objects.get(name=request.POST.get('assigned_to'))
        comment = request.POST.get('comment')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        resolution = request.POST.get('resolution')
        resolved_by = Employee.objects.get(name=request.POST.get('resolved_by'))
        tested_by = request.POST.get('tested_by')
        product = Product.objects.get(name=request.POST.get('product'))
        # created_by = Employee.objects.get(name=request.POST.get('created_by'))
        
        Bugs.objects.create(
            program=program,
            report_type=report_type,
            problem_summary=problem_summary,
            problem=problem,
            suggested_fix=suggested_fix,
            reproducible=reproducible,
            report_by=report_by,
            date=date,
            functional_area=functional_area,
            assigned_to=assigned_to,
            comment=comment,
            status=status,
            priority=priority,
            resolution=resolution,
            resolved_by=resolved_by,
            tested_by=tested_by,
            product=product,
            # created_by=created_by
        )
        return redirect('bug')
        
    employees = Employee.objects.all()
    products = Product.objects.all()
    tester = Employee.objects.filter(user_level='Tester')
    print("TESTER---",tester)
    return render(request, 'bug_create.html', {'employees': employees, 'products': products})

def bug_update(request, pk):
    bug = Bugs.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            print('looooooooooooooooo',request.POST)
            bug.program = request.POST.get('program')
            bug.report_type = request.POST.get('report_type')
            bug.problem_summary = request.POST.get('problem_summary')
            bug.problem = request.POST.get('problem')
            bug.suggested_fix = request.POST.get('suggested_fix')
            bug.reproducible = request.POST.get('reproducible')
            bug.report_by = Employee.objects.get(name=request.POST.get('report_by'))
            bug.date = request.POST.get('date')
            bug.functional_area = request.POST.get('functional_area')
            bug.assigned_to = Employee.objects.get(name=request.POST.get('assigned_to'))
            bug.comment = request.POST.get('comment')
            bug.status = request.POST.get('status')
            bug.priority = request.POST.get('priority')
            bug.resolution = request.POST.get('resolution')
            bug.resolved_by = Employee.objects.get(name=request.POST.get('resolved_by'))
            bug.tested_by = request.POST.get('tested_by')
            bug.product = Product.objects.get(name=request.POST.get('product'))
            # bug.created_by = Employee.objects.get(name=request.POST.get('created_by'))
            
            bug.save()
            return redirect('bug')
        except Exception as e:
            print("ERROR"*300,e)

    employees = Employee.objects.all()
    products = Product.objects.all()
    print("BUG---->>>",bug.__dict__)
    return render(request, 'bug_update.html', {'bug': bug, 'employees': employees, 'products': products})

def bug_delete(request, pk):
    bug = Bugs.objects.get(pk=pk)
    bug.delete()
    return redirect('bug')


def database_managment(request):
    print("KAAAAAS")
    return render(request,'database_managment.html')

def add_area(request):
    if request.method == 'POST':
        name = request.POST.get('area_name')
        areas = request.POST.get('area')
        Area.objects.create(area_name=name,areas=areas)
        return redirect('area_list')
    areas = Area.objects.all()
    print("AREAAAAA",areas)
    return render(request, 'area_list.html', {'areas':areas})
    # return render(request, 'area_list.html')


def area(request):
    if request.method == 'POST':
        # try:
        print("request.POST.get('area_id')",request.POST.get('area_id'),request.POST.get('area_name'))
        area_id = request.POST.get('area_id')
        obj = Area.objects.get(area_id=area_id)
    
        print('looooooooooooooooo',obj)
        obj.area_name = request.POST.get('area_name')
        obj.areas = request.POST.get('area')
        print('AREA SAVED')
        obj.save()
        return redirect('area_list')
        # except Exception as e:
        #     print("ERROR",e)
    areas = Area.objects.all()
    # print("AREAAAAA-----",areas)
    return render(request, 'area_list.html', {'areas':areas})
