from django.urls import include, path, re_path

app_name = 'api'

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
