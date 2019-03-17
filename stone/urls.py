from django.urls import path

from . import views

urlpatterns = [
    path('forest', views.forest, name = 'forest'),
    path('addtree', views.addtree, name = 'addtree'),
    path('edittree/<int:tree_id>', views.edittree, name = 'edittree')
]
# Edit to add id to edittree path