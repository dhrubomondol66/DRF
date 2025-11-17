from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project, Task
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProjectListSerializer, ProjectDetailSerializer, TaskSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().select_related('owner')
    permission_classes = [IsOwnerOrReadOnly,]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['owner__id']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at']

    def get_serializer_class(self):
        if self.action in ('retrive',):
            return ProjectDetailSerializer
        return ProjectListSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, method=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def task(self, request, pk=None):
        project = self.get_object()
        tasks = project.tasks.all()
        page = self.paginate_queryset(tasks)
        serializer = TaskSerializer(page or tasks, many=True, context={'request':request})
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('project', 'assignee', 'created_by').all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'due_date', 'project']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(created_at=self.request.user)
