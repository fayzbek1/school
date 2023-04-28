from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]

class Ch_groups(forms.ModelForm):
    class Meta:
        model = Ch_groups
        fields = ['group']


        
        
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ['username','email','fullname','about','country','city','adress',]  
       
          
class Create1AForm(forms.ModelForm):
    class Meta:
        model = Student_1A
        fields = ['first_name','last_name','birth_date','country','city','adress',]      

class Create1BForm(forms.ModelForm):
    class Meta:
        model = Student_1B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create1DForm(forms.ModelForm):
    class Meta:
        model = Student_1D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create1FForm(forms.ModelForm):
    class Meta:
        model = Student_1F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        
#2
class Create2AForm(forms.ModelForm):
    class Meta:
        model = Student_2A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create2BForm(forms.ModelForm):
    class Meta:
        model = Student_2B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create2DForm(forms.ModelForm):
    class Meta:
        model = Student_2D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create2FForm(forms.ModelForm):
    class Meta:
        model = Student_2F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]                    
        
#3
class Create3AForm(forms.ModelForm):
    class Meta:
        model = Student_3A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create3BForm(forms.ModelForm):
    class Meta:
        model = Student_3B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create3DForm(forms.ModelForm):
    class Meta:
        model = Student_3D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create3FForm(forms.ModelForm):
    class Meta:
        model = Student_3F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]                    
        
#4
class Create4AForm(forms.ModelForm):
    class Meta:
        model = Student_4A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create4BForm(forms.ModelForm):
    class Meta:
        model = Student_4B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create4DForm(forms.ModelForm):
    class Meta:
        model = Student_4D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create4FForm(forms.ModelForm):
    class Meta:
        model = Student_4F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        
#5
class Create5AForm(forms.ModelForm):
    class Meta:
        model = Student_5A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create5BForm(forms.ModelForm):
    class Meta:
        model = Student_5B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create5DForm(forms.ModelForm):
    class Meta:
        model = Student_5D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create5FForm(forms.ModelForm):
    class Meta:
        model = Student_5F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]                    
        
#6
class Create6AForm(forms.ModelForm):
    class Meta:
        model = Student_6A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create6BForm(forms.ModelForm):
    class Meta:
        model = Student_6B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create6DForm(forms.ModelForm):
    class Meta:
        model = Student_6D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create6FForm(forms.ModelForm):
    class Meta:
        model = Student_6F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]                    
        
#7
class Create7AForm(forms.ModelForm):
    class Meta:
        model = Student_7A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create7BForm(forms.ModelForm):
    class Meta:
        model = Student_7B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create7DForm(forms.ModelForm):
    class Meta:
        model = Student_7D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create7FForm(forms.ModelForm):
    class Meta:
        model = Student_7F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]                    
        
#8
class Create8AForm(forms.ModelForm):
    class Meta:
        model = Student_8A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create8BForm(forms.ModelForm):
    class Meta:
        model = Student_8B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create8DForm(forms.ModelForm):
    class Meta:
        model = Student_8D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create8FForm(forms.ModelForm):
    class Meta:
        model = Student_8F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            

#9       
class Create9AForm(forms.ModelForm):
    class Meta:
        model = Student_9A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create9BForm(forms.ModelForm):
    class Meta:
        model = Student_9B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create9DForm(forms.ModelForm):
    class Meta:
        model = Student_9D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

class Create9FForm(forms.ModelForm):
    class Meta:
        model = Student_9F
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]                    

#10
class Create10AForm(forms.ModelForm):
    class Meta:
        model = Student_10A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create10BForm(forms.ModelForm):
    class Meta:
        model = Student_10B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create10DForm(forms.ModelForm):
    class Meta:
        model = Student_10D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

#11
class Create11AForm(forms.ModelForm):
    class Meta:
        model = Student_11A
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create11BForm(forms.ModelForm):
    class Meta:
        model = Student_11B
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]
        

class Create11DForm(forms.ModelForm):
    class Meta:
        model = Student_11D
        fields = ['first_name','last_name','birth_date','country','city','adress','klass',]            
        

