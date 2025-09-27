from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register),
    # Add other user-related endpoints here
]