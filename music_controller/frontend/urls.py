"""URls for frontend"""

from django.urls import include, path

from .views import index

# Admin is already defined, the rest we are defining
urlpatterns = [path("", index), path("join", index), path("create", index)]
