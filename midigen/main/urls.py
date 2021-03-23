from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('jojo', views.jojo, name="jojo"),
    path('form-element', views.formelement, name="form-element"),
    path('app-profile', views.appprofile, name="app-profile"),
]