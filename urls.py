from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('search/',views.Search,name='search'),
    path('category/<str:name>/',views.Category,name='category'),
    path('country/<str:name>/',views.Country,name='country'),
]
