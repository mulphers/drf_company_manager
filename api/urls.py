from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.employee_views import CreateEmployeeView, GetCurrentUser
from api.task_views import (AssignTaskView, CloseTaskView, CreateTaskView,
                            GetAssignedTaskView, GetTaskView, UpdateTaskView)

app_name = 'api'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('employee/create/', CreateEmployeeView.as_view()),
    path('employee/current/', GetCurrentUser.as_view()),

    path('task/get/', GetTaskView.as_view()),
    path('task/assign/', AssignTaskView.as_view()),
    path('task/get_assigned/', GetAssignedTaskView.as_view()),
    path('task/create/', CreateTaskView.as_view()),
    path('task/update/', UpdateTaskView.as_view()),
    path('task/close/', CloseTaskView.as_view()),
]
