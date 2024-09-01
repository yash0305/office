from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.list_clients, name='list_clients'),
    path('create-client/', views.create_client, name='create_client'),
    path('clients/<int:id>/', views.client_detail, name='client_detail'),
    path('clients/<int:id>/update/', views.update_client, name='update_client'),
    path('clients/<int:id>/delete/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/projects/', views.create_project, name='create_project'),
    path('projects/', views.user_projects, name='user_projects'),
]