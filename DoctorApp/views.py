from django.shortcuts import render,redirect
from DoctorApp.models import Doctor
from DoctorApp.forms import DoctorForm
# Create your views here.

def doc(request):
    
    if request.method == "POST":
                       
        form = DoctorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
                
            except:
                pass    
    else:
        form = DoctorForm()

    return render(request,'index.html',{'form':form})    

def show(request):
    docs = Doctor.objects.all()

    return render(request,'show.html',{'docs':docs})    


def edit(request,id):
    data = Doctor.objects.get(id = id)
    return render(request,'edit.html',{'data':data})


def update(request, id):
    if request.method =='POST':
        data = Doctor.objects.get(id=id)
        #print(data)
        form = DoctorForm(request.POST, instance = data)
        p = form.is_valid()
        #print('in this update',p)
        
        if form.is_valid():

            #print('hello')
            form.save()    
            return redirect("/show")

    return render(request,'edit.html',{'data':data})

def destroy(request, id):
    data = Doctor.objects.get(id = id)
    data.delete()
    return redirect("/show")    