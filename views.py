from django.shortcuts import render, HttpResponse, redirect
from app01.models import Users
import re
# Create your views here.
def index(request):
    return render(request,"main.html")

def login(request):
    if request.method == "GET":
        return render(request,"LogIn.html")
    else :
        username = request.POST.get("username")
        """
        pwd = request.POST.get("password")
        if username == "" or username == None or pwd == "" or pwd == None:
            return render(request, 'LogIn.html',{"error_msg":"Please enter the username and password"})
        data_list=[]
        data_list=Users.objects.filter(name=username,password=pwd).first()
        #print(data_list)
        #print(data_list.name,data_list.password)
        if data_list == None:
            return render(request, 'LogIn.html',{"error_msg":"username or password error"})
        else:
            return render(request, 'user_main.html',{"user_msg":data_list.name})
        """
        return render(request, 'user_main.html',{"user_msg":username})
        """
        if data_list.name==username and data_list.password==pwd:
            return HttpResponse("success")
        else:
            return render(request, 'LogIn.html',{"error_msg":"username or password error"})
"""
        """
        if username == 'root' and password == '123':
            #return redirect("") 
            return render(request, 'user_main.html')
        else:
            return render(request, 'LogIn.html',{"error_msg":"username or password error"})
"""

def sign_up(request):
    if request.method == "GET":
        return render(request,"SignUp.html")
    else:
        username = request.POST.get("username")
        e_mail = request.POST.get("email")
        pwd = request.POST.get("password")
        Cpwd = request.POST.get("confirm-password")
        
        if username == "" or username == None or pwd == "" or pwd == None or e_mail == None or e_mail == "" or Cpwd == None or Cpwd =="":
            return render(request, 'SignUp.html',{"error_msg_empty":"All blanks must be filled"})
        
        validate_email=re.fullmatch("^[^\s@]+@[^\s@]+\.[^\s@]+$",e_mail)
        if validate_email == None:
            return render(request, 'SignUp.html',{"error_msg_email":"Please enter a valid email address"})
        
        validate_pwd=re.fullmatch("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+]).{8,}$",pwd)
        if validate_pwd == None:
            return render(request, 'SignUp.html',{"error_msg_pwd":"Password must have at least one uppercase, one lowercase, one number, and one special character and must be at least 8 characters long"})
        
        if Cpwd != pwd:
            return render(request, 'SignUp.html',{"error_msg_Cpwd":"Password and confirm password must match"})
        
        topic_list=[]
        interesting_topics = (request.POST.get("intersted1"),request.POST.get("intersted2"),request.POST.get("intersted3"),request.POST.get("intersted4"),request.POST.get("intersted5"),request.POST.get("intersted6"),request.POST.get("intersted7"),request.POST.get("intersted8"))
        for num in interesting_topics:
            if num != None:
                topic_list.append(num)
        str=","
        new_topic_list=(str.join(topic_list)) #remove square brackets and quotation mark
        Users.objects.create(name=username,password=pwd,email=e_mail,preference=new_topic_list)
        
        return redirect("/login/")
        #return HttpResponse("success")
        #return render(request,"LogIn.html")

    """
    else:
        return render(request,'SignUp.html')
    """

def user_page(request):
    if request.method == "GET":
        return render(request,"user_main.html")
    

def forgetPassword(request):
    if request.method == "GET":
        return render(request,"ForgetPassword.html")
    else:
        e_mail = request.POST.get("email")

        if e_mail == None or e_mail == "":
            return render(request, 'ForgetPassword.html',{"error_msg":"Email is empty"})
        
        validate_email=re.fullmatch("^[^\s@]+@[^\s@]+\.[^\s@]+$",e_mail)
        if validate_email == None:
            return render(request, 'ForgetPassword.html',{"error_msg":"Please enter a valid email address"})
       
        data_list=[]
        data_list=Users.objects.filter(email=e_mail).first()
        if data_list == None:
            return render(request, 'ForgetPassword.html',{"error_msg":"email error"})
        else:
            return HttpResponse("Your password: "+ data_list.password)

"""
def tpl(request):
    name="cloud"
    roles=["admin","CEO","security"]
    user_info={"name":"cloud", "salary":1000,"role":"CTO"}
    return render(request, 'fake.html',{"n1":name,"n2":roles,"n3":user_info})

"""


"""
def orm(request):
    #test
    #Users.objects.create(name="cloud",password="12345",email="cloud@123.com",preference="Sport")
    #Users.objects.create(name="Alex",password="23456",email="Alex@123.com",preference="Video")
    #Users.objects.all().delete()
    #Users.objects.filter(uid=3).delete()
   
    data_list = Users.objects.all()
    for obj in data_list:
        print(obj.uid,obj.name,obj.password,obj.email,obj.preference)
  
   #Users.objects.filter(uid=8).update(password=2929)
   return HttpResponse("success")
"""
