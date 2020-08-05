from django.urls import path
from . import views




urlpatterns=[

    
path ('', views.index, name="index"),
# path('deletefirstline/' , views.deletefirstline, name="deletefirstline"),
path('analyze/', views.analyze, name="analyze"),
]


