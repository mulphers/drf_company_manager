from django.urls import include, path, re_path

from api.employee_views import GetCurrentUser
from api.views import CreateTaskView, GetTaskView

app_name = 'api'

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('employee/current/', GetCurrentUser.as_view()),

    path('task/get/', GetTaskView.as_view()),
    # path('task/assign/', ...),
    # path('task/get_assigned/', ...),
    path('task/create/', CreateTaskView.as_view()),
    # path('task/update/', ...),
    # path('task/delete/', ...),
]
