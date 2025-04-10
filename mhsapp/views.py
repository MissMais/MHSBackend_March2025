from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import *
from .serializers import *

from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError




# @api_view(["GET"])
# def home(request):
#     return Response("hello world")

class HomeView(APIView):
    def get(self,request):
        return Response("hello world")
 
# USER CRUD
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully', 'data': serializer.data})
    
    def get(self,request,pk = None):
        if pk:
            obj = User.objects.get(pk = pk)
            serializer = UserSerializer(obj)
            return Response(serializer.data)
        else:
            obj = User.objects.all()
            serializer = UserSerializer(obj,many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully', 'data': serializer.data})
        return Response(serializer.errors)
    


    def delete(self,request, pk = None):
        if pk:
            try: 
                obj = User.objects.get(pk = pk)
                obj.delete()
                return Response('data deleted successfully')

            except:
                return Response('searching for the id is not found, plz enter valid id')
      
        else:
            obj = User.objects.all()
            obj.delete()
            return Response('all data is deleted successfully')


# CUSTOMER PAYLOAD :-
# {
#   "first_name": "John",
#   "last_name": "Doe",
#   "username": "johndoe123",
#   "password": "pass123",
#   "is_active": true,
#   "is_superuser": false,
#   "Email": "john@example.com",
#   "contact": "1234567890",
#   "Address_type": "Home",
#   "Name": "John D",
#   "House_No": 123,
#   "Area_Colony": "Green Street",
#   "Landmark": "Near School",
#   "Pincode": 110001,
#   "City": "Delhi",
#   "State": "Delhi",
#   "Country": "India",
#   "Address_Contact": "1234567890"
# }



# CUSTOMER REGISTRATION 
class CustomerView(APIView):
    def post(self, request):
        
        user_data = {
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "username": request.data.get("username"),
            "password": make_password(request.data.get("password")),
            "is_active": request.data.get("is_active", True),
            "is_superuser": request.data.get("is_superuser", False),
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            return Response(user_serializer.errors)

        address_data = {
            "User_id": user.id,
            "Address_type": request.data.get("Address_type"),
            "Name": request.data.get("Name"),
            "House_No": request.data.get("House_No"),
            "Area_Colony": request.data.get("Area_Colony"),
            "Landmark": request.data.get("Landmark"),
            "Pincode": request.data.get("Pincode"),
            "City": request.data.get("City"),
            "State": request.data.get("State"),
            "Country": request.data.get("Country"),
            "Contact": request.data.get("Address_Contact")
        }
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address_serializer.save()
        else:
            user.delete()
            return Response(address_serializer.errors)

        customer_data = {
            "User_id": user.id,
            "Email": request.data.get("Email"),
            "contact": request.data.get("contact")
        }
        # print(customer_data) 
        customer_serializer = CustomerSerializer(data=customer_data)
        customer_serializer.is_valid(raise_exception=True)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response({'message': 'Customer created successfully'})
        else:
            user.delete()
            return Response(customer_serializer.errors)

    def get(self, request, pk = None):
        if pk:
            customers = Customer.objects.get(pk = pk)
            serializer = CustomerSerializer(customers)
            return Response(serializer.data)

        else:    
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
    

    def put(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Customer updated successfully'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response({'message': 'Customer deleted successfully'})


# EMPLOYEE PAYLOAD :-
# {
#   "first_name": "Alice",
#   "last_name": "Smith",
#   "username": "alicesmith",
#   "password": "pass456",
#   "is_active": 1,
#   "is_superuser": 1,
#   "Address": "Office Block B",
#   "Salary": 50000,
#   "email": "alice@example.com",
#   "contact": "9876543210"
# }


class EmployeeView(APIView):
    def post(self, request):
        user_data = {
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "username": request.data.get("username"),
            "password": make_password(request.data.get("password")),
            "is_active": request.data.get("is_active", True),
            "is_superuser": request.data.get("is_superuser", False),
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            return Response(user_serializer.errors)

        employee_data = {
            "User_id": user.id,
            "Address": request.data.get("Address"),
            "Salary": request.data.get("Salary"),
            "email": request.data.get("email"),
            "contact": request.data.get("contact")
        }
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response({'message': 'Employee created successfully'})
        else:
            user.delete()
            return Response(employee_serializer.errors)

    def get(self,request,pk = None):
        if pk:
            obj = Employee.objects.get(pk = pk)
            serializer = EmployeeSerializer(obj)
            return Response(serializer.data)
        else:
            obj = Employee.objects.all()
            serializer = EmployeeSerializer(obj,many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee updated successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response({'message': 'Employee deleted successfully'})




# ADDRESS 
class AddressView(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Address created successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def get(self,request,pk = None):
        if pk:
            obj = Address.objects.get(pk = pk)
            serializer = AddressSerializer(obj)
            return Response(serializer.data)
        else:
            obj = Address.objects.all()
            serializer = AddressSerializer(obj,many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response({'error': 'Address not found'})

        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Address updated successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response({'error': 'Address not found'})

        address.delete()
        return Response({'message': 'Address deleted successfully'})
    

# {
#     "Category_name": "burkha"
# }


# CATEGROY
class CategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category created successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def get(self,request,pk = None):
        if pk:
            obj = Category.objects.get(pk = pk)
            serializer = CategorySerializer(obj)
            return Response(serializer.data)
        else:
            obj = Category.objects.all()
            serializer = CategorySerializer(obj,many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'})

        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category updated successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def delete(self,request, pk = None):
        if pk:
            try: 
                obj = Category.objects.get(pk = pk)
                obj.delete()
                return Response('data deleted successfully')

            except:
                return Response('searching for the id is not found, plz enter valid id')
      
        else:
            obj = Category.objects.all()
            obj.delete()
            return Response('all data is deleted successfully')
    


    # {
    #     "Sub_Category_Name": "black burkha",
    #     "Category_id": 2
    # }

# SUBCATEGROY
class SubCategoryView(APIView):
    def post(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SubCategory created successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def get(self, request, pk=None):
        if pk:
            obj = SubCategory.objects.get(pk = pk)
            serializer = SubCategorySerializer(obj)
            return Response(serializer.data)

        search_query = request.query_params.get('search', '')
        if search_query:
            subcategories = SubCategory.objects.filter(Sub_Category_Name__icontains=search_query)
        else:
            subcategories = SubCategory.objects.all()

        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            subcategory = SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response({'error': 'SubCategory not found'})

        serializer = SubCategorySerializer(subcategory, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SubCategory updated successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def delete(self,request, pk = None):
        if pk:
            try: 
                obj = SubCategory.objects.get(pk = pk)
                obj.delete()
                return Response('data deleted successfully')

            except:
                return Response('searching for the id is not found, plz enter valid id')
      
        else:
            obj = SubCategory.objects.all()
            obj.delete()
            return Response('all data is deleted successfully')



# {
#     "variation_name":"uytrew"
# }
    
class VariationView(APIView):
    def post(self, request):
        serializer = VariationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Variation created successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def get(self,request,pk = None):
        if pk:
            obj = variation.objects.get(pk = pk)
            serializer = VariationSerializer(obj)
            return Response(serializer.data)
        else:
            obj = variation.objects.all()
            serializer = VariationSerializer(obj,many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            VARIATION = variation.objects.get(pk=pk)
        except variation.DoesNotExist:
            return Response({'error': 'variation not found'})

        serializer = VariationSerializer(VARIATION, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'variation updated successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def delete(self,request, pk = None):
        if pk:
            try: 
                obj = variation.objects.get(pk = pk)
                obj.delete()
                return Response('data deleted successfully')

            except:
                return Response('searching for the id is not found, plz enter valid id')
      
        else:
            obj = variation.objects.all()
            obj.delete()
            return Response('all data is deleted successfully')
        

# {
#     "variation_id":2,
#     "value":"vgfdfdd",
#     "color_code":"gefgfds"
# }

class Variation_Option_View(APIView):
    def post(self, request):
        serializer = variation_OptionSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'message': 'variation_Option created successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def get(self, request, pk=None):
        if pk:
            obj = variation_option.objects.get(pk = pk)
            serializer = variation_OptionSerializer(obj)
            return Response(serializer.data)

        search_query = request.query_params.get('search', '')
        if search_query:
            obj = variation_option.objects.filter(variaton_name__icontains=search_query)
        else:
            obj = variation_option.objects.all()

        serializer = variation_OptionSerializer(obj, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            obj = variation_option.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response({'error': 'variation_option not found'})

        serializer = variation_OptionSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'variation_option updated successfully', 'data': serializer.data})
        return Response(serializer.errors)

    def delete(self,request, pk = None):
        if pk:
            try: 
                obj = variation_option.objects.get(pk = pk)
                obj.delete()
                return Response('data deleted successfully')

            except:
                return Response('searching for the id is not found, plz enter valid id')
      
        else:
            obj = variation_option.objects.all()
            obj.delete()
            return Response('all data is deleted successfully')

class ProductView(APIView):
    def get(self,request,pk=None):
        if pk:
            obj=Product.objects.get(pk=pk)
            serializer=ProductSerializer(obj,many=False)
            return Response(serializer.data)
        else:
            obj=Product.objects.all()
            serializer=ProductSerializer(obj,many=True)
            return Response(serializer.data)
        
    def post(self,request):
        data=request.data
        serializer=ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("data added successfully")
        return Response(serializer.errors)
    
    def put(self,request,pk=None):
        data=request.data
        obj=Product.objects.get(pk=pk)
        serializer=ProductSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated successfully")
        return Response(serializer.errors)
    
    def delete(self,request,pk=None):
        obj=Product.objests.get(pk=pk)
        obj.delete()
        return Response("data deleted successfully")

# product payload
# {
# "Product_Description":"good quality clothes",
# "Sub_Category_id":1,
# "Availability":13,
# "Stock":45,
# "Price":4000
# }
        

class LoginView(APIView):
    # permission_classes = [AllowAny]  # Allow anyone to attempt login

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid username or password"}, status=400)


# Username and password for login
# {
# "username":"Sahil123",
# "password":"123"
# }

class LogoutView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=400)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout successful'})
        except TokenError:
            return Response({'error': 'Invalid or expired token'}, status=400)