from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoList_main),
    path('<int:pk>/', views.ToDoList_detail),
    path('item/', views.Item_main),
    path('item/<int:pk>/', views.Item_detail),
]