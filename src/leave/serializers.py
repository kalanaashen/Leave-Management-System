from .models import *
from rest_framework import serializers



class CustomUserSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model=CustomUser
        fields=['id','username','email','role']
    
    

class SuperVisorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=SuperVisor
        fields=['supervisor_type', 'supervisor']
        
        
        
class LeaveCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = [
            'leave_type',
            'from_date',
            'to_date',
            'from_date_type',
            'to_date_type',
            'reason'
        ]

class LeaveResponseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    leave_type = serializers.StringRelatedField()

    class Meta:
        model = Leave
        fields = [
            'id',
            'user',
            'leave_type',
            'from_date',
            'to_date',
            'status',
            'reason'
        ]

class LeavetypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=LeaveType
        fields="__all__"
        
class LeaveDateTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=LeaveDateType
        fields="__all__"
        
        