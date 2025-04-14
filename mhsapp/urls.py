from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view()),
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
    path('var/', VariationView.as_view()),
    path('var/<int:pk>/', VariationView.as_view()),
    path('opt/',Variation_Option_View.as_view()),
    path('opt/<int:pk>/',Variation_Option_View.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/',ProductView.as_view(),name='product'),
    path('product/<int:pk>',ProductView.as_view(),name='product'),
    path('product/<str:cat>',ProductView.as_view(),name='product'),
    path('pro/',Product_variation_Views.as_view()),
    path('pro/<int:pk>',Product_variation_Views.as_view())
]
