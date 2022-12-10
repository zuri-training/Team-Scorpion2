from django.urls import path
from .views import landingPage, signup_page, login_page


urlpatterns = [
    path('', landingPage, name='first-page'),
    path('signup/', signup_page, name='sign-page'),
    path('login/', login_page, name='log-page')
]
