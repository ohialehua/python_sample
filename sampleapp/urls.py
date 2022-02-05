from django.urls import path, include
from .views import SampleAppList

urlpatterns = [
    path('', SampleAppList.as_view()),
]