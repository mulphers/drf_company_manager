from django.urls import include, path, re_path

from api.employee_views import GetCurrentUser
from api.task_views import (AssignTaskView, CloseTaskView, CreateTaskView,
                            GetAssignedTaskView, GetTaskView, UpdateTaskView)

app_name = 'api'

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('employee/current/', GetCurrentUser.as_view()),

    path('task/get/', GetTaskView.as_view()),
    path('task/assign/', AssignTaskView.as_view()),
    path('task/get_assigned/', GetAssignedTaskView.as_view()),
    path('task/create/', CreateTaskView.as_view()),
    path('task/update/', UpdateTaskView.as_view()),
    path('task/close/', CloseTaskView.as_view()),
]
