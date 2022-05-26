from django.urls import path

from .views import CvView

urlpatterns = [
    path('', CvView.as_view(), name='cv'),
]
