from django.urls import path
from .views import ProjectListView, AcceptProjectView, UpdateProgressView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/accept/', AcceptProjectView.as_view(), name='accept-project'),
    path('progress/<int:pk>/update/', UpdateProgressView.as_view(), name='update-progress'),
]
