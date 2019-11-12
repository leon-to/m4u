from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('patreon/', views.patreon),
]
