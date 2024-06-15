from .views import index
from django.urls import path, include

#Admin is already defined, the rest we are defining
urlpatterns = [
    path('', index)
]