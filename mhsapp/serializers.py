from rest_framework import serializers
from .models import *

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'is_active', 'is_superuser']

# Address Serializer
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

# Customer Serializer 
class CustomerSerializer(serializers.ModelSerializer):
    # For nested response
    user = UserSerializer(source='User_id', read_only=True)
    address = AddressSerializer(source='User_id.address', read_only=True)

    class Meta:
        model = Customer
        fields = ['id','User_id', 'Email', 'contact','user', 'address']
        extra_kwargs = {
            'User_id': {'required': False}
        }


# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='User_id', read_only=True)

    class Meta:
        model = Employee
        fields = [
            'id', 'User_id', 'Address', 'Salary', 'email', 'contact',
            'user'
        ]
        extra_kwargs = {
            'User_id': {'required': False}
        }


# Category Serializer 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'Category_name']

# SubCategory Serializer
class SubCategorySerializer(serializers.ModelSerializer):
    Category = CategorySerializer(source='Category_id',read_only=True)

    class Meta:
        model = SubCategory
        fields = [
            'id', 'Sub_Category_Name', 'Category_id',
            'Category'
        ]
        