from django.urls import path, include
from record.views import record

urlpatterns = [
    path('', record, name='record'),
]
