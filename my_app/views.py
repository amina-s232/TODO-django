from django.shortcuts import render,redirect
from django.views.generic import View
from my_app.forms import Userregistrationform,Loginform,Taskform,Forgotpasswordform,Otpverifyform,resetpasswordform
from my_app.models import User,TaskModel,Otpmodel
from django.contrib.auth import authenticate,login,logout
import random
from django.core.mail import send_mail
from django.utils.decorators import method_decorator

# Create your views here.

#register , login , add task,read rask, delete task,update task,logout,forgot passoword,

def is_user(fn):
    def wrapper(request,**kwargs):
        id = kwargs.get("pk")
        item=TaskModel.objects.get(id=id)
        if item.user_id == request.user:
            return fn(request,**kwargs)
        return redirect("login")
    return wrapper




class Userreigistarationview(View):
    def get(self,request):
        form = Userregistrationform
        return render(request,'signup.html',{'form':form})
    
    def post(self,request):
        form =Userregistrationform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            User.objects.create_user(username=username,password=password,email=email)
        form=Userregistrationform
        # return render(request,'signup.html',{'form':form})
        return redirect('login')
#login

class Loginview(View):
    def get(self,request):
        form=Loginform
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form=Loginform(request.POST)
        if form.is_valid():

            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user_obj=authenticate(request,username=username,password=password)
            if user_obj:
                login(request,user_obj)

                print(request.user)
        
            return redirect("tasklist")
        else:
            form=Loginform()

        return render(request,'login.html',{'form':form})

class Logoutview(View):
    def get(self,request):
        logout(request)
        return redirect('login')
    

class Addtaskview(View):
    def get(self,request):
        form = Taskform
        return render(request,'addtask.html',{'form':form})
    def post(self,request):
        form=Taskform(request.POST)
        if form.is_valid():
            TaskModel.objects.create(user_id=request.user,**form.cleaned_data)
        return render(request,'addtask.html',{'form':form})
    
# @method_decorator(decorator=is_user,name="dispatch")
class Taskreadview(View):
    def get(self,request):

        # items= TaskModel.objects.all()
        items=TaskModel.objects.filter(user_id=request.user)
        return render(request,'tasklist.html',{'items':items})    

@method_decorator(decorator=is_user,name="dispatch")
class Taskupdate(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        item= TaskModel.objects.get(id=id)
        form=Taskform(instance=item)
        return render(request,'update.html',{'form':form})
    def post(self,request,**kwargs):

        id=kwargs.get('pk')

        item =TaskModel.objects.get(id=id)
        form = Taskform(request.POST,instance=item)
        if form.is_valid:
            form.save()

        form =Taskform
        return render(request,'update.html',{'form':form})
    
@method_decorator(decorator=is_user,name='dispatch')    
class Taskdelete(View):
    def get(self,request,**kwargs):
        id =kwargs.get('pk')
        TaskModel.objects.get(id=id).delete()
        return redirect('tasklist')
    
class Taskdetails(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        item=TaskModel.objects.get(id=id)
        return render(request,'detail.html',{'item':item})    


class Taskedit(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        data=TaskModel.objects.get(id=id)
        data.completed_status=True
        data.save()
        return redirect('tasklist')
    

class Forgotpassword(View):
        def get(self,request):
            form=Forgotpasswordform
            return render(request,'forgotpwd.html',{"form":form})
        def post(self,request):

            form=Forgotpasswordform(request.POST)

            if form.is_valid():
                 
                 email=form.cleaned_data.get('email')
                 user=User.objects.get(email=email)
                 otp =random.randint(1000,9999)
                 Otpmodel.objects.create(user_id=user,otp=otp)  
                 send_mail(subject="otp for password reset",message=str(otp),from_email="iamamin936@gmail.com",recipient_list=[email])
                 return redirect('otpverify')
            return render(request,'forgotpwd.html',{"form":form})
                #  afwe nque ezvq fyzd

class Otpverifyview(View):
    def get(self,request):
        form=Otpverifyform
        return render(request,'otpverify.html',{'form':form})
    def post(self,request):
        form=Otpverifyform(request.POST)
        if form.is_valid():
            otp=form.cleaned_data.get('otp')
            item=Otpmodel.objects.get(otp=otp)
            user_id=item.user_id
            user=User.objects.get(id=user_id.id)
            username=user.username
            if item:
                request.session['user']=username
                return redirect("reset")
            return render(request,'otpverify.html',{'form':form})
        
class Resetpassword(View):
    def get(self,request):
        form=resetpasswordform
        return render(request,'resetpwd.html',{'form':form}) 
    def post(self,request):
        form=resetpasswordform(request.POST)

        if form.is_valid(): 
            password=form.cleaned_data.get('password')
            confirm_password=form.cleaned_data.get('confirm_password')
            if password == confirm_password:
                username=request.session.get('user')
                user=User.objects.get(username=username)
                user.set_password(password)
                user.save()
                return redirect('login')
            
        return render(request,'resetpwd.html',{'form':form})
    
class Taskfilterview(View):
    def get(self,request):
        category= request.GET.get('category')
        Task=TaskModel.objects.filter(user_id=request.user)
        tasks= Task.filter(task_catagory=category)
        print(tasks)
        return render(request,'filter.html',{'tasks':tasks})
    

class Index(View):
    def get(self,request):
        return render(request,'indexx.html')