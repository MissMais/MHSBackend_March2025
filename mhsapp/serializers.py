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
        fields=['Product_Description','Sub_Category_id','Availability','Stock','Price','Sub_Category']
    
# Product variation Serializer
class Product_variation_serializer(serializers.ModelSerializer):
    Products = ProductSerializer(source='Product_id',read_only=True)
    variation_options = variation_OptionSerializer(source='option_id',read_only=True)

    class Meta:
        model = Product_variation
        fields=['Product_id','option_id','Products','variation_options']


class ImageSerializer(serializers.ModelSerializer):
    product_variation = Product_variation_serializer(source='Product_variation_id',read_only = True)
    # image = serializers.ImageField(required=False)
    class Meta:
        model = image
        fields = ['id','img_path','Product_variation_id','product_variation']
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None