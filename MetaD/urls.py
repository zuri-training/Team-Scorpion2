from django.urls import path
from .views import landingPage, signup_page, login_page, aboutUs, log_out_page, dashboard, contact


urlpatterns = [
    path('', landingPage, name='first-page'),
    path('signup/', signup_page, name='sign-page'),
    path('login/', login_page, name='log-page'),
    path('about/', aboutUs, name='about-page'),
    path('logout/', log_out_page, name='log-out'),
    path('dashboard/', dashboard, name='dash-page'),
    path('contact/', contact, name='cont-page')
]
