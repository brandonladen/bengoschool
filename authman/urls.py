from django.urls import path
from .views import *

urlpatterns = [
    path("doLogin/", doLogin, name='user_login'),
    path("", login_page, name='login_page'),
    path("logout_user/", logout_user, name='user_logout'),
]
