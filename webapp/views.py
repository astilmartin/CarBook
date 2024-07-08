from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from backend.models import cardb, productdb
from webapp.models import registerdb, bookdb


# Create your views here.
def homepage(request):
    car=cardb.objects.all()
    pro=productdb.objects.all()
    return render(request,"home.html",{'car':car,'pro':pro})

def aboutpage(request):
    return render(request,"about.html")

def contactpage(request):
    return render(request,"contact.html")

def servicepage(request):
    return render(request,"services.html")

def pricepage(request):
    car = cardb.objects.all()
    pro = productdb.objects.all()
    return render(request,"pricing.html",{'car':car,'pro':pro})

def carspage(request):
    car=cardb.objects.all()
    pro = productdb.objects.all()
    return render(request,"vehicles.html",{'car':car,'pro':pro})


def filtered_brands(request,car_name):
    car=cardb.objects.filter(Brand=car_name)
    pro=productdb.objects.all()
    return render(request,"brand_filter.html",{'car':car,'pro':pro})

def singlepage(request,carid):
    car=cardb.objects.get(id=carid)
    return render(request,"single_car.html",{'car':car})


def register_page(request):
    return render(request,"register.html")



def save_register(request):
    if request.method=="POST":
        us=request.POST.get('user')
        em=request.POST.get('email')
        pa=request.POST.get('pass')
        im=request.FILES['img']
        obj=registerdb(Username=us,Email=em,Password=pa,User_image=im)
        if registerdb.objects.filter(Username=us).exists():
            messages.warning(request,"Username already exists..!!")
            return redirect(register_page)
        elif registerdb.objects.filter(Email=em).exists():
            messages.warning(request,"Email ID already exists...!!")
            return redirect(register_page)
        else:
            obj.save()
            messages.success(request,"Registered Successfully..!!")
        return redirect(user_login_page)


def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pas=request.POST.get('password')
        if registerdb.objects.filter(Username=un,Password=pas).exists():
            request.session['Username']=un
            request.session['Password']=pas
            return redirect(homepage)
        else:
            return redirect(register_page)
    else:
        return redirect(register_page)


def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(homepage)

def user_login_page(request):
    return render(request,"user_login.html")


def booking_page(request,carid):
    car = cardb.objects.get(id=carid)
    data = registerdb.objects.get(Username=request.session['Username'])
    return render(request,"booking.html",{'car':car,"data":data})


def save_booking(request,carid):
    if request.method=="POST":
        up=request.POST.get('pup')
        off=request.POST.get('doff')
        pd=request.POST.get('pdate')
        dd=request.POST.get('ddate')
        pt=request.POST.get('ptime')
        un=request.POST.get('uname')
        try:
            img = request.FILES['uimg']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = registerdb.objects.get(Username=request.session['Username']).User_image
        try:
            cim = request.FILES['cimg']
            fs = FileSystemStorage()
            cfile = fs.save(cim.name, cim)
        except MultiValueDictKeyError:
            cfile = cardb.objects.get(id=carid).Car_Image
        obj=bookdb(Pickup=up,Dropoff=off,Pickup_date=pd,Dropoff_date=dd,Pickup_time=pt,Username=un,User_Image=file,Car_image=cfile)
        obj.save()
        messages.success(request, "Successful")
        return redirect(bookpage)


def bookpage(request):
    data=bookdb.objects.filter(Username=request.session['Username'])
    return render(request,"user_booking.html",{'data':data})