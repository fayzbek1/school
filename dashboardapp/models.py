from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

CLASS_CHOICES =(
    #1
    ( 1.1 , "1A"),
    ( 1.2 , "1B"),
    ( "1D" , "1D"),
    ( "1F" , "1F"),
    
    #2
    ( "2A" , "2A"),
    ( "2B" , "2B"),
    ( "2D" , "2D"),
    ( "2F" , "2F"),
    
    #3
    ( "3A" , "3A"),
    ( "3B" , "3B"),
    ( "3D" , "3D"),
    ( "3F" , "3F"),
    
    #4
    ( "4A" , "4A"),
    ( "4B" , "4B"),
    ( "4D" , "4D"),
    ( "4F" , "4F"),
    
    #5
    ( "5A" , "5A"),
    ( "5B" , "5B"),
    ( "5D" , "5D"),
    ( "5F" , "5F"),
    
    #6
    ( "6A" , "6A"),
    ( "6B" , "6B"),
    ( "6D" , "6D"),
    ( "6F" , "6F"),
    
    #7
    ( "7A" , "7A"),
    ( "7B" , "7B"),
    ( "7D" , "7D"),
    ( "7F" , "7F"),
    
    #8
    ( "8A" , "8A"),
    ( "8B" , "8B"),
    ( "8D" , "8D"),
    ( "8F" , "8F"),

    #9
    ( "9A" , "9A"),
    ( "9B" , "9B"),
    ( "9D" , "9D"),
    ( "9F" , "9F"),
    
    #10
    ( "10A" , "10A"),
    ( "10B" , "10B"),
    ( "10D" , "10D"),
    
    #11
    ( "11A" , "11A"),
    ( "11B" , "11B"),
    ( "11D" , "11D"),
    ( "11F" , "11F"),
    
)    
SPTSALIST_CHOICES = (
    ( "math", "math"),
    ( "motherlangue", "motherlangue"),
    ( "physc", "physc"),
    ( "geografe", "geografe"),
    ( "music", "music"),
    ( "archihtura", "archihtura"),
    ( "work", "work"),
    ( "english", "english"),
    ( "russian", "russian"),
    ( "history", "history"),
    ( "literature", "literature"),
)  


class User_profile(models.Model):
    username = models.OneToOneField(User , on_delete=CASCADE)
    email = models.EmailField()
    fullname = models.CharField(max_length=70)
    about = models.TextField()
    adress = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    avatar = models.ImageField(upload_to='profile')
    


class Mentor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    salary = models.IntegerField()
    student = models.CharField(max_length=50)
    spesalis = models.CharField(max_length=50,choices=SPTSALIST_CHOICES, default= "math")

#students

class Student_1A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_1B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1B")    

class Student_1D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1d")    
    

class Student_1F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")      
#2
class Student_2A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_2B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_2D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_2F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")      
 #3   
class Student_3A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    

class Student_3B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_3D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_3F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")      


    #4
class Student_4A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_4B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_4D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_4F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")          
    #5
class Student_5A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_5B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_5D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_5F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")      
    #6
class Student_6A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
   
class Student_6B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_6D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_6F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")      
#7     
class Student_7A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_7B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_7D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_7F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")      


#8
class Student_8A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_8B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_8D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_8F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")  
#9
class Student_9A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_9B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_9D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

class Student_9F(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")      
#10
class Student_10A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_10B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_10D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    
    

     
#11 
class Student_11A(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")
    
class Student_11B(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    

class Student_11D(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    klass = models.CharField(max_length=30,choices=CLASS_CHOICES, default= "1A")    


class Admins(models.Model):
    full_name = models.CharField(max_length=30)
    t_number = models.IntegerField()
    email = models.EmailField()
    
class Ch_groups(models.Model):
    group = models.CharField(max_length=3,choices=CLASS_CHOICES, default= 1.1)


    