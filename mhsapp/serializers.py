from rest_framework import serializers
from .models import *
import base64

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
        
# variation Serializer
class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = variation
        fields = ['id', 'variation_name']

# variations option Serializer
class variation_OptionSerializer(serializers.ModelSerializer):
    variation_id = serializers.PrimaryKeyRelatedField(queryset=variation.objects.all()) 
    variation = VariationSerializer(source='variation_id', read_only=True)  

    class Meta:
        model = variation_option
        fields = ['id', 'value', 'color_code', 'variation_id', 'variation']
    
# Product Serializer
class ProductSerializer(serializers.ModelSerializer):

    Sub_Category=SubCategorySerializer(source='Sub_Category_id',read_only=True)

    class Meta:
        model=Product
        fields=['id','Product_Description','Sub_Category_id','Availability','Stock','Price','Sub_Category']
    
# Product variation Serializer
class Product_variation_serializer(serializers.ModelSerializer):
    Products = ProductSerializer(source='Product_id',read_only=True)
    variation_options = variation_OptionSerializer(source='option_id',read_only=True)

    class Meta:
        model = Product_variation
        fields=['id','Product_id','option_id','Products','variation_options']



class encoder(serializers.ImageField):
    def to_representation(self, value):
        if not value:
            return None
        
        # If the value is already a bytes-like object (i.e., base64 string), return it directly
        if isinstance(value, bytes):
            return base64.b64encode(value).decode('utf-8')

        # Otherwise, handle the ImageField
        with value.open('rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')


class ImageSerializer(serializers.ModelSerializer):
    product_variation = Product_variation_serializer(source='Product_variation_id', read_only=True)
    img_path = encoder()  # Use the custom encoder for the ImageField
    
    class Meta:
        model = image
        fields = ['id', 'img_path', 'Product_variation_id', 'product_variation']


class Cart_Serializer(serializers.ModelSerializer):
    Customer_Data = CustomerSerializer(source='Customer_id',read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'Customer_id', 'Customer_Data']