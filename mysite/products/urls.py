from django.urls import path, include
from products import views

urlpatterns = [
    path('home/', views.index, name='index'),
]
