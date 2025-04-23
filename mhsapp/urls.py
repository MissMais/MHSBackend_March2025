from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static



router=DefaultRouter()
router.register('images',ImageView)

urlpatterns = [
    path('',HomeView.as_view()),
    path('',include(router.urls)),
    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('customer/<int:pk>/', CustomerView.as_view()),
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:pk>/', EmployeeView.as_view()),
    path('address/', AddressView.as_view()),
    path('address/<int:pk>/', AddressView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),
    path('sub_category/', SubCategoryView.as_view()),
    path('sub_category/<int:pk>/', SubCategoryView.as_view()),
    path('variation/', VariationView.as_view()),
    path('variation/<int:pk>/', VariationView.as_view()),
    path('variation_option/',Variation_Option_View.as_view()),
    path('variation_option/<int:pk>/',Variation_Option_View.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/',ProductView.as_view(),name='product'),
    path('product/<int:pk>',ProductView.as_view(),name='product'),
    # path('product/<str:cat>',ProductView.as_view(),name='product'),
    path('product_variation/',Product_variation_Views.as_view()),
    path('product_variation/<int:pk>',Product_variation_Views.as_view()),
    # Image
    # path('image',ImageView.as_view()),
    # path('image/<int:pk>',ImageView.as_view()),
    path('cart_item/',Cart_item.as_view()),
    path('cart_item/<int:pk>',Cart_item.as_view()),
    path('change_password/',Change_Password.as_view())
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
