from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]