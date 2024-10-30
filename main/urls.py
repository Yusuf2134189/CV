from django.urls import path
from main import admin, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cv_view, name='cv_view'),
]
