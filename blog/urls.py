from django.urls import path
from . import views
from .views import PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages_list, name='pages_list'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
    path('pages/create/', PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/edit/', PageUpdateView.as_view(), name='page_edit'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
]