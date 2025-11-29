from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='home'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),  # type: ignore[arg-type]  <-- add if static checker complains
]
