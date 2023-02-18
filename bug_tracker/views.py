from django.shortcuts import render, redirect
from .models import Bug

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bug_tracker/bug_list.html', {'bugs': bugs})

def bug_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        severity = request.POST['severity']
        bug = Bug(title=title, description=description, severity=severity)
        bug.save()
        return redirect('bug_list')
    return render(request, 'bug_tracker/bug_form.html')

def bug_update(request, pk):
    bug = Bug.objects.get(pk=pk)
    if request.method == 'POST':
        bug.title = request.POST['title']
        bug.description = request.POST['description']
        bug.severity = request.POST['severity']
        bug.save()
        return redirect('bug_list')
    return render(request, 'bug_tracker/bug_form.html', {'bug': bug})

def bug_delete(request, pk):
    bug = Bug.objects.get(pk=pk)
    bug.delete()
    return redirect('bug_list')
