from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),

    path('delete-task/<int:id>/', views.delete_task, name='delete_task')
]