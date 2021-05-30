from django.urls import path
from . import views

urlpatterns = [
    path('donate_page', views.donate_page, name="donate_page"),
    path('success', views.success, name="success"),

]
