from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Employee, Bugs




def product_list(request):
    products = Product.objects.all()
    return render(request, 'base.html', {'products': 'products'})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

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
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_level = request.POST.get('user_level')
        Employee.objects.create(name=name, email=email, user_level=user_level)
        return redirect('employee_list')
    return render(request, 'employee_create.html')

def employee_update(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.user_level = request.POST.get('user_level')
        employee.save()
        return redirect('employee_detail', pk=pk)
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
        program = request.POST.get('program')
        report_type = request.POST.get('report_type')
        problem_summary = request.POST.get('problem_summary')
        problem = request.POST.get('problem')
        suggested_fix = request.POST.get('suggested_fix')
        reproducible = request.POST.get('reproducible')
        report_by = Employee.objects.get(pk=request.POST.get('report_by'))
        date = request.POST.get('date')
        functional_area = request.POST.get('functional_area')
        assigned_to = Employee.objects.get(pk=request.POST.get('assigned_to'))
        comment = request.POST.get('comment')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        resolution = request.POST.get('resolution')
        resolved_by = Employee.objects.get(pk=request.POST.get('resolved_by'))
        tested_by = request.POST.get('tested_by')
        product = Product.objects.get(pk=request.POST.get('product'))
        created_by = Employee.objects.get(pk=request.POST.get('created_by'))
        
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
            created_by=created_by
        )
        return redirect('bug_list')
        
    employees = Employee.objects.all()
    products = Product.objects.all()
    return render(request, 'bug_create.html', {'employees': employees, 'products': products})

def bug_update(request, pk):
    bug = Bugs.objects.get(pk=pk)
    if request.method == 'POST':
        bug.program = request.POST.get('program')
        bug.report_type = request.POST.get('report_type')
        bug.problem_summary = request.POST.get('problem_summary')
        bug.problem = request.POST.get('problem')
        bug.suggested_fix = request.POST.get('suggested_fix')
        bug.reproducible = request.POST.get('reproducible')
        bug.report_by = Employee.objects.get(pk=request.POST.get('report_by'))
        bug.date = request.POST.get('date')
        bug.functional_area = request.POST.get('functional_area')
        bug.assigned_to = Employee.objects.get(pk=request.POST.get('assigned_to'))
        bug.comment = request.POST.get('comment')
        bug.status = request.POST.get('status')
        bug.priority = request.POST.get('priority')
        bug.resolution = request.POST.get('resolution')
        bug.resolved_by = Employee.objects.get(pk=request.POST.get('resolved_by'))
        bug.tested_by = request.POST.get('tested_by')
        bug.product = Product.objects.get(pk=request.POST.get('product'))
        bug.created_by = Employee.objects.get(pk=request.POST.get('created_by'))
        
        bug.save()
        return redirect('bug_detail', pk=pk)
        
    employees = Employee.objects.all()
    products = Product.objects.all()
    return render(request, 'bug_update.html', {'bug': bug, 'employees': employees, 'products': products})

def bug_delete(request, pk):
    bug = Bugs.objects.get(pk=pk)
    bug.delete()
    return redirect('bug_list')

