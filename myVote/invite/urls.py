from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('createevent/', views.Event_View, name = 'event'),
    path('signup/', views.signup_view, name = 'signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('profile/', views.login_view, name='profile'),
    
]