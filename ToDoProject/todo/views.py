from django.shortcuts import render,redirect
from todo.models import Task
# Create your views here.
def add(request):
    if (request.method=="post"):
        Heading_ =request.post['Heading']
        Details_ =request.post['Details']
        Date_ =request.post['Date']
        print(Heading_)
        print(Details_)
        print(Date_)

        insert_data = Task.objects.Create(Heading=Heading_, Details= Details_, Date=Date_,)

        insert_data.save()
        return redirect("/")
    return render(request,'todo/add.html')

def index(request):
    content={}
    #content[data]=Task.objects.all()
    content[data]=Task.objects.filter(is_deleted="n")
    return render(request,'todo/index.html',content)

def delete(request,tid):
    record_to_be_deleted =Task.objects.filter(id=tid)
    #record_to_be_deleted.delete()
    record_to_be_deleted.update(is_deleted="y")
    return redirect("/")

def update(request,tid):
    if (request.method=="post"):
        Heading_ =request.post['Heading']
        Details_ =request.post['Details']
        Date_ =request.post['Date']
        record_to_be_update=Task.objects.filter(id=tid)
        record_to_be_update=update(Heading=Heading_, Details= Details_, Date=Date_,)
        return render(request,'todo/update.html',content)
        return redirect("/")
    else:
        content={}
        content[data]=Task.objects.get(id=tid)
        return render(request,'todo/update.html',content)
