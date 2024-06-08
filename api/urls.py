from django.urls import include, path, re_path

from api.views import CreateTaskView, GetTaskView

app_name = 'api'

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('task/get/', GetTaskView.as_view()),
    path('task/create/', CreateTaskView.as_view()),
]
