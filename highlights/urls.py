from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("worldcup/<str:videolink>", views.worldcup, name="worldcup"),
    path("premierleague/<str:videolink>", views.premierleague, name="premierleague"),
    path("comingsoon", views.comingsoon, name="comingsoon")
]
