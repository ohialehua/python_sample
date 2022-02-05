from django.urls import path, include
from .views import SampleAppTest

urlpatterns = [
    path('', SampleAppTest.as_view()),
]