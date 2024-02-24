from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerialier
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import authentication


@api_view(http_method_names=['POST', 'GET'])


def task_api(request):
    if request.method == 'POST':
        serializer = TaskSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)
    if request.method == 'GET':
        task = Task.objects.all()
        tasks = TaskSerialier(task, many=True)
        return Response(data=tasks.data)

@api_view(http_method_names=['GET', 'DELETE', 'PUT', 'PATCH'])

def task_details_api(request, pk=None):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        serializer = TaskSerialier(task)
        return Response(data=serializer.data, status=200)
    if request.method == 'DELETE':
        task.delete()
        return Response(data=None, status=204)
    if request.method == 'PUT':
        serializer = TaskSerialier(data=request.data, instance=task)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=205)
        return Response(data=serializer.errors, status=400)
    if request.method == 'PATCH':
        serializer = TaskSerialier(data=request.data, instance=task, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=205)
        return Response(data=serializer.errors, status=400)
