from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
    path('cust/', CustomerView.as_view()),
    path('cust/<int:pk>/', CustomerView.as_view()),
    path('emp/', EmployeeView.as_view()),
    path('emp/<int:pk>/', EmployeeView.as_view()),
    path('add/', AddressView.as_view()),
    path('add/<int:pk>/', AddressView.as_view()),
    path('cat/', CategoryView.as_view()),
    path('cat/<int:pk>/', CategoryView.as_view()),
    path('subcat/', SubCategoryView.as_view()),
    path('subcat/<int:pk>/', SubCategoryView.as_view()),
]
