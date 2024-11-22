from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register_user, name='register'),
    path('log_out/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit_profile', views.edit_profile_view, name='edit_profile'),

]
