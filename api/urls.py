from django.urls import path

from api.views import publication_list

urlpatterns = [
    path("publications/", publication_list, name="publication_list")
]