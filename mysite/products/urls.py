from django.urls import path, include
from products import views

app_name = 'products'

urlpatterns = [
    
    # function based index view
    # -------------------------------------------------------------------------------
    path('home/', views.index, name='index'),
    
    # class based index view
    # -------------------------------------------------------------------------------
    # path('home/', views.IndexClassView.as_view(), name='index'),
    
    # function based detail view
    # -------------------------------------------------------------------------------
    # path('detail/<int:item_id>/', views.detail, name='detail'),
    
    # class based detail view
    # -------------------------------------------------------------------------------
    path('detail/<int:pk>/', views.ProductsDetail.as_view(), name='detail'),
    
    # function based create item view
    # -------------------------------------------------------------------------------
    # path('add/', views.create_item, name='create_item'),
    
    # class based detail view
    # -------------------------------------------------------------------------------
    path('add/', views.CreateItem.as_view(), name='create_item'),
    
    # function based update item view
    # -------------------------------------------------------------------------------
    path('update/<int:id>/', views.update_item, name='update_item'),
    
    # function based delete item view
    # -------------------------------------------------------------------------------
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
