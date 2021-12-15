from django.urls import path
from . import views

urlpatterns = [
    path('fetch_data', views.fetch_data),
    path('predict', views.predict),
]