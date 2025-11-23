from django.urls import path
from django.views.generic import RedirectView
from .views import SignupView, LoginView


urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False), name='home'),
    path('register/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
