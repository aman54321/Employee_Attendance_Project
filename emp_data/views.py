from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages
from .models import Employee,Register, CustomUser
from .forms import employee_data_Form
from django.contrib.auth.decorators import login_required, permission_required
from .filters import DateFilter
from django.core.paginator import Paginator
import psycopg2
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def home(request):
    return render(request,'login.html')

@login_required(login_url='user_login')
def show(request):
    return render(request,'index.html')

@login_required(login_url='user_login')
@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show1')
def atten(request):
    context = {}
    if request.method=='GET':
        name = request.GET.get('name', '')
        date = request.GET.get('date', '')
        val_1={'name':name,'date':date}
        filtered_data = DateFilter(
            request.GET,
            queryset = Employee.objects.all()
        )
        
        context['filtered_data'] = filtered_data
        context['val_1']=val_1

        paginated_filtered_date = Paginator(filtered_data.qs,10)
        page_number = request.GET.get('page')
        data_obj = paginated_filtered_date.get_page(page_number)

        context['data_obj'] = data_obj

    return render(request, 'attendance.html', context=context)

def show1(request):
    return render(request, 'show1.html')

@login_required(login_url='user_login')
# @permission_required(emp_data.)
@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show1')
def show_all_data(request):
    context = {}
    if request.method=='GET':
        name = request.GET.get('name', '')
        date = request.GET.get('date', '')
        val_1={'name':name,'date':date}
        filtered_data = DateFilter(
            request.GET,
            queryset = Employee.objects.all()
        )
        
        context['filtered_data'] = filtered_data
        context['val_1']=val_1

        paginated_filtered_date = Paginator(filtered_data.qs,10)
        page_number = request.GET.get('page')
        data_obj = paginated_filtered_date.get_page(page_number)

        context['data_obj'] = data_obj

    return render(request, 'data.html', context=context)


def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # Is_staff = request.POST.get('Is staff')
        # Is_active = request.POST.get('Is active')

        # value = {"email":email,}
        # errorMsg=''
        # if (not name):
        #     errorMsg="Name is Required"
        # elif len(name)<=2:
        #     errorMsg="Name should be of minimum 3 letters"
        # elif name.isdigit():
        #     errorMsg="Name must contain letters only"
        # elif (not email):
        #     errorMsg="Email is required"
        # elif (not '@gmail' in email):
        #     errorMsg="It only accepts '@gmail' google format"
        # elif (not username):
        #     errorMsg="User Name is Required"
        # elif username.isalnum():
        #     errorMsg="User Name must contain a number, character and special character(!@#$_-&)"
        # elif len(username)<=2:
        #     errorMsg="User name should be of minimum 3 letters"
        # elif len(password1)<4:
        #     errorMsg="Length of password must be more than 4"
        # elif password1 != password2:
        #     errorMsg="password do not match"
        # if not errorMsg:
        myuser = CustomUser.objects.create_user(email, password1, is_staff = False, is_active = True)
        myuser.save()
        return redirect('user_login')
    # else:
    #     val={
    #         # 'error':errorMsg,
    #         'values':value
    #     }
        # return render(request,'register.html',val)
    return render(request,'register.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        user = authenticate(email=email, password=password)
        val={'email':email}
        error_Msg=''
        if (not email):
            error_Msg="Email is Required"
        elif (not password):
            error_Msg="Password is Required"
        elif user is None:
            error_Msg="Incorrect email/Password"
        if user is not None:
            login(request,user) 
            messages.success(request, "Successfully Logged In")
            return redirect('show')
        else:
            data={
                'error_message': error_Msg,
                'vals':val
                }
            return render(request, 'login.html', data)
    return render(request, 'login.html')

@login_required(login_url='user_login')
def edit(request,pk):
    employee = Employee.objects.get(pk=pk)
    form = employee_data_Form(instance=employee)

    if request.method == 'POST':
        form = employee_data_Form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('show_all_data')

    context = {'form':form}
    return render(request,'edit.html',context)

@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show1')
def create(request):
    form = employee_data_Form()
    if request.method == 'POST':
        form = employee_data_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_all_data')
    context = {'form': form}
    return render(request,'create.html',context)

@login_required(login_url='user_login')
def delete(request,pk):
    emp=Employee.objects.get(pk=pk)
    if request.method == "POST":
        emp.delete()
        return redirect('show_all_data')
    context = {'emp': emp}
    return render(request,'delete.html',context)

@login_required(login_url='user_login')
def logout(request):
    auth_logout(request)
    return redirect('user_login')


# def register(request):
#     if request.method =='POST':
#         postdata=request.POST
#         name = postdata.get('name')
#         username = postdata.get('username')
#         email = postdata.get('email')
#         e_id = postdata.get('e_id')
#         designation = postdata.get('designation')
#         password1 = postdata.get('password1')
#         password2 = postdata.get('password2')
#         value = {"name":name,"email":email,"username":username,'e_id':e_id,'designation':designation}
#         errorMsg=''
#         if (not name):
#             errorMsg="Name is Required"
#         elif len(name)<=2:
#             errorMsg="Name should be of minimum 3 letters"
#         elif name.isdigit():
#             errorMsg="Name must contain letters only"
#         elif (not email):
#             errorMsg="Email is required"
#         elif (not '@gmail' in email):
#             errorMsg="It only accepts '@gmail' google format"
#         elif (not username):
#             errorMsg="User Name is Required"
#         elif username.isalnum():
#             errorMsg="User Name must contain a number, character and special character(!@#$_-&)"
#         elif len(username)<=2:
#             errorMsg="User name should be of minimum 3 letters"
#         elif len(password1)<4:
#             errorMsg="Length of password must be more than 4"
#         elif password1 != password2:
#             errorMsg="password do not match"
#         if not errorMsg:
#             form = Register(name=name,username=username, email=email, e_id=e_id, designation=designation, password1=password1, password2=password2)
#             form.save()
#             return redirect('signin')
#         else:
#             val={
#                 'error':errorMsg,
#                 'values':value
#             }
#             return render(request,'signup.html',val)
#     return render(request,'signup.html')


def signin(request):
    if request.method == "POST":
        e_mail = request.POST.get('e_mail')
        pwd = request.POST.get('pwd')
        uname= request.POST.get('uname')
        x = Register.objects.all().filter(email=e_mail,username=uname,password1=pwd)
        for i in x:
            if i.email == e_mail and i.username == uname and i.password1 == pwd:
                return render(request, 'index.html')
    return render(request, 'signin.html')

@login_required(login_url='user_login')
# @user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists())
def user_data(request):
    data = Register.objects.all()
    return render(request,'list.html',{'data':data})





