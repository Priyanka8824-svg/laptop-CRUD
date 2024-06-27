from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm

# Create your views here.
def hview(request):

    return render(request,"app1/home.html",{})

def lview(request):
    form = LaptopForm()
    if request.method == "POST":
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/laptop_add.html",{"form":form})

def sview(request):
    laptop = Laptop.objects.all()
    print(laptop)
    return render(request,"app1/show.html",{"obj":laptop})

def updateview(request,pk):
    obj = Laptop.objects.get(lid=pk)
    form = LaptopForm(instance=obj)
    if request.method == "POST":
        form = LaptopForm(request.POST,instance=obj)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/laptop_add.html",{"form":form})

def deleteview(request,x):
## directly delete record ##
    # obj = Laptop.objects.get(lid=x)
    # obj.delete()
    # return redirect("/a1/sv/")

## confirm page ##
    obj = Laptop.objects.get(lid=x)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})