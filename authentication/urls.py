from django.urls import path
from .views.login import Login,Logout
from .views.password import ResetPassword,ForgetPassword
from .views.signup import Signup

urlpatterns = [
    path('login/',Login.as_view()),
    path('login/',Logout.as_view()),
    path('reset_password/',ResetPassword.as_view()),
    path('forget_password/',ForgetPassword.as_view()),
    path('signup/',Signup.as_view()),
]