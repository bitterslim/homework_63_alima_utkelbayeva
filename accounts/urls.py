from django.urls import path
from accounts.views.acc_view import AccountView
from accounts.views.login_view import LoginView, logout_view
from accounts.views.register_view import RegisterView
from accounts.views.profile_view import ProfileView, UserChangeView, PasswordChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('profile/<int:pk>/password/change', PasswordChangeView.as_view(), name='password_change'),
    path('logout/', logout_view, name='logout'),
    path('seacrh/',  AccountView.as_view(), name='acc_search')
]
