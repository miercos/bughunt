from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('product_list', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),

    path('employee/', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    path('bug/', views.bug_list, name='bug_list'),
    path('bug/<int:pk>/', views.bug_detail, name='bug_detail'),
    path('bug/create/', views.bug_create, name='bug_create'),
    path('bug/<int:pk>/update/', views.bug_update, name='bug_update'),

    
]
