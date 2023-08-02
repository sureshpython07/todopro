from django.shortcuts import render,HttpResponse
from ormexamples.models import Customer,Vehicle,Customer_one,Vehicle_many, Worker,Machine
from django.template import Template

# Create your views here.
def oneToOne(request):
    customer=Customer.objects.all()
    print(customer.values())
    vehicle=Vehicle.objects.all()
    context={
        'customer' : customer,
        'vehicle'  : vehicle
    }
    return render(request,'ormex/orm.html',context)

def oneToMany(request):
    customer_one=Customer_one.objects.all()
    vehicle_many=Vehicle_many.objects.all()
    context1={
        'customer_one' : customer_one,
        'vehicle_many'  : vehicle_many
    }
    return render(request,'ormex/orm.html',context1)


def manyToMany(request):
    workers=Worker.objects.all()
    print(type(workers))
    machine=Machine.objects.all()
    context={
        'workers':workers,
        'machine':machine
        }
    return HttpResponse(content=context)