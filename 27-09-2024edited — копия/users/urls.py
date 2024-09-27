from django.urls import path
from .views import UserProfileView, register, login_view, logout_view

app_name = "users"

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]