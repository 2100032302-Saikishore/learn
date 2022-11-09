import csv

from imp import source_from_cache
from tokenize import Name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import cat,movie,music,marriage
import datetime
def dh(request):
    allevents = movie.objects.all()
    context = {'al': allevents}
    return render(request, 'dhistory.html', context)
def home(request):
    return render(request,"base.html")
def contact(request):
    return render(request,"contact.html")
def faqs(request):
    return render(request,"Faqs.html")
def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"newuserlogin.html")
def dlogin(request):
    return render(request,"dealerlogin.html")
def register(request):
    return render(request,"newuserregister.html")
def registerD(request):
    return render(request,"dealeregistration.html")
def base2(request):
    return render(request,"base2.html")
def logselect(request):
    return render(request,"select.html")
def music1(request):
    if request.method == 'POST':
        conname=request.POST['name1']
        nameor=request.POST['name2']
        conadd=request.POST['name3']
        city=request.POST['name4']
        zip=request.POST['name5']
        price=request.POST['name6']
        yaddress=request.POST['name7']
        ycity=request.POST['name8']
        zip=request.POST['name9']
        phno=request.POST['name10']
        email=request.POST['name11']
        print=(conadd,phno)
        mu=music(conname=conname,nameor=nameor,conadd=conadd,city=city,zip=zip,price=price,yaddress=yaddress,ycity=ycity,yzip=zip,phno=phno,email=email)
        mu.save()
    return render(request,"Music.html")
#def movies1(request):
#    return render(request,"movies.html")
def movies(request):
    if request.method == 'POST':
        busname=request.POST['name1']
        nameuser=request.POST['name2']
        thaddress=request.POST['name3']
        c=request.POST['name4']
        z=request.POST['name5']
        pri=request.POST['name6']
        yadd=request.POST['name7']
        yc=request.POST['name8']
        yz=request.POST['name9']
        phno=request.POST['name10']
        mail=request.POST['name11']
        print(busname,nameuser,thaddress)
        m=movie(business=busname,name=nameuser,thadd=thaddress, city=c,zip=z,price=pri, yaddress=yadd,ycity=yc, yzip=yz,phnum=phno,email=mail)
        m.save()
    return render(request,"movies.html")
# def catering(request):
#     return render(request,"catering.html")
def marriage1(request):
    if request.method == 'POST':
        hall=request.POST['name1']
        halladd=request.POST['name2']
        city=request.POST['name3']
        zip=request.POST['name4']
        pricepe=request.POST['name5']
        capacity=request.POST['name6']
        phno=request.POST['name7']
        email=request.POST['name8']
        mr=marriage(hall1=hall,halladd1=halladd,city1=city,zip1=zip,pricepe1=pricepe,capacity1=capacity,phno1=phno,email1=email)
        mr.save()
        print(phno)

    return render(request,"marriage.html")
def userregisteruser(request):
    if  request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['uname']
        passwd = request.POST['password']
        messages.info(request, 'Passwords dont match')
        date = datetime.date.today()
        user3 = User.objects.create_user(first_name = fname, last_name = lname, username = username , password = passwd , email = email, date_joined = date)
        user3.save()
        print('user created')
        return redirect('/login')

    return render(request,'newuserlogin.html')
def userloginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = auth.authenticate(username=username, password=password)
        print(username, password)
        if user1 is not None:
            auth.login(request,user1)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/login")
    else:
        return render(request,'newuserlogin.html')
#def Registered_User(request):

#def photo(request):
#     return render(request,"photo.html")
# def mail(request):
#     send_mail(
#         'test mail using django framework',#subject
#         'hello sir',#body
#         'csaikishore145@gmail.com',#from address
#         ['koushikpavani6@gmail.com','gsarathchandra1382@gmail.com'],#to address
#         fail_silently =False,
#     )
#     return print('Mail sent')
# def mail1(request):
#     with open("{% static 'try.csv' %}",'r') as f:
#         reader=csv.reader(f)
#         next(reader)
#         for name,addr in reader:
#             send_mail('Test Mail Using Django Framework',
#                       'Hello Sir/Mam This is Django Example',
#                       'csaikishore145@gmail.com',
#                       [addr],
#                       fail_silently=False,
#                       )
#         #return print("Mail Sent")
def Catering(request):
    if request.method == 'POST':
        Servicename = request.POST['name']
        Name = request.POST['name1']
        PPrice = request.POST['name2']
        Capacity = request.POST['name3']
        Mobile = request.POST['name4']
        Email = request.POST['name5']
        data = cat(sname=Servicename, name=Name, pph=PPrice,capacity=Capacity,mobile=Mobile,email=Email)#, namemanu=Name1, pricemanu=PPrice, mobile=Mobile, emailmanu=Email)
        data.save()
        print(Servicename)  # ,Name1,PPrice,Mobile,Email

    return render(request, 'catering.html')
def dr(request):
    if  request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['uname']
        passwd = request.POST['password']
        messages.info(request, 'Passwords dont match')
        date = datetime.date.today()
        user3 = User.objects.create_user(first_name = fname, last_name = lname, username = username , password = passwd , email = email, date_joined = date,is_staff=True)
        user3.save()
        print('user created')
        return redirect('/dlogin')

    return render(request,'dealerlogin.html')
def dlogin(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user1 = auth.authenticate(username=username, password=password)
            print(username, password)
            if user1 is not None:
                if user1.is_staff == True:
                    auth.login(request, user1)
                    return redirect('/base2')
                messages.info(request, 'invalid username or password')
                return redirect("/dlogin")
            else:
                messages.info(request, 'invalid username or password')
                return redirect("/dlogin")
        else:
            return render(request,'dealerlogin.html')
