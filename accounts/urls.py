from accounts import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout, name='logout')
]
