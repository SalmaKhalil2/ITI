from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.create_project, name='create_project'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/donate/', views.donate, name='donate'),
]
