from django.urls import path

from home.views import home

urlpatterns = [    
path("", home, name='hello world nessa porra')
]