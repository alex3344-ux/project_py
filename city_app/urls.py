from django.urls import include, path
from .views import index


urlpatterns = [
    path('cities/<int:pk>', index, name='cities_view'),
]