from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name+' '+str(self.id)
    class Meta:
        db_table='customer'

class Vehicle(models.Model):
    name=models.CharField(max_length=255)
    color=models.CharField(max_length=50)
    cutomer =models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        db_table='vehicle'
    
class Customer_one(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name+' '+str(self.id)
    
    class Meta:
        db_table='customer_one'

class Vehicle_many(models.Model):
    name=models.CharField(max_length=255)
    color=models.CharField(max_length=50)
    cutomer =models.ForeignKey(
        Customer_one,
        on_delete=models.CASCADE,
        related_name='Vehicle_many'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        db_table='vehicle_many'

class  Worker(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Machine(models.Model):
    name= models.CharField(max_length=50)
    workers= models.ManyToManyField(
        Worker,
        related_name='Machine'
    )
    def __str__(self):
        return self.name

