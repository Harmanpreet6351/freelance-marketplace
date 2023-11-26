from django.urls import path
import web.views as views

urlpatterns = [
    path("", view=views.index, name="index")
]