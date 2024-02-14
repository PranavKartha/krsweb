from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('formtest/', include('formtest.urls')),
    path('', views.hello, name='hello'),
    path('json', views.json, name='json'),
    path('json_basictest', views.json_basictest, name='json_basictest'),
    path('krsform', views.krs, name='krs'),
    path('admin/', admin.site.urls),
]