from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True)

class Customer(models.Model):
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Email = models.CharField(max_length=100)
    contact = models.BigIntegerField()

class Employee(models.Model):
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=255)
    Salary = models.IntegerField()
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=16)

class Address(models.Model):
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Address_type = models.CharField(max_length=50, null=True, blank=True)
    Name = models.CharField(max_length=100)
    House_No = models.IntegerField()
    Area_Colony = models.CharField(max_length=100)
    Landmark = models.CharField(max_length=100)
    Pincode = models.IntegerField()
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Contact = models.CharField(max_length=16)

class Category(models.Model):
    Category_name = models.CharField(max_length=100)

class SubCategory(models.Model):
    Sub_Category_Name = models.CharField(max_length=100)
    Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class variation(models.Model):
    variation_name = models.CharField(max_length=100)

class variation_option(models.Model):
    variation_id = models.ForeignKey(variation, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
