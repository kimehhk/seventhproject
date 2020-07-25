from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('<int:blog_id>', blog.views.detail, name="detail"),
    path('add/', blog.views.add, name='add'),
    path('create', blog.views.create, name='create'),
    path('update/<int:pk>', blog.views.update, name='update'),
    path('delete/<int:pk>', blog.views.delete, name='delete'),
]
