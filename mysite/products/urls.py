from django.urls import path, include
from products import views

app_name = 'products'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
]
