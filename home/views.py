from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
#from home.models import Task
from django.contrib.auth.decorators import login_required
from home.models import Contact,Product,Orders,OrderUpdate
from django.contrib import messages
from math import ceil
from PayTm import Checksum
import json
from django.views.decorators.csrf import  csrf_exempt
MERCHANT_KEY = 'addyour key'
# Create your views here.


def index(request):

    allProducts=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4) -(n/4))
        allProducts.append([prod,range(1,nSlides),nSlides])
    params={'allProducts':allProducts}

    return render(request,'index.html',params)

'''
@login_required
def addtask(request):
    if request.method =='POST':
        task=request.POST['task']
        desc=request.POST['desc']
        task=Task(task=task,desc=desc)
        task.save()
        print('The data has been saved successfully')
    return render(request,'addtask.html')

def todoList(request):
    alltasks=Task.objects.all()
    context={
      'tasks':alltasks  
    }
    return render(request,'todo_list.html',context)

    '''
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        phoneNumber=request.POST['phone']

        contact=Contact(name=name,email=email,desc=desc,phoneNumber=phoneNumber)
        contact.save()
        messages.info(request,"we will get back to you soon")
    return render(request,'contact.html')
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/login')
    if request.method=="POST":

        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
         

        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
        id = Order.order_id
        oid=str(id)
        oid=str(id)
        param_dict = {

            'MID': 'add ur merchant id',
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')

@csrf_exempt
def handlerequest(request):

    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            a=response_dict['ORDERID']
            b=response_dict['TXNAMOUNT']
            # rid=a.replace("infykart","")
           
            # print(rid)
            # filter2= Orders.objects.filter(order_id=rid)
            filter2= Orders.objects.filter(order_id=a)
            print(filter2)
            print(a,b)
            for post1 in filter2:

                post1.oid=a
                post1.amountpaid=b
                post1.paymentstatus="PAID"
                post1.save()
            print("run agede function")
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})
