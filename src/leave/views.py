from django.shortcuts import render
from  .models import *
from .serializers import *
from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class=CustomUserSerializer
    
    def get_queryset(self):
        
        return CustomUser.objects.filter(id=self.request.user.id)
        
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]   
        return [IsAuthenticated()]       
    
class SuperVisorViewSet(viewsets.ModelViewSet):
    serializer_class = SuperVisorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SuperVisor.objects.filter(user=self.request.user)
    
class LeaveViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return LeaveCreateSerializer
        return LeaveResponseSerializer

    def get_queryset(self):
        return Leave.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status="PENDING")

    permission_classes = [IsAuthenticated]
    
class LeaveTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class LeaveDateTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LeaveDateType.objects.all()
    serializer_class = LeaveDateTypeSerializer
    permission_classes = [IsAuthenticated]
    
    


class LeaveViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return LeaveCreateSerializer
        return LeaveResponseSerializer

    def get_queryset(self):
        return Leave.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status="PENDING")

    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        leave = self.get_object()
        leave.status = "APPROVED"
        leave.updated_by = request.user
        leave.save()
        return Response({"message": "Leave approved"})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        leave = self.get_object()
        leave.status = "REJECTED"
        leave.updated_by = request.user
        leave.save()
        return Response({"message": "Leave rejected"})
    
