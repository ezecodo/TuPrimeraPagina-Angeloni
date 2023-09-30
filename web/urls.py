from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("create/", views.create_dj, name="create_dj"),
    path("search/", views.search_dj, name="search_dj"),
    path("list/", views.list_djs, name="list_djs"),
    path("edit/<int:dj_id>/", views.edit_dj, name="edit_dj"),
    path("delete/<int:dj_id>/", views.delete_dj, name="delete_dj"),
]
