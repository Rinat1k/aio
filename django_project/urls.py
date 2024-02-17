from django.urls import re_path
from aio import views

urlpatterns = [
    re_path(r"^chat/", views.chat, name="chat"),
    re_path(r"^image/", views.image, name="image"),
    re_path(r"^voice/", views.voice, name="voice"),
    re_path(r"^create_cv/", views.create_cv, name="resume"),
    re_path(r"", views.index),
]
