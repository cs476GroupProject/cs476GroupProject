# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from app01 import models
import re
from app01.models import Users
from itertools import chain

#abstract observer class
class Error(object):
	def __init__(self,errorBlock,publish):
		self.errorBlock=errorBlock
		self.publish=publish
	def update(self):
		pass

#concrete observer class
class emptyError(Error):
	def update(self):
            errorText = self.publish.error_status+ ' ' +self.errorBlock+ ' please fill all empty block'
            print(errorText)
        

class validateError(Error):
	def update(self):
            errorText = self.publish.error_status+ ' ' +self.errorBlock+' please enter a valid form'
            print(errorText)		
		
class matchError(Error):
	def update(self):
            errorText = self.publish.error_status+ ' ' +self.errorBlock+' please enter the matched content'
            print(errorText)	

class existError(Error):
     def update(self):
        errorText= self.publish.error_status+ ' ' +self.errorBlock+' please try other username'
        print(errorText)
        

#abstract publisher class
class Publish(object):
	def attach(self,error):
		pass
	def detach(self,error):
		pass
	def notify(self):
		pass
		
#concrete publisher class
class ErrorChecker(Publish):
	def __init__(self):
		self.error_list=[]
		self.error_status=""
	
	def attach(self,error):
		self.error_list.append(error)
	
	def detach(self,error):
		self.error_list.remove(error)
		
	def notify(self):
		self.error_status="error happened"
		print("some error happened")
		for item in self.error_list:
			item.update()

# Create your views here.
def index(request):
    return render(request, "main.html")

def login(request):
    publisher=ErrorChecker()
    empty=emptyError("some block is not filled",publisher)
    match=matchError("username and password is not match",publisher)
    publisher.attach(empty)
    publisher.attach(match)

    if request.method == "GET":
        return render(request, "LogIn.html")
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        if username == "" or username == None or pwd == "" or pwd == None:
            publisher.notify()
            return render(request, 'LogIn.html', {"error_msg": empty.errorBlock})
        data_list = []
        data_list = Users.objects.filter(name=username, password=pwd).first()
        if data_list == None:
            publisher.notify()
            return render(request, 'LogIn.html', {"error_msg": match.errorBlock})
        else:
            a = data_list.preference.split(',') 

        
            list_img = []
            like_list = models.Customized.objects.filter(uid=data_list.uid).all()
            if like_list is None:
                like_list = []
            for i in a:
                img = models.Website.objects.filter(sitename=i).all()
                list_img = chain(list_img, img)

            return render(request, 'user_main.html', {"user_msg": data_list.name, 'img': list_img, 'like': like_list})
        


def sign_up(request):
    publisher=ErrorChecker()
    empty=emptyError("some block is not filled",publisher)
    validate=validateError("email is not valid",publisher)
    match=matchError("confirm password and password is not match",publisher)
    exist=existError("username already exist",publisher)
    publisher.attach(empty)
    publisher.attach(validate)
    publisher.attach(match)
    publisher.attach(exist)
    if request.method == "GET":
        return render(request, "SignUp.html")
    else:
        username = request.POST.get("username")
        e_mail = request.POST.get("email")
        pwd = request.POST.get("password")
        Cpwd = request.POST.get("confirm-password")

        if username == "" or username == None or pwd == "" or pwd == None or e_mail == None or e_mail == "" or Cpwd == None or Cpwd == "":
            publisher.notify()
            return render(request, 'SignUp.html', {"error_msg_empty": empty.errorBlock})

        validate_email = re.fullmatch("^[^\s@]+@[^\s@]+\.[^\s@]+$", e_mail)
        if validate_email == None:
            publisher.notify()
            return render(request, 'SignUp.html', {"error_msg_email": validate.errorBlock})

        validate_pwd = re.fullmatch("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+]).{8,}$", pwd)
        if validate_pwd == None:
            publisher.notify()
            return render(request, 'SignUp.html', {
                "error_msg_pwd": "Password must have at least one uppercase, one lowercase, one number, and one special character and must be at least 8 characters long"})

        if Cpwd != pwd:
            publisher.notify()
            return render(request, 'SignUp.html', {"error_msg_Cpwd": match.errorBlock})
        data_list = []
        data_list = Users.objects.filter(name=username).first()
        if data_list != None:
            publisher.notify()
            return render(request, 'SignUp.html', {"error_msg_empty": exist.errorBlock})

        topic_list = []
        interesting_topics = (
            request.POST.get("intersted1"), request.POST.get("intersted2"), request.POST.get("intersted3"),
            request.POST.get("intersted4"), request.POST.get("intersted5"), request.POST.get("intersted6"),
            request.POST.get("intersted7"), request.POST.get("intersted8"))
        for num in interesting_topics:
            if num != None:
                topic_list.append(num)
        str = ","
        new_topic_list = (str.join(topic_list))  # remove square brackets and quotation mark
        Users.objects.create(name=username, password=pwd, email=e_mail, preference=new_topic_list)

        return redirect("/login/")



def user_page(request):
    publisher=ErrorChecker()
    empty=emptyError("some block is not filled",publisher)
    match=matchError("something is not match",publisher)
    if request.method == "GET":
        return redirect("/login/")
    else:
        img = request.FILES.get('img')
        if img is None:
            return render(request, 'user_main.html', {"error_msg": empty.errorBlock})
        imgname = str(img)
        username = request.POST.get('username')

        uid = models.Users.objects.filter(name=username).first().uid
        url = request.POST.get('url')
        sitename = request.POST.get('webname')
        models.Customized.objects.create(url=url,image=img,sitename=sitename,uid_id=uid,imgname=imgname)

        data_list = []
        data_list = Users.objects.filter(name=username).first()
        if data_list == None:
            return render(request, 'LogIn.html', {"error_msg": match.errorBlock})
        else:
            a = data_list.preference.split(',')
        
            list_img = []
            like_list = models.Customized.objects.filter(uid=data_list.uid).all()
            if like_list is None:
                like_list = []
            for i in a:
                img = models.Website.objects.filter(sitename=i).all()
                list_img = chain(list_img, img)

            return render(request, 'user_main.html', {"user_msg": data_list.name, 'img': list_img, 'like': like_list})


def forgetPassword(request):
    publisher=ErrorChecker()
    empty=emptyError("some block is empty",publisher)
    validate=validateError("email not valid",publisher)
    match=matchError("email and username is not match",publisher)
    publisher.attach(empty)
    publisher.attach(validate)
    publisher.attach(match)

    if request.method == "GET":
        return render(request, "ForgetPassword.html")
    else:
        e_mail = request.POST.get("email")
        uname = request.POST.get("username")
        if e_mail == None or e_mail == "":
            return render(request, 'ForgetPassword.html', {"error_msg": empty.errorBlock})

        validate_email = re.fullmatch("^[^\s@]+@[^\s@]+\.[^\s@]+$", e_mail)
        if validate_email == None:
            return render(request, 'ForgetPassword.html', {"error_msg": validate.errorBlock})

        if uname == None or uname == "":
            return render(request, 'ForgetPassword.html', {"error_msg": empty.errorBlock})

        data_list = []
        data_list = Users.objects.filter(email=e_mail, name=uname).first()
        if data_list == None:
            return render(request, 'ForgetPassword.html', {"error_msg": match.errorBlock})
        else:
            return render(request, 'passwordReturn.html', {"yourPassword": data_list.password})

def passwordReturn(request):
    if request.method == "GET":
        return render(request, "ForgetPassword.html")
    else:
        return render(request, "passwordReturn.html")

