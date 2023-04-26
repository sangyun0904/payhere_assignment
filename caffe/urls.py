from django.urls import path
from caffe import views

urlpatterns = [
    path('caffe/', views.ProductList.as_view()),
    path('caffe/<int:pk>/', views.ProductDetail.as_view()),
    path('caffe/signup/', views.SellerSignup.as_view()),
    path('caffe/<int:page>/<str:search>/', views.ProductSearch.as_view())
]