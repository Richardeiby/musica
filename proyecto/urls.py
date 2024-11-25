from django.urls import path
from django.views import View
from . import views

urlpatterns =[
    path('inicio', views.inicio, name='inicio'),
    path('body', views.body, name='body'),
    path('index', views.index, name='index'),
    path('musica/crear', views.crear, name='crear'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),

    
]