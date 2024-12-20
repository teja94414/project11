from django.urls import path
from app8.views import *

app_name="app8"

urlpatterns = [
    path ('app8/',app8,name='app8'),
]
