from django.urls import include, path
from .views import index


urlpatterns = [
    path('person/<int:pk>', index, name='person_view'),
]