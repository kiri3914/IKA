from django.urls import path
from .views import RegistrationView, LoginView, logout

urlpatterns = [
    path("register", RegistrationView.as_view(), name='registrations'),
    path("login", LoginView.as_view(), name='login'),
    path("logout", logout, name='logout'),
]
