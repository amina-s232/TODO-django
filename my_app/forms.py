from django import forms 
from my_app.models import User,TaskModel

class Userregistrationform(forms.ModelForm):
    class Meta:
        model =User
        fields =['username','password','email']
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter name"}),
            "password":forms.PasswordInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter password"}),
            "email":forms.EmailInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter email"}),
        }
        help_texts={
            'username':None
        }
class Loginform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter name"}),error_messages={'required': ''})
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter password"}),error_messages={'required': ''})   
    

class Taskform(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['created_date','completed_status','user_id']
        widgets={
            "task_name":forms.TextInput(attrs={'class':'form-control w-75 mx-auto','placeholder':'Task name'}),
            "due_date":forms.DateInput(attrs={'class':'form-control w-75 mx-auto','placeholder':'Due date'}),
            "description":forms.TextInput(attrs={'class':'form-control w-75 mx-auto','placeholder':'Description'}),
            "task_catagory":forms.Select(attrs={'class':'form-control'}),

        }
    
class Forgotpasswordform(forms.Form):
    email = forms.EmailField( max_length=100,
    widget=forms.EmailInput(attrs={
        'class': 'form-control w-75 mx-auto',
        'placeholder': 'Enter Email'
    }))

class Otpforgotpasswordform(forms.Form):
    email=forms.CharField(max_length=100)

class Otpverifyform(forms.Form):
    otp=forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Enter otp','inputmode':'numeric'}))

class resetpasswordform(forms.Form):
    password= forms.CharField(max_length=50,
                              widget=forms.PasswordInput(attrs={'class':'form-control w-75 mx-auto','placeholder':'password'})
                              )
    confirm_password=forms.CharField(max_length=50,
                                widget=forms.PasswordInput(attrs={'class':'form-control w-75 mx-auto','placeholder':'confirm password'})
                                )