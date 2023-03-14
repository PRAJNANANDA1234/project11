from app1.views import *
from django.urls import path
app_name='p'
urlpatterns=[
    path('pink/',pink,name='pink')
]