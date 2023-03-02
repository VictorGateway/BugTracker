
from django.urls import path
from .views import SignUpView, GuestLoginView

urlpatterns = [
     path("signup/", SignUpView.as_view(), name="signup"),
     path("guest/", GuestLoginView.as_view(), name="guest_login")
   
]
