from django.shortcuts import render , redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from authshopcart.utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes ,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from home.models import Product
from math import ceil

# Create your views here.
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    allProducts=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4) -(n/4))
        allProducts.append([prod,range(1,nSlides),nSlides])
    params={'allProducts':allProducts}
    return render(request,'authshopcart/home.html',params)

def signup(request):
    print('i am signuping....')
    if(request.method=='POST'):
        email=request.POST['email']
        p1=request.POST['pass1']
        p2=request.POST['pass2']
        if p1!=p2:
            messages.warning(request,"Passwords are not matching")
            #return HttpResponse('Passwords are not matching')
            return redirect(request,'authshopcart/signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,"Email already Existing")
                return render(request,'authshopcart/signup.html')
        except:
            pass

        user=User.objects.create_user(email,email,p1)
        user.is_active=False
        user.save()
        email_subject="Active Your Account"
        message=render_to_string('authshopcart/activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
             'token' : generate_token.make_token(user)
             })
        
        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,'Activate your account by clicking the link in your mail')
        return redirect('/authshopcart/login/')
    return render(request,'authshopcart/signup.html')

class activate(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,'Account activated Successfully')
            return redirect('/authshopcart/login')
        return render(request,'authshopcart/activatefail.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def handlelogin(request):

    if request.method=='POST':
        username=request.POST['email']
        userpassword=request.POST['pass']
        myuser=authenticate(username=username,password=userpassword)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/authshopcart/home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/authshopcart/login')
    

    return render(request,'authshopcart/login.html')
@login_required
def handlelogout(request):
    logout(request)
    messages.info(request,'Logout success')
    return redirect('/authshopcart/login')