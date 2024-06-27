from django.urls import path
from .views import *

urlpatterns = [
    path("hv/",hview),
    path("lv/",lview),
    path("sv/",sview),
    path("uv/<int:pk>/",updateview),
    path("dv/<int:x>/",deleteview)
]