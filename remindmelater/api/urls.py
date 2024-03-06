from django.urls import path
from .views import ReminderEndpoint

urlpatterns = [
    path('reminder/', ReminderEndpoint.as_view(), name='reminder'),
]