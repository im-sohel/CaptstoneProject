from django.urls import path
from . import views

app_name = 'carsApp'

urlpatterns=[ 
    path('bookvisit/', views.bookvisit, name="name_bookvisit"),
    path('visitconfirm', views.visitconf, name="name_visitconf"),
]