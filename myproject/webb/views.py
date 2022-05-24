from django.shortcuts import render
from .models import Contact
from .models import Product
from math import ceil
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
            'welcome text':"Welcome to jnja2"
    }
    return render(request,"index.html",context)
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        subject = request.POST['subject']
        if len(name) < 2 or len(email) < 3 or len(subject) < 5 or len(desc) < 4:
            messages.error(request, "Please fill the form correctly")

        else:
            contact = Contact(name=name, email=email,desc=desc,subject=subject)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "contact.html")
        # print(name,email,desc,subject)
    # context={
    #         'welcome text':"Welcome to jnja2"
    # }

def about(request):
    context={
            'welcome text':"Welcome to jnja2"
    }
    return render(request,"about.html",context)
def courses(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request,"courses.html",params)

def listcourse(request):
    return render(request,"listcourse.html")

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'prodView.html', {'product':product[0]})

def payment(request):
    return render(request,"payment.html")


def debitpay(request):
    return render(request,"debitpay.html")
