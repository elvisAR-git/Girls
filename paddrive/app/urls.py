from django.urls import path

from .views import index, about, contact, blog, blog_detail, gallery

app_name = "app"

urlpatterns = [
    path("", index),
    path("about/", about),
    path("contact/", contact),
    path("blog/", blog),
    path("blog/<int:id>/", blog_detail),
    path("gallery/", gallery)
]
