from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='bug_list'),
    path('create/', views.bug_create, name='bug_create'),
    path('update/<int:pk>/', views.bug_update, name='bug_update'),
    path('delete/<int:pk>/', views.bug_delete, name='bug_delete'),
]
