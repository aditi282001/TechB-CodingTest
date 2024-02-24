from django.urls import path
from .views import task_api, task_details_api

urlpatterns = [
    path('task/', task_api),
    path('tasks/<int:pk>/' , task_details_api)
]