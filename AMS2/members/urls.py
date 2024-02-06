from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingPage, name="landing"),
    path('login/',views.login_page),
    path('signup/',views.sign_up, name="login"),
    path('logout/',views.sign_out, name="logout"),
]
