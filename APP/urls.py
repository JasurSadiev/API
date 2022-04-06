from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('int:pk/', DetailedNewton.as_view()),
    path('', ListNewton.as_view()),
]