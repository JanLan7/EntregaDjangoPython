from django.urls import path
from .views import login_view, logout_view, register_view, profile_view, edit_profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),  # Asegúrate de que esta ruta exista
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
]
