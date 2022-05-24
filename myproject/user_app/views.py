from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout


# from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if pass1 == pass2 and (len(pass1) > 4):
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
                return render(request, 'register.html')
            else:
            # Create the user
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                messages.success(request, " Your account has been successfully created")
                return redirect('/account/login')
        else:
            messages.error(request, "Passwords must be same and greater than five character")
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')
    # return HttpResponse("hii")

def loginp(request):
    if request.method == "POST":
          loginusername= request.POST['loginusername']
          password = request.POST['password']
          user = authenticate(username=loginusername, password=password)
          if user is not None:
               login(request, user)
               messages.success(request, "Successfully Logged In")
               return redirect("/webb")
          else:
               messages.error(request, "Invalid credentials! Please try again")
               return redirect("/account/login/")
    else:
        return render(request, 'login.html')
def logoutp(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/webb')

def mycourses(request):
    context={
            'welcome text':"Welcome to jnja2"
    }
    return render(request,"mycourses.html",context)