from django.urls import path
from .views import landingPage, signUp,logIn


urlpatterns = [
    path('home/', landingPage, name='home-page'),
    path('signup/', signUp, name='signup-page'),
    path('login/',logIn,  name='login-page')
]
