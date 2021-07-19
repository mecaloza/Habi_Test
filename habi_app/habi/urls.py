from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [

    path('search-property/', views.Search_Property.as_view(), name='search'),



]
