from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from backend.models import productdb, cardb
from django.contrib import messages


# Create your views here.

def main_page(request):
    return render(request, "index.html")


def new_page(request):
    return render(request, "add_brand.html")




def details_page(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        img = request.FILES['img']
        obj = productdb(Name=na, Details=de, Image=img)
        obj.save()
        messages.success(request, "Brand saved successfully")
        return redirect(new_page)


def Show_product(request):
    data = productdb.objects.all()
    return render(request, "show_brands.html", {'data': data})


def edit_page(req, proid):
    data = productdb.objects.get(id=proid)
    return render(req, "edit.html", {'data': data})


def update_product(request, proid):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=proid).Image
        productdb.objects.filter(id=proid).update(Name=na, Details=de, Image=file)
        messages.success(request, "Updated successfully")
        return redirect(Show_product)


def delete_product(req, proid):
    x = productdb.objects.filter(id=proid)
    x.delete()
    messages.error(req, "Deleted successfully")
    return redirect(Show_product)


def login_page(request):
    return render(request, "login.html")


def admin_login(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pa = request.POST.get("password")
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pa)
            if x is not None:
                login(request, x)
                request.session["username"] = un
                request.session["password"] = pa
                messages.success(request, "Login successful")
                return redirect(main_page)
            else:
                messages.error(request, "Invalid password")
                return redirect(login_page)
        else:
            messages.warning(request, "Invalid user")
            return redirect(login_page)


def admin_logout(request):
    del request.session["username"]
    del request.session["password"]
    messages.success(request, "Logout successful")
    return redirect(login_page)


def car_page(req):
    bar = productdb.objects.all()
    return render(req, "cars.html", {'bar': bar})


def cdetails_page(request):
    if request.method == "POST":
        bar = request.POST.get('brand')
        c_na = request.POST.get('cname')
        pr = request.POST.get('price')
        c_de = request.POST.get('cdescription')
        c_img = request.FILES['cimg']
        obj = cardb(Brand=bar, Car_Name=c_na, Car_price=pr, C_Description=c_de, Car_Image=c_img)
        obj.save()
        messages.success(request, "Saved successfully")
        return redirect(car_page)


def show_cars(request):
    data = cardb.objects.all()
    return render(request, "show_car.html", {'data': data})


def edit_cars(req, carid):
    data = cardb.objects.get(id=carid)
    cat = productdb.objects.all()
    return render(req, "edit_cars.html", {'data': data, 'cat': cat})


def update_cars(request, carid):
    if request.method == "POST":
        ca = request.POST.get('bname')
        pn = request.POST.get('p_name')
        pp = request.POST.get('price')
        pd = request.POST.get('p_description')
        try:
            img = request.FILES['p_img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = cardb.objects.get(id=carid).Car_Image
        cardb.objects.filter(id=carid).update(Brand=ca, Car_Name=pn, Car_price=pp, C_Description=pd, Car_Image=file)
        messages.success(request, "Updated successfully")
        return redirect(show_cars)


def delete_cars(req, carid):
    x = cardb.objects.filter(id=carid)
    x.delete()
    messages.error(req, "Deleted successfully")
    return redirect(show_cars)