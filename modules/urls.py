from django.urls import path
from .views import index
from .views import list_client, create_client, update_client, delete_client
from .views import list_project, create_project, update_project, delete_project
from .views import list_requirement, create_requirement, update_requirement, delete_requirement
from .views import list_task, create_task, update_task, delete_task
from .views import list_error, create_error, update_error, delete_error
from .views import list_comment, create_comment, update_comment, delete_comment
from .views import list_rol, create_rol, update_rol, delete_rol

# in development
from .views import list_project_derivated, create_project_derivated, update_project_derivated, delete_project_derivated, view_project_derivated

urlpatterns = [
    path('', index, name = 'index'),

    path('list_client', list_client, name = 'list_client'),
    path('create_client', create_client, name = 'create_client'),
    path('update_client/<int:id>/', update_client, name = 'update_client'),
    path('delete_client/<int:id>/', delete_client, name = 'delete_client'),

    path('list_project', list_project, name = 'list_project'),
    path('create_project', create_project, name = 'create_project'),
    path('update_project/<int:id>/', update_project, name = 'update_project'),
    path('delete_project/<int:id>/', delete_project, name = 'delete_project'),

    path('list_requirement', list_requirement, name = 'list_requirement'),
    path('create_requirement', create_requirement, name = 'create_requirement'),
    path('update_requirement/<int:id>/', update_requirement, name = 'update_requirement'),
    path('delete_requirement/<int:id>/', delete_requirement, name = 'delete_requirement'),

    path('list_task', list_task, name = 'list_task'),
    path('create_task', create_task, name = 'create_task'),
    path('update_task/<int:id>/', update_task, name = 'update_task'),
    path('delete_task/<int:id>/', delete_task, name = 'delete_task'),

    path('list_error', list_error, name = 'list_error'),
    path('create_error', create_error, name = 'create_error'),
    path('update_error/<int:id>/', update_error, name = 'update_error'),
    path('delete_error/<int:id>/', delete_error, name = 'delete_error'),

    path('list_comment', list_comment, name = 'list_comment'),
    path('create_comment', create_comment, name = 'create_comment'),
    path('update_comment/<int:id>/', update_comment, name = 'update_comment'),
    path('delete_comment/<int:id>/', delete_comment, name = 'delete_comment'),

    path('list_rol', list_rol, name = 'list_rol'),
    path('create_rol', create_rol, name = 'create_rol'),
    path('update_rol/<int:id>/', update_rol, name = 'update_rol'),
    path('delete_rol/<int:id>/', delete_rol, name = 'delete_rol'),

    # in development
    path('list_project_derivated', list_project_derivated, name = 'list_project_derivated'),
    path('create_project_derivated', create_project_derivated, name = 'create_project_derivated'),
    path('update_project_derivated/<int:id>/', update_project_derivated, name = 'update_project_derivated'),
    path('delete_project_derivated/<int:id>/', delete_project_derivated, name = 'delete_project_derivated'),
    path('view_project_derivated/<int:id>/', view_project_derivated, name = 'view_project_derivated'),
]
