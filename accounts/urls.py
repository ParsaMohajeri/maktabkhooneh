from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'
urlpatterns = [
    path('login', views.login_view, name='login'),
    # login
    path('logout', views.logout_view, name='logout'),
    # logout
    path('signup', views.signup_view, name='signup'),
    # registration / signup
    # path('password_reset', views.reset, name='password_reset'),
    # path('change-password', views.change_password, name='change'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]