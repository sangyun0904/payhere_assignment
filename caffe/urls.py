from django.urls import path
from caffe import views

urlpatterns = [
    path('caffe/', views.product_list),
    path('caffe/<int:pk>/', views.product_detail),
    path('caffe/signup/', views.seller_signup)
]