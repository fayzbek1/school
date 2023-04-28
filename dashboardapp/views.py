from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

def test(request):
    return render(request,'mainapp/test.html')

def tablestudent(request):
    return render(request,'mainapp/students.html')

def mainpage(request):
    return render(request,'mainapp/index.html')

def registeruser(request):
    form = CreateUserForm
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user')
            return redirect('login')
        
    context = {
        'form':form,
        
    }    
    return render(request,'mainapp/register.html',context)  





def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password1')

        user = authenticate(request,  username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Username or password was incorrect")

    context = {

    }        

    return render(request,'mainapp/login.html')   

def logoutuser(request):
    logout(request)
    return redirect('login') 

def user_profile(request):
    profiles = User_profile.objects.all()

    context = {
        'profiles':profiles,
        'username':request.user,
    }
    return render(request,'mainapp/user_profile.html',context)  

def createprofile(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            CreateProfileForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/createprofile.html',context)

def updateprofile(request,pk):
    profile = User_profile.objects.get(id=pk)
    form = CreateProfileForm(instance=profile)
    if request.method == "POST":
        form = CreateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()

    context = {
        'form':form,
    }
    return render(request,'mainapp/update_profile.html',context)

def mentortable(request):
    return render(request,'mainapp/mentor_table.html')

def base (request):
    profiles = User_profile.objects.all()
    context = {
        'username':request.user,
        'profiles':profiles
    }
    return render(request,'mainapp/base.html',context)  

#class
#class 1
def student_1A_table(request):
    student1a = Student_1A.objects.all()
    context = {
        'student1a':student1a
    }
    return render(request,'mainapp/students/student_1A.html',context)
def student_1B_table(request):
    student1b = Student_1B.objects.all()
    context = {
        'student1b':student1b
    }
    return render(request,'mainapp/students/student_1B.html',context)
def student_1D_table(request):
    student1d = Student_1D.objects.all()
    context = {
        'student1d':student1d
    }
    return render(request,'mainapp/students/student_1D.html',context)
def student_1F_table(request):
    student1f = Student_1F.objects.all()
    context = {
        'student1f':student1f
    }
    return render(request,'mainapp/students/student_1F.html',context)    

#class 2
def student_2A_table(request):
    student2a = Student_2A.objects.all()
    context = {
        'student2a':student2a
    }
    return render(request,'mainapp/students/student_2A.html',context)
def student_2B_table(request):
    student2b = Student_2B.objects.all()
    context = {
        'student2b':student2b
    }
    return render(request,'mainapp/students/student_2B.html',context)
def student_2D_table(request):
    student2d = Student_2D.objects.all()
    context = {
        'student2d':student2d
    }
    return render(request,'mainapp/students/student_2D.html',context)
def student_2F_table(request):
    student2f = Student_2F.objects.all()
    context = {
        'student2f':student2f
    }
    return render(request,'mainapp/students/student_2F.html',context)    

#class 3
def student_3A_table(request):
    student3a = Student_3A.objects.all()
    context = {
        'student3a':student3a
    }
    return render(request,'mainapp/students/student_3A.html',context)
def student_3B_table(request):
    student3b = Student_3B.objects.all()
    context = {
        'student3b':student3b
    }
    return render(request,'mainapp/students/student_3B.html',context)
def student_3D_table(request):
    student3d = Student_3D.objects.all()
    context = {
        'student3d':student3d
    }
    return render(request,'mainapp/students/student_3D.html',context)
def student_3F_table(request):
    student3f = Student_3F.objects.all()
    context = {
        'student3f':student3f
    }
    return render(request,'mainapp/students/student_3F.html',context)    

#class 4
def student_4A_table(request):
    student4a = Student_4A.objects.all()
    context = {
        'student4a':student4a
    }
    return render(request,'mainapp/students/student_4A.html',context)
def student_4B_table(request):
    student4b = Student_4B.objects.all()
    context = {
        'student4b':student4b
    }
    return render(request,'mainapp/students/student_4B.html',context)
def student_4D_table(request):
    student4d = Student_4D.objects.all()
    context = {
        'student4d':student4d
    }
    return render(request,'mainapp/students/student_4D.html',context)
def student_4F_table(request):
    student4f = Student_4F.objects.all()
    context = {
        'student4f':student4f
    }
    return render(request,'mainapp/students/student_4F.html',context)  

#class 5
def student_5A_table(request):
    student5a = Student_5A().objects.all()
    context = {
        'student5a':student5a
    }
    return render(request,'mainapp/students/student_5A.html',context)
def student_5B_table(request):
    student5b = Student_5B.objects.all()
    context = {
        'student5b':student5b
    }
    return render(request,'mainapp/students/student_5B.html',context)
def student_5D_table(request):
    student5d = Student_5D.objects.all()
    context = {
        'student5d':student5d
    }
    return render(request,'mainapp/students/student_5D.html',context)
def student_5F_table(request):
    student5f = Student_5F.objects.all()
    context = {
        'student5f':student5f
    }
    return render(request,'mainapp/students/student_5F.html',context)  

#class 6
def student_6A_table(request):
    student6a = Student_6A.objects.all()
    context = {
        'student6a':student6a
    }
    return render(request,'mainapp/students/student_6A.html',context)
def student_6B_table(request):
    student6b = Student_6B.objects.all()
    context = {
        'student6b':student6b
    }
    return render(request,'mainapp/students/student_6B.html',context)
def student_6D_table(request):
    student6d = Student_6D.objects.all()
    context = {
        'student6D':student6d
    }
    return render(request,'mainapp/students/student_6D.html',context)
def student_6F_table(request):
    student6f = Student_6F.objects.all()
    context = {
        'student6f':student6f
    }
    return render(request,'mainapp/students/student_6F.html',context) 

#class 7
def student_7A_table(request):
    student7a = Student_7A.objects.all()
    context = {
        'student7a':student7a
    }
    return render(request,'mainapp/students/student_7A.html',context)
def student_7B_table(request):
    student7b = Student_7B.objects.all()
    context = {
        'student7b':student7b
    }
    return render(request,'mainapp/students/student_7B.html',context)
def student_7D_table(request):
    student7d = Student_7D.objects.all()
    context = {
        'student7d':student7d
    }
    return render(request,'mainapp/students/student_7D.html',context)
def student_7F_table(request):
    student7f = Student_7F.objects.all()
    context = {
        'student7f':student7f
    }
    return render(request,'mainapp/students/student_7F.html',context) 

#class 8
def student_8A_table(request):
    student8a = Student_8A.objects.all()
    context = {
        'student8a':student8a
    }
    return render(request,'mainapp/students/student_8A.html',context)
def student_8B_table(request):
    student8b = Student_8B.objects.all()
    context = {
        'student8b':student8b
    }
    return render(request,'mainapp/students/student_8B.html',context)
def student_8D_table(request):
    student8d = Student_8D.objects.all()
    context = {
        'student8d':student8d
    }
    return render(request,'mainapp/students/student_8D.html',context)
def student_8F_table(request):
    student8f = Student_8F.objects.all()
    context = {
        'student8f':student8f
    }
    return render(request,'mainapp/students/student_7F.html',context) 

#class 9
def student_9A_table(request):
    student9a = Student_9A.objects.all()
    context = {
        'student9a':student9a
    }
    return render(request,'mainapp/students/student_9A.html',context)
def student_9B_table(request):
    student9b = Student_9B.objects.all()
    context = {
        'student9b':student9b
    }
    return render(request,'mainapp/students/student_9B.html',context)
def student_9D_table(request):
    student9d = Student_9D.objects.all()
    context = {
        'student9D':student9d
    }
    return render(request,'mainapp/students/student_9D.html',context)
def student_9F_table(request):
    student9f = Student_9F.objects.all()
    context = {
        'student9f':student9f
    }
    return render(request,'mainapp/students/student_9F.html',context) 

#class 10
def student_10A_table(request):
    student10a = Student_10A.objects.all()
    context = {
        'student10a':student10a
    }
    return render(request,'mainapp/students/student_10A.html',context)
def student_10B_table(request):
    student10b = Student_10B.objects.all()
    context = {
        'student10b':student10b
    }
    return render(request,'mainapp/students/student_10B.html',context)
def student_10D_table(request):
    student10d = Student_10D.objects.all()
    context = {
        'student10d':student10d
    }
    return render(request,'mainapp/students/student_10D.html',context)

#class 11
def student_11A_table(request):
    student11a = Student_11A.objects.all()
    context = {
        'student11a':student11a
    }
    return render(request,'mainapp/students/student_11A.html',context)
def student_11B_table(request):
    student11b = Student_11B.objects.all()
    context = {
        'student11B':student11b
    }
    return render(request,'mainapp/students/student_11B.html',context)
def student_11D_table(request):
    student11d = Student_11D.objects.all()
    context = {
        'student11d':student11d
    }
    return render(request,'mainapp/students/student_11D.html',context)

#create students
def createe1a(request):
    form = Create1AForm()
    if request.method == 'POST':
        form = Create1AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-1A-t')
        else:
            Create1AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create1a.html',context)

def createe1b(request):
    form = Create1BForm()
    if request.method == 'POST':
        form = Create1BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-1B-t')
        else:
            Create1BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create1b.html',context)

def createe1d(request):
    form = Create1DForm()
    if request.method == 'POST':
        form = Create1DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-1D-t')
        else:
            Create1DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create1d.html',context)

def createe1f(request):
    form = Create1FForm()
    if request.method == 'POST':
        form = Create1FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-1F-t')
        else:
            Create1FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create1f.html',context)

def createe2a(request):
    form = Create2AForm()
    if request.method == 'POST':
        form = Create2AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-2A-t')
        else:
            Create2AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create2a.html',context)

def createe2b(request):
    form = Create2BForm()
    if request.method == 'POST':
        form = Create2BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-2B-t')
        else:
            Create2BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create2b.html',context)

def createe2d(request):
    form = Create2DForm()
    if request.method == 'POST':
        form = Create2DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-2D-t')
        else:
            Create2DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create2d.html',context)

def createe2f(request):
    form = Create2FForm()
    if request.method == 'POST':
        form = Create2FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-2F-t')
        else:
            Create2FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create2f.html',context)

def createe3a(request):
    form = Create3AForm()
    if request.method == 'POST':
        form = Create3AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-3a-t')
        else:
            Create3AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create3a.html',context)

def createe3b(request):
    form = Create3BForm()
    if request.method == 'POST':
        form = Create3BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-3B-t')
        else:
            Create3BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create3b.html',context)

def createe3d(request):
    form = Create3DForm()
    if request.method == 'POST':
        form = Create3DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-3D-t')
        else:
            Create3DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create3d.html',context)

def createe3f(request):
    form = Create3FForm()
    if request.method == 'POST':
        form = Create3FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-3F-t')
        else:
            Create3FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create3f.html',context)

def createe4a(request):
    form = Create4AForm()
    if request.method == 'POST':
        form = Create4FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-4A-t')
        else:
            Create4AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create4a.html',context)

def createe4b(request):
    form = Create4BForm()
    if request.method == 'POST':
        form = Create4BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-4B-t')
        else:
            Create4BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create4b.html',context)

def createe4d(request):
    form = Create4DForm()
    if request.method == 'POST':
        form = Create4DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-4D-t')
        else:
            Create4DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create4b.html',context)

def createe4f(request):
    form = Create4FForm()
    if request.method == 'POST':
        form = Create4FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-4F-t')
        else:
            Create4FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create4f.html',context)

def createe5a(request):
    form = Create5AForm()
    if request.method == 'POST':
        form = Create5AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-5A-t')
        else:
            Create5AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create5a.html',context)

def createe5b(request):
    form = Create5BForm()
    if request.method == 'POST':
        form = Create5BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-5B-t')
        else:
            Create5BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create5b.html',context)

def createe5d(request):
    form = Create5DForm()
    if request.method == 'POST':
        form = Create5DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-5D-t')
        else:
            Create5DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create5d.html',context)

def createe5f(request):
    form = Create5FForm()
    if request.method == 'POST':
        form = Create5FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-5F-t')
        else:
            Create5FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create5f.html',context)

def createe6a(request):
    form = Create6AForm()
    if request.method == 'POST':
        form = Create6AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-6A-t')
        else:
            Create6AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create6a.html',context)

def createe6b(request):
    form = Create6BForm()
    if request.method == 'POST':
        form = Create6BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-6B-t')
        else:
            Create6BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create6b.html',context)

def createe6d(request):
    form = Create6DForm()
    if request.method == 'POST':
        form = Create6DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-6D-t')
        else:
            Create6DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create6d.html',context)

def createe6f(request):
    form = Create6FForm()
    if request.method == 'POST':
        form = Create6FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-6F-t')
        else:
            Create6FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create6f.html',context)

def createe7a(request):
    form = Create7AForm()
    if request.method == 'POST':
        form = Create7AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-7A-t')
        else:
            Create7AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create7a.html',context)

def createe7b(request):
    form = Create7BForm()
    if request.method == 'POST':
        form = Create7BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-7B-t')
        else:
            Create7BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create7b.html',context)

def createe7d(request):
    form = Create7DForm()
    if request.method == 'POST':
        form = Create7DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-7D-t')
        else:
            Create7DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create7d.html',context)

def createe7f(request):
    form = Create7FForm()
    if request.method == 'POST':
        form = Create7FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-7F-t')
        else:
            Create7FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create7f.html',context)

def createe8a(request):
    form = Create8AForm()
    if request.method == 'POST':
        form = Create8AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-8A-t')
        else:
            Create8AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create8a.html',context)

def createe8b(request):
    form = Create8BForm()
    if request.method == 'POST':
        form = Create8BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-8B-t')
        else:
            Create8BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create8b.html',context)

def createe8d(request):
    form = Create8DForm()
    if request.method == 'POST':
        form = Create8DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-8D-t')
        else:
            Create8DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create8d.html',context)

def createe8f(request):
    form = Create8FForm()
    if request.method == 'POST':
        form = Create8FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-8F-t')
        else:
            Create8FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create8f.html',context)

def createe9a(request):
    form = Create9AForm()
    if request.method == 'POST':
        form = Create9AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-9A-t')
        else:
            Create9AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create9a.html',context)

def createe9b(request):
    form = Create9BForm()
    if request.method == 'POST':
        form = Create9BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-9B-t')
        else:
            Create9BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create9b.html',context)

def createe9d(request):
    form = Create9DForm()
    if request.method == 'POST':
        form = Create9DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-9D-t')
        else:
            Create9DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create9d.html',context)

def createe9f(request):
    form = Create9FForm()
    if request.method == 'POST':
        form = Create9FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-9F-t')
        else:
            Create9FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create9f.html',context)

def createe10a(request):
    form = Create10AForm()
    if request.method == 'POST':
        form = Create10AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-10A-t')
        else:
            Create10AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create10a.html',context)

def createe10b(request):
    form = Create10BForm()
    if request.method == 'POST':
        form = Create10BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-10B-t')
        else:
            Create10BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create10b.html',context)

def createe10d(request):
    form = Create10DForm()
    if request.method == 'POST':
        form = Create10DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-10D-t')
        else:
            Create10DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create10d.html',context)

def createe11a(request):
    form = Create11AForm()
    if request.method == 'POST':
        form = Create11AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-11A-t')
        else:
            Create11AForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create11a.html',context)

def createe11b(request):
    form = Create11BForm()
    if request.method == 'POST':
        form = Create11BForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-11B-t')
        else:
            Create11BForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create11b.html',context)

def createe11d(request):
    form = Create11DForm()
    if request.method == 'POST':
        form = Create11DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-11D-t')
        else:
            Create11DForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create11d.html',context)


    form = Create8FForm()
    if request.method == 'POST':
        form = Create8FForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-8F-t')
        else:
            Create8FForm()

    context = {
        'form': form,

    }
    return render(request,'mainapp/create/create8f.html',context)

#delete
def delete1a(request,pk):
    delete1a = Student_1A.objects.get(id=pk)
    if request.method == "POST":
        delete1a.delete()
        return redirect('student-1A-t')
    context = {
        'delete1a':delete1a
    }
    return render(request,'mainapp/delete/delete1a.html',context)

def delete1b(request,pk):
    delete1b = Student_1B.objects.get(id=pk)
    if request.method == "POST":
        delete1b.delete()
        return redirect('student-1B-t')
    context = {
        'delete1b':delete1b
    }
    return render(request,'mainapp/delete/delete1b.html',context)

def delete1d(request,pk):
    delete1d = Student_1D.objects.get(id=pk)
    if request.method == "POST":
        delete1d.delete()
        return redirect('student-1D-t')
    context = {
        'delete1d':delete1d
    }
    return render(request,'mainapp/delete/delete1d.html',context)

def delete1f(request,pk):
    delete1f = Student_1F.objects.get(id=pk)
    if request.method == "POST":
        delete1f.delete()
        return redirect('student-1F-t')
    context = {
        'delete1f':delete1f
    }
    return render(request,'mainapp/delete/delete1f.html',context)

def delete2a(request,pk):
    delete2a = Student_2A.objects.get(id=pk)
    if request.method == "POST":
        delete2a.delete()
        return redirect('student-2A-t')
    context = {
        'delete2a':delete2a
    }
    return render(request,'mainapp/delete/delete2a.html',context)

def delete2b(request,pk):
    delete2b = Student_2B.objects.get(id=pk)
    if request.method == "POST":
        delete2b.delete()
        return redirect('student-1B-t')
    context = {
        'delete2b':delete2b
    }
    return render(request,'mainapp/delete/delete2b.html',context)

def delete2d(request,pk):
    delete2d = Student_2D.objects.get(id=pk)
    if request.method == "POST":
        delete2d.delete()
        return redirect('student-1D-t')
    context = {
        'delete2d':delete2d
    }
    return render(request,'mainapp/delete/delete2d.html',context)

def delete2f(request,pk):
    delete2f = Student_2F.objects.get(id=pk)
    if request.method == "POST":
        delete2f.delete()
        return redirect('student-2F-t')
    context = {
        'delete2f':delete2f
    }
    return render(request,'mainapp/delete/delete2f.html',context)

def delete3a(request,pk):
    delete3a = Student_3A.objects.get(id=pk)
    if request.method == "POST":
        delete3a.delete()
        return redirect('student-3A-t')
    context = {
        'delete3a':delete3a
    }
    return render(request,'mainapp/delete/delete3a.html',context)

def delete3b(request,pk):
    delete3b = Student_3B.objects.get(id=pk)
    if request.method == "POST":
        delete3b.delete()
        return redirect('student-3B-t')
    context = {
        'delete3b':delete3b
    }
    return render(request,'mainapp/delete/delete3b.html',context)

def delete3d(request,pk):
    delete3d = Student_3D.objects.get(id=pk)
    if request.method == "POST":
        delete3d.delete()
        return redirect('student-3D-t')
    context = {
        'delete3d':delete3d
    }
    return render(request,'mainapp/delete/delete3d.html',context)

def delete3f(request,pk):
    delete3f = Student_3F.objects.get(id=pk)
    if request.method == "POST":
        delete3f.delete()
        return redirect('student-3F-t')
    context = {
        'delete3f':delete3f
    }
    return render(request,'mainapp/delete/delete3f.html',context)

def delete4a(request,pk):
    delete4a = Student_4A.objects.get(id=pk)
    if request.method == "POST":
        delete4a.delete()
        return redirect('student-4A-t')
    context = {
        'delete4a':delete4a
    }
    return render(request,'mainapp/delete/delete4a.html',context)

def delete4b(request,pk):
    delete4b = Student_4B.objects.get(id=pk)
    if request.method == "POST":
        delete4b.delete()
        return redirect('student-4B-t')
    context = {
        'delete4b':delete4b
    }
    return render(request,'mainapp/delete/delete4b.html',context)

def delete4d(request,pk):
    delete4d = Student_4D.objects.get(id=pk)
    if request.method == "POST":
        delete4d.delete()
        return redirect('student-4D-t')
    context = {
        'delete4d':delete4d
    }
    return render(request,'mainapp/delete/delete4d.html',context)

def delete4f(request,pk):
    delete4f = Student_4F.objects.get(id=pk)
    if request.method == "POST":
        delete4f.delete()
        return redirect('student-4F-t')
    context = {
        'delete4f':delete4f
    }
    return render(request,'mainapp/delete/delete4f.html',context)
 
def delete5a(request,pk):
    delete5a = Student_5A.objects.get(id=pk)
    if request.method == "POST":
        delete5a.delete()
        return redirect('student-5A-t')
    context = {
        'delete5a':delete5a
    }
    return render(request,'mainapp/delete/delete5a.html',context)

def delete5b(request,pk):
    delete5b = Student_5B.objects.get(id=pk)
    if request.method == "POST":
        delete5b.delete()
        return redirect('student-5B-t')
    context = {
        'delete5b':delete5b
    }
    return render(request,'mainapp/delete/delete5b.html',context)

def delete5d(request,pk):
    delete5d = Student_5D.objects.get(id=pk)
    if request.method == "POST":
        delete5d.delete()
        return redirect('student-5D-t')
    context = {
        'delete5d':delete5d
    }
    return render(request,'mainapp/delete/delete5d.html',context)

def delete5f(request,pk):
    delete5f = Student_1F.objects.get(id=pk)
    if request.method == "POST":
        delete5f.delete()
        return redirect('student-5F-t')
    context = {
        'delete5f':delete5f
    }
    return render(request,'mainapp/delete/delete5f.html',context)

def delete6a(request,pk):
    delete6a = Student_6A.objects.get(id=pk)
    if request.method == "POST":
        delete6a.delete()
        return redirect('student-6A-t')
    context = {
        'delete6a':delete6a
    }
    return render(request,'mainapp/delete/delete6a.html',context)

def delete6b(request,pk):
    delete6b = Student_6B.objects.get(id=pk)
    if request.method == "POST":
        delete6b.delete()
        return redirect('student-6B-t')
    context = {
        'delete6b':delete6b
    }
    return render(request,'mainapp/delete/delete6b.html',context)

def delete6d(request,pk):
    delete6d = Student_6D.objects.get(id=pk)
    if request.method == "POST":
        delete6d.delete()
        return redirect('student-6D-t')
    context = {
        'delete6d':delete6d
    }
    return render(request,'mainapp/delete/delete6d.html',context)

def delete6f(request,pk):
    delete6f = Student_6F.objects.get(id=pk)
    if request.method == "POST":
        delete6f.delete()
        return redirect('student-6F-t')
    context = {
        'delete6f':delete6f
    }
    return render(request,'mainapp/delete/delete6f.html',context)

def delet7a(request,pk):
    delete7a = Student_7A.objects.get(id=pk)
    if request.method == "POST":
        delete7a.delete()
        return redirect('student-7A-t')
    context = {
        'delete7a':delete7a
    }
    return render(request,'mainapp/delete/delete7a.html',context)

def delete7b(request,pk):
    delete7b = Student_7B.objects.get(id=pk)
    if request.method == "POST":
        delete7b.delete()
        return redirect('student-7B-t')
    context = {
        'delete7b':delete7b
    }
    return render(request,'mainapp/delete/delete7b.html',context)

def delete7d(request,pk):
    delete7d = Student_7D.objects.get(id=pk)
    if request.method == "POST":
        delete7d.delete()
        return redirect('student-7D-t')
    context = {
        'delete7d':delete7d
    }
    return render(request,'mainapp/delete/delete7d.html',context)

def delete7f(request,pk):
    delete7f = Student_7F.objects.get(id=pk)
    if request.method == "POST":
        delete7f.delete()
        return redirect('student-7F-t')
    context = {
        'delete7f':delete7f
    }
    return render(request,'mainapp/delete/delete7f.html',context)

def delete8a(request,pk):
    delete8a = Student_8A.objects.get(id=pk)
    if request.method == "POST":
        delete8a.delete()
        return redirect('student-8A-t')
    context = {
        'delete8a':delete8a
    }
    return render(request,'mainapp/delete/delete8a.html',context)

def delete8b(request,pk):
    delete8b = Student_8B.objects.get(id=pk)
    if request.method == "POST":
        delete8b.delete()
        return redirect('student-8B-t')
    context = {
        'delete8b':delete8b
    }
    return render(request,'mainapp/delete/delete8b.html',context)

def delete8d(request,pk):
    delete8d = Student_8D.objects.get(id=pk)
    if request.method == "POST":
        delete8d.delete()
        return redirect('student-8D-t')
    context = {
        'delete8d':delete8d
    }
    return render(request,'mainapp/delete/delete8d.html',context)

def delete8f(request,pk):
    delete8f = Student_8F.objects.get(id=pk)
    if request.method == "POST":
        delete8f.delete()
        return redirect('student-8F-t')
    context = {
        'delete8f':delete8f
    }
    return render(request,'mainapp/delete/delete8f.html',context)


def delete9a(request,pk):
    delete9a = Student_9A.objects.get(id=pk)
    if request.method == "POST":
        delete9a.delete()
        return redirect('student-9A-t')
    context = {
        'delete9a':delete9a
    }
    return render(request,'mainapp/delete/delete9a.html',context)

def delete9b(request,pk):
    delete9b = Student_9B.objects.get(id=pk)
    if request.method == "POST":
        delete9b.delete()
        return redirect('student-9B-t')
    context = {
        'delete9b':delete9b
    }
    return render(request,'mainapp/delete/delete9b.html',context)

def delete9d(request,pk):
    delete9d = Student_9D.objects.get(id=pk)
    if request.method == "POST":
        delete9d.delete()
        return redirect('student-9D-t')
    context = {
        'delete9d':delete9d
    }
    return render(request,'mainapp/delete/delete9d.html',context)

def delete9f(request,pk):
    delete9f = Student_9F.objects.get(id=pk)
    if request.method == "POST":
        delete9f.delete()
        return redirect('student-9F-t')
    context = {
        'delete9f':delete9f
    }
    return render(request,'mainapp/delete/deletef.html',context)

def delet10a(request,pk):
    delete10a = Student_10A.objects.get(id=pk)
    if request.method == "POST":
        delete10a.delete()
        return redirect('student-10A-t')
    context = {
        'delete10a':delete10a
    }
    return render(request,'mainapp/delete/delete10a.html',context)

def delete10b(request,pk):
    delete10b = Student_10B.objects.get(id=pk)
    if request.method == "POST":
        delete10b.delete()
        return redirect('student-10B-t')
    context = {
        'delete10b':delete10b
    }
    return render(request,'mainapp/delete/delete10b.html',context)

def delete10d(request,pk):
    delete10d = Student_10D.objects.get(id=pk)
    if request.method == "POST":
        delete10d.delete()
        return redirect('student-10D-t')
    context = {
        'delete10d':delete10d
    }
    return render(request,'mainapp/delete/delete10d.html',context)

def delete11a(request,pk):
    delete11a = Student_11A.objects.get(id=pk)
    if request.method == "POST":
        delete11a.delete()
        return redirect('student-11A-t')
    context = {
        'delete11a':delete11a
    }
    return render(request,'mainapp/delete/delete11a.html',context)

def delete11b(request,pk):
    delete11b = Student_11B.objects.get(id=pk)
    if request.method == "POST":
        delete11b.delete()
        return redirect('student-11B-t')
    context = {
        'delete11b':delete11b
    }
    return render(request,'mainapp/delete/delete11b.html',context)

def delete11d(request,pk):
    delete11d = Student_11D.objects.get(id=pk)
    if request.method == "POST":
        delete11d.delete()
        return redirect('student-11D-t')
    context = {
        'delete11d':delete8d
    }
    return render(request,'mainapp/delete/delete11d.html',context)

#update
def update1a(request,pk):
    student1a = Student_1A.objects.get(id=pk)
    form = Create1AForm(instance=student1a)
    if request.method == "POST":
        form = Create1AForm(request.POST,instance=student1a)
        if form.is_valid():
            form.save()
            return redirect('student-1A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create1a.html',context)

def update1b(request,pk):
    student1b = Student_1B.objects.get(id=pk)
    form = Create1BForm(instance=student1b)
    if request.method == "POST":
        form = Create1BForm(request.POST,instance=student1b)
        if form.is_valid():
            form.save()
            return redirect('student-1B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create1b.html',context)

def update1d(request,pk):
    student1d = Student_1D.objects.get(id=pk)
    form = Create1DForm(instance=student1d)
    if request.method == "POST":
        form = Create1DForm(request.POST,instance=student1d)
        if form.is_valid():
            form.save()
            return redirect('student-1D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create1d.html',context)

def update1f(request,pk):
    student1f = Student_1F.objects.get(id=pk)
    form = Create1FForm(instance=student1f)
    if request.method == "POST":
        form = Create1FForm(request.POST,instance=student1f)
        if form.is_valid():
            form.save()
            return redirect('student-1F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create1f.html',context)

def update2a(request,pk):
    student2a = Student_2A.objects.get(id=pk)
    form = Create2AForm(instance=student2a)
    if request.method == "POST":
        form = Create2AForm(request.POST,instance=student2a)
        if form.is_valid():
            form.save()
            return redirect('student-2A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create2a.html',context)

def update2b(request,pk):
    student2b = Student_2B.objects.get(id=pk)
    form = Create2BForm(instance=student2b)
    if request.method == "POST":
        form = Create1BForm(request.POST,instance=student2b)
        if form.is_valid():
            form.save()
            return redirect('student-2B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create2b.html',context)

def update2d(request,pk):
    student2d = Student_2D.objects.get(id=pk)
    form = Create2DForm(instance=student2d)
    if request.method == "POST":
        form = Create2DForm(request.POST,instance=student2d)
        if form.is_valid():
            form.save()
            return redirect('student-2D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create2d.html',context)

def update2f(request,pk):
    student2f = Student_2F.objects.get(id=pk)
    form = Create2FForm(instance=student2f)
    if request.method == "POST":
        form = Create2FForm(request.POST,instance=student2f)
        if form.is_valid():
            form.save()
            return redirect('student-2F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create2f.html',context)

def update3a(request,pk):
    student3a = Student_3A.objects.get(id=pk)
    form = Create3AForm(instance=student3a)
    if request.method == "POST":
        form = Create3AForm(request.POST,instance=student3a)
        if form.is_valid():
            form.save()
            return redirect('student-3A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create3a.html',context)

def update3b(request,pk):
    student3b = Student_1B.objects.get(id=pk)
    form = Create1BForm(instance=student3b)
    if request.method == "POST":
        form = Create1BForm(request.POST,instance=student3b)
        if form.is_valid():
            form.save()
            return redirect('student-3B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create3b.html',context)

def update3d(request,pk):
    student3d = Student_3D.objects.get(id=pk)
    form = Create3DForm(instance=student3d)
    if request.method == "POST":
        form = Create3DForm(request.POST,instance=student3d)
        if form.is_valid():
            form.save()
            return redirect('student-3D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create3d.html',context)

def update3f(request,pk):
    student3f = Student_3F.objects.get(id=pk)
    form = Create3FForm(instance=student3f)
    if request.method == "POST":
        form = Create3FForm(request.POST,instance=student3f)
        if form.is_valid():
            form.save()
            return redirect('student-3F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create3f.html',context)

def update4a(request,pk):
    student4a = Student_4A.objects.get(id=pk)
    form = Create4AForm(instance=student4a)
    if request.method == "POST":
        form = Create4AForm(request.POST,instance=student4a)
        if form.is_valid():
            form.save()
            return redirect('student-4A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create4a.html',context)

def update4b(request,pk):
    student4b = Student_4B.objects.get(id=pk)
    form = Create4BForm(instance=student4b)
    if request.method == "POST":
        form = Create4BForm(request.POST,instance=student4b)
        if form.is_valid():
            form.save()
            return redirect('student-4B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create4b.html',context)

def update4d(request,pk):
    student4d = Student_4D.objects.get(id=pk)
    form = Create4DForm(instance=student4d)
    if request.method == "POST":
        form = Create4DForm(request.POST,instance=student4d)
        if form.is_valid():
            form.save()
            return redirect('student-4D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create4d.html',context)

def update4f(request,pk):
    student4f = Student_4F.objects.get(id=pk)
    form = Create4FForm(instance=student4f)
    if request.method == "POST":
        form = Create4FForm(request.POST,instance=student4f)
        if form.is_valid():
            form.save()
            return redirect('student-4F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create4f.html',context)

def update5a(request,pk):
    student5a = Student_5A.objects.get(id=pk)
    form = Create5AForm(instance=student5a)
    if request.method == "POST":
        form = Create5AForm(request.POST,instance=student5a)
        if form.is_valid():
            form.save()
            return redirect('student-5A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create5a.html',context)

def update5b(request,pk):
    student5b = Student_5B.objects.get(id=pk)
    form = Create5BForm(instance=student5b)
    if request.method == "POST":
        form = Create5BForm(request.POST,instance=student5b)
        if form.is_valid():
            form.save()
            return redirect('student-5B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create5b.html',context)

def update5d(request,pk):
    student5d = Student_5D.objects.get(id=pk)
    form = Create5DForm(instance=student5d)
    if request.method == "POST":
        form = Create5DForm(request.POST,instance=student5d)
        if form.is_valid():
            form.save()
            return redirect('student-5D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create5d.html',context)

def update5f(request,pk):
    student5f = Student_5F.objects.get(id=pk)
    form = Create5FForm(instance=student5f)
    if request.method == "POST":
        form = Create5FForm(request.POST,instance=student5f)
        if form.is_valid():
            form.save()
            return redirect('student-5F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create5f.html',context)

def update6a(request,pk):
    student6a = Student_6A.objects.get(id=pk)
    form = Create6AForm(instance=student6a)
    if request.method == "POST":
        form = Create2AForm(request.POST,instance=student6a)
        if form.is_valid():
            form.save()
            return redirect('student-6A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create6a.html',context)

def update6b(request,pk):
    student6b = Student_6B.objects.get(id=pk)
    form = Create6BForm(instance=student6b)
    if request.method == "POST":
        form = Create6BForm(request.POST,instance=student6b)
        if form.is_valid():
            form.save()
            return redirect('student-6B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create6b.html',context)

def update6d(request,pk):
    student6d = Student_6D.objects.get(id=pk)
    form = Create6DForm(instance=student6d)
    if request.method == "POST":
        form = Create6DForm(request.POST,instance=student6d)
        if form.is_valid():
            form.save()
            return redirect('student-6D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create6d.html',context)

def update6f(request,pk):
    student6f = Student_6F.objects.get(id=pk)
    form = Create6FForm(instance=student6f)
    if request.method == "POST":
        form = Create6FForm(request.POST,instance=student6f)
        if form.is_valid():
            form.save()
            return redirect('student-6F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create6f.html',context)

def update7a(request,pk):
    student7a = Student_7A.objects.get(id=pk)
    form = Create7AForm(instance=student7a)
    if request.method == "POST":
        form = Create7AForm(request.POST,instance=student7a)
        if form.is_valid():
            form.save()
            return redirect('student-7A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create7a.html',context)

def update7b(request,pk):
    student7b = Student_7B.objects.get(id=pk)
    form = Create7BForm(instance=student7b)
    if request.method == "POST":
        form = Create7BForm(request.POST,instance=student7b)
        if form.is_valid():
            form.save()
            return redirect('student-7B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create7b.html',context)

def update7d(request,pk):
    student7d = Student_7D.objects.get(id=pk)
    form = Create7DForm(instance=student7d)
    if request.method == "POST":
        form = Create7DForm(request.POST,instance=student7d)
        if form.is_valid():
            form.save()
            return redirect('student-7D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create7d.html',context)

def update7f(request,pk):
    student7f = Student_7F.objects.get(id=pk)
    form = Create7FForm(instance=student7f)
    if request.method == "POST":
        form = Create7FForm(request.POST,instance=student7f)
        if form.is_valid():
            form.save()
            return redirect('student-3F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create7f.html',context)

def update8a(request,pk):
    student8a = Student_8A.objects.get(id=pk)
    form = Create8AForm(instance=student8a)
    if request.method == "POST":
        form = Create8AForm(request.POST,instance=student8a)
        if form.is_valid():
            form.save()
            return redirect('student-8A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create8a.html',context)

def update8b(request,pk):
    student8b = Student_8B.objects.get(id=pk)
    form = Create8BForm(instance=student8b)
    if request.method == "POST":
        form = Create8BForm(request.POST,instance=student8b)
        if form.is_valid():
            form.save()
            return redirect('student-8B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create8b.html',context)

def update8d(request,pk):
    student8d = Student_8D.objects.get(id=pk)
    form = Create8DForm(instance=student8d)
    if request.method == "POST":
        form = Create8DForm(request.POST,instance=student8d)
        if form.is_valid():
            form.save()
            return redirect('student-8D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create8d.html',context)

def update8f(request,pk):
    student8f = Student_8F.objects.get(id=pk)
    form = Create8FForm(instance=student8f)
    if request.method == "POST":
        form = Create8FForm(request.POST,instance=student8f)
        if form.is_valid():
            form.save()
            return redirect('student-8F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create8f.html',context)

def update9a(request,pk):
    student9a = Student_9A.objects.get(id=pk)
    form = Create9AForm(instance=student9a)
    if request.method == "POST":
        form = Create9AForm(request.POST,instance=student9a)
        if form.is_valid():
            form.save()
            return redirect('student-9A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create9a.html',context)

def update9b(request,pk):
    student9b = Student_9B.objects.get(id=pk)
    form = Create9BForm(instance=student9b)
    if request.method == "POST":
        form = Create9BForm(request.POST,instance=student9b)
        if form.is_valid():
            form.save()
            return redirect('student-9B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create9b.html',context)

def update9d(request,pk):
    student9d = Student_9D.objects.get(id=pk)
    form = Create9DForm(instance=student9d)
    if request.method == "POST":
        form = Create9DForm(request.POST,instance=student9d)
        if form.is_valid():
            form.save()
            return redirect('student-9D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create9d.html',context)

def update9f(request,pk):
    student9f = Student_9F.objects.get(id=pk)
    form = Create9FForm(instance=student9f)
    if request.method == "POST":
        form = Create6FForm(request.POST,instance=student9f)
        if form.is_valid():
            form.save()
            return redirect('student-9F-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create9f.html',context)

def update10a(request,pk):
    student10a = Student_10A.objects.get(id=pk)
    form = Create10AForm(instance=student10a)
    if request.method == "POST":
        form = Create10AForm(request.POST,instance=student10a)
        if form.is_valid():
            form.save()
            return redirect('student-10A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create10a.html',context)

def update10b(request,pk):
    student10b = Student_10B.objects.get(id=pk)
    form = Create10BForm(instance=student10b)
    if request.method == "POST":
        form = Create10BForm(request.POST,instance=student10b)
        if form.is_valid():
            form.save()
            return redirect('student-10B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create10b.html',context)

def update10d(request,pk):
    student10d = Student_10D.objects.get(id=pk)
    form = Create10DForm(instance=student10d)
    if request.method == "POST":
        form = Create10DForm(request.POST,instance=student10d)
        if form.is_valid():
            form.save()
            return redirect('student-10D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create10d.html',context)


def update11a(request,pk):
    student11a = Student_11A.objects.get(id=pk)
    form = Create11AForm(instance=student11a)
    if request.method == "POST":
        form = Create11AForm(request.POST,instance=student11a)
        if form.is_valid():
            form.save()
            return redirect('student-11A-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create11a.html',context)

def update11b(request,pk):
    student11b = Student_11B.objects.get(id=pk)
    form = Create11BForm(instance=student11b)
    if request.method == "POST":
        form = Create11BForm(request.POST,instance=student11b)
        if form.is_valid():
            form.save()
            return redirect('student-11B-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create11b.html',context)

def update11d(request,pk):
    student11d = Student_11D.objects.get(id=pk)
    form = Create11DForm(instance=student11d)
    if request.method == "POST":
        form = Create11DForm(request.POST,instance=student11d)
        if form.is_valid():
            form.save()
            return redirect('student-11D-t')
    context = {
        'form':form,
    }
    return render(request,'mainapp/create/create11d.html',context)


def cprofile(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
        
            CreateProfileForm()
            return redirect('profile')
    context = {
        'form': form,

    }
    return render(request,'mainapp/create_profile.html',context)

def createeforms(request):
    return render(request,'mainapp/createstuent.html')
 

def admin_table(request):
    return render(request,'mainapp/admins_table.html')  



