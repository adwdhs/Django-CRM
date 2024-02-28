from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from .models import Record
@login_required(login_url='login')
def index(request):
    records = Record.objects.filter(user=request.user)

    context = {
        'records': records,


    }
    return render(request, 'index.html', context)


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if len(password) < 6:
                messages.error(request, 'Incorrect Username or Password')
                return redirect('login')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if user.is_authenticated:
                    messages.success(request, 'You Have Been Logged In')
                    return redirect('index')
                else:
                    messages.error(request, 'Incorrect Username or Password')
                    return redirect('login')
            else:
                messages.error(request, 'An Error Occurred, Please Try Again')
                return redirect('login')




def logoutUser(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out')
    return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            context = {
                'username': username,
                'email': email,
            }
            if password2 == password1:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        if len(password1) < 6:
                            messages.error(request, 'Password is Too Short')
                            return render(request, 'register.html', context)

                        user = User.objects.create_user(username=username, email=email)
                        user.set_password(password1)
                        user.save()
                        messages.success(request, 'Account Created Successfully')
                        return redirect('login')
            else:
                messages.error(request, "Passwords don't match")
                return render(request, 'register.html', context)

            return render(request, 'register.html')


def detail(request, pk):
    record = Record.objects.get(pk=pk)

    context = {
        'record': record
    }
    if request.method == 'GET':
        return render(request, 'detail.html', context)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        record.first_name = first_name
        record.last_name = last_name
        record.email = email
        record.phone_num = phone
        record.address = address
        record.city = city
        record.country = country
        record.save()
        messages.success(request, 'Record Updated')
        return redirect('index')



def delete(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Record Was Deleted')
    return redirect('index')


class AddNewView(View):
    def get(self, request):
        return render(request, 'addnew.html')

    def post(self, request):
        if request.method == 'POST':

            if request.POST.get('first_name') or request.POST.get('last_name'):

                Record.objects.create(first_name=request.POST.get('first_name'),
                                    last_name=request.POST.get('last_name'),
                                    email=request.POST.get('email'),
                                    phone_num=request.POST.get('phone'),
                                    address=request.POST.get('address'),
                                    city=request.POST.get('city'),
                                    country=request.POST.get('country'),
                                    user=request.user)

                return redirect('index')
            else:
                messages.error(request, "Record Can't Be Empty")
                return render(request, 'addnew.html')





