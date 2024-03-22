from django.urls import path
from .views import OcrIndex



urlpatterns = [
    path('',OcrIndex.as_view(),name='ocr-index')
]