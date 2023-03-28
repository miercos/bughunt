from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('admin-login',views.Admin_login.as_view(),name="admin-login"),
    path('logout',views.Logout.as_view(),name="Logout"),



    path('database_managment',views.database_managment,name="database_managment"),
    path('product_list/', views.product_list, name='product_list'),
    path('product/', views.product, name='product'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),

    path('employee/', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    path('bug/', views.bug_list, name='bug'),
    path('bug/<int:pk>/', views.bug_detail, name='bug_detail'),
    path('bug/create/', views.bug_create, name='bug_create'),
    path('bug/<int:pk>/update/', views.bug_update, name='bug_update'),
    path('bug/<int:pk>/delete/', views.bug_delete, name='bug_delete'),

    path('add_area/', views.add_area, name='add_area'),
    path('area/', views.area, name='area_list'),

    

    
]
